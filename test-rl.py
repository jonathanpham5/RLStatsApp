import json
from rls.rocket import RocketLeague

key = 'KITT7IJON8TT7XAEABU1PF8DJZ2GDIMH'
rocket = RocketLeague(api_key=key)
response = rocket.players.player(id='76561198064487811', platform=1)
print(json.dumps(response.json(), indent=4))

