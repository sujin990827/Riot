from riotwatcher import LolWatcher, ApiError
from datetime import datetime, timedelta
import time

lol_watcher = LolWatcher('RGAPI-e737ad70-dea6-4d9b-ba0a-c3dd9d692283')
my_region = 'kr' # 지역은 북미에서 한국으로 변경해 주었다.
#target = input('검색할 닉네임을 입력하세요:\n') # 키보드 입력을 받아 닉네임을 적도록 변경

#소환사의 이름을 가지고, 소환사의 정보를 me에 담는다
me = lol_watcher.summoner.by_name(my_region, "")

spectator = None


#무한 루프를 돌린다.
while True:
    print('[*] Checking...', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # spectator(관전 api)를 소환사의 아이디로 가져올 것이다. 
    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

        # spectator 정보중에 게임시작 시간을 파이선이 알아 볼 수 있도록 바꾼다
        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)

        # 게임시작 시간과 현재 시간의 차이가 60초 이하면 알림이 오는 것이다
        if datetime.now() - start_time < timedelta(minutes=5):
            print('[!] 겜중이네..?', start_time.strftime('%Y-%m-%d %H:%M:%S'))
    except:
        pass

    time.sleep(5)