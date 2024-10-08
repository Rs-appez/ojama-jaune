from decouple import config

#debug
DEBUG = config('DEBUG',default=False)

#token
OJAMA_JAUNE_TOKEN =config('TOKEN_OJAMA_JAUNE')
CHALLONGE_TOKEN = config('CHALLONGE_TOKEN',default='')


#role
DUELIST_ID =964988897849380934
TEAM_ID = 911384286530240533
CLOWN_ID = 1074840625024864346
CANARD_ID = 1074471615296979125
LOUP_ID = 1075882804052758538
NINJA_ID = 1077399444410073158
BAOBABOON_ID = 1077629140980727879
SINGE_ID = 1080951146476212224

#role test
BOT_DEV_ID=964950962848555008
DUELIST_ID_TEST=964896304041951334
CATEGORY_TOURNAMENT_ID_TEST = 882029388315631658
TEAM_ID_TEST = 964909150914097152

#Categorie_ID_tournament
CATEGORY_TOURNAMENT_ID = 932636106271358996

#Channel
OJAMA_CHANNEL = 967907551016542299
SALLE_D_ATTENTE = 932636241277648959
PAIRING_CHANNEL = 935258127270555648
BOT_TEST_CHANNEL = 964951777273339914
BANLIST_CHANNEL = 1277102942696112223

#Guild
GUILD_ID = config('GUILD_ID')
GUILD_APPEZ_ID = config('GUILD_APPEZ_ID')
GUILD_APPEZ_CELLAR_ID = config('GUILD_APPEZ_CELLAR_ID')

#speed
DUELIST_ID_SPEED = 979124654105055252
ADMIN_SPEED = 973978236688171078
CATEGORY_TOURNAMENT_ID_SPEED = 978042278536949820 

#backend
BACKEND_URL = config('BACKEND_URL')
BACKEND_TOKEN = config('BACKEND_TOKEN')

URL_YGOPRO = "https://db.ygoprodeck.com/api/v7/"
URL_YGORGA = "https://db.ygorganization.com/data/"
URL_TOP_DL = "https://docs.google.com/spreadsheets/d/1vUh_qSBqpPH1Ak0OTwo-2YgeQjqtoQwJlNjpWgDe-ls/htmlview#"
URL_TOP_LAMPI = "https://docs.google.com/spreadsheets/d/1yWtjcj2NeG4m9COt7sKDqTFaYCUc0-sBvGEhM2qXF0w/edit#gid=1373958324"
URL_TOP_SEBTO = "https://docs.google.com/spreadsheets/d/1mCCb2BLY-FlQ8vrza433U622fapF7vvrF0xy8Qb12sY/edit#gid=0"


#banlist
BANLIST_URL = "https://www.yugioh-card.com/en/limited/"
BANLIST_URL_DB = "https://www.db.yugioh-card.com/yugiohdb/forbidden_limited.action"
