from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

import config
from datetime import datetime,timedelta, timezone

class Scheduler:
    def __init__(self,bot) -> None:
        self.bot=bot
        self.scheduler = AsyncIOScheduler()
        self.__init_schedule()
        self.__add_jobs()
        self.scheduler.start()

    def __init_schedule(self):
        job_defaults = {"coalesce": False, "max_instances": 3}
        self.scheduler.configure(job_defaults=job_defaults)

    def __add_jobs(self):
        self.scheduler.add_job(self.__clear_thread, CronTrigger(minute='*/20'))


    async def __clear_thread(self):   

        guild = self.bot.get_guild(int(config.GUILD_ID))
        if guild:
            for thread in guild.get_channel(int(config.OJAMA_CHANNEL)).threads:
                async for msg in thread.history(limit=1):
                    if datetime.now(timezone.utc)- msg.created_at >  timedelta(minutes=20):
                        await thread.delete()