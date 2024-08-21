from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

import config
import requests
import asyncio
from threading import Thread
from bs4 import BeautifulSoup

class SchedulerBanlist:

    api_url = config.BACKEND_URL + "decklist/banlist/"

    def __init__(self,bot) -> None:
        self.bot=bot
        self.banlist_url = config.BANLIST_URL
        self.banlist_url_db = config.BANLIST_URL_DB
        self.last_banlist = self.__get_last_banlist()
        self.channel_id = int(config.BOT_TEST_CHANNEL)
        self.channel = None
        self.scheduler = None

        loop = asyncio.get_event_loop()

        Thread(target=self.__start, name="banlist_init", args=[loop]).start()

    def __init_schedule(self):
        job_defaults = {"coalesce": False, "max_instances": 3}
        self.scheduler.configure(job_defaults=job_defaults)

    def __add_jobs(self):
        self.scheduler.add_job(self.__check_banlist, CronTrigger(minute='*/5'), id='banlist')


    async def __check_banlist(self):   

        html = requests.get(self.banlist_url).content.decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')

        for elem in soup.find_all('a', attrs={"class": "wp-block-button__link has-text-color has-background"}):
            if 'View the list here' in elem.text:
                url = elem['href']
                break
        
        if not url:
            await self.__send_message("Error in banlist html")
            self.scheduler.remove_job('banlist') 
        
        elif url != self.last_banlist:
            await self.__send_message("Banlist updated : " + self.banlist_url_db)
            self.last_banlist = url
            self.__update_last_banlist()



    async def __send_message(self,msg):
        await self.channel.send(msg)


    def __start(self, old_loop):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.__get_channel())
        asyncio.set_event_loop(old_loop)
        self.scheduler = AsyncIOScheduler()
        self.__init_schedule()
        self.__add_jobs()
        self.scheduler.start()


    async def __get_channel(self):

        while not self.bot.init:
            await asyncio.sleep(1)
        guild = self.bot.get_guild(int(config.GUILD_ID))
        if guild :
            self.channel = guild.get_channel(self.channel_id)


    def __get_last_banlist(self):

        res = requests.get(SchedulerBanlist.api_url+"1/" ,headers={"Authorization":config.BACKEND_TOKEN})

        return res.json()['banlist_date']
    
    def __update_last_banlist(self):
        response = requests.put(SchedulerBanlist.api_url ,headers={"Authorization":config.BACKEND_TOKEN},json={"banlist_date":self.last_banlist})
        if response.status_code == 200:
            return True
        else:
            return False