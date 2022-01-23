import requests

class BotStatus():
    def __init__(self, bot_id: int=None, api_token: str=None):
        r = requests.get(f"https://discloud.app/status/bot/{bot_id}", headers={"api-token":api_token})
        result = r.json()
        headers = r.headers
        self.bot_id = result['bot_id']
        self.info = result['info']
        self.container = result['container']
        self.cpu = result['cpu']
        self.memory = result['memory']
        self.last_restart = result['last_restart']
        self.ratelimit = headers['x-ratelimit-limit']
        self.ratelimit_remaining = headers['x-ratelimit-remaining']
        self.ratelimit_reset = headers['x-ratelimit-reset']
        self.json = result

class UserStatus():
    def __init__(self, api_token: str=None):
        r = requests.get("https://discloud.app/status/user", headers={"api-token":api_token})
        result = r.json()
        headers = r.headers
        self.userID = result['userID']
        self.plan = result['plan']
        self.lastDataLeft = result['lastDataLeft']
        self.planDataEnd = result['planDataEnd']
        self.ratelimit = headers['x-ratelimit-limit']
        self.ratelimit_remaining = headers['x-ratelimit-remaining']
        self.ratelimit_reset = headers['x-ratelimit-reset']
        self.json = result
        
class BotRestart():
    def __init__(self, bot_id: str=None, api_token: str=None):
        r = requests.post(f"https://discloud.app/status/bot/{bot_id}/restart", headers={"api-token":api_token})
        result = r.json()
        headers = r.headers

        self.ratelimit = headers['x-ratelimit-limit']
        self.ratelimit_remaining = headers['x-ratelimit-remaining']
        self.ratelimit_reset = headers['x-ratelimit-reset']
        self.result = result['message']
        self.json = result


class BotLogs():
    def __init__(self, bot_id: str=None, api_token: str=None):
        r = requests.get(f"https://discloud.app/status/bot/{bot_id}/logs", headers={"api-token":api_token})
        result = r.json()
        headers = r.headers
        self.bot_id = result['bot_id']
        self.link = result['link']
        self.logs = result['logs']
        self.ratelimit = headers['x-ratelimit-limit']
        self.ratelimit_remaining = headers['x-ratelimit-remaining']
        self.ratelimit_reset = headers['x-ratelimit-reset']
        self.json = result
