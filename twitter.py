import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def list_friends(acct, categories = ("screen_name", "location"), flag = "print"):

    def search(dict0, category):
        for i in dict0:
            if i == category:
                return dict0[category]
        for i in dict0:
            if type(dict0[i]) == dict:
                inf = search(dict0[i])
                if not inf:
                    return inf
        return None

    # https://apps.twitter.com/
    # Create App and get the four strings, put them in hidden.py

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)

    data = []
    for user in js["users"]:
        user_info = dict()
        for category in categories:
            inf = search(user, category)
            user_info[category] = inf
        data.append(user_info)
    if flag == "print":
        print(json.dumps(data, ensure_ascii = False, indent=4))
    elif flag == "save":
        with open("friend_info.json", "w", encoding = "utf-8") as file:
            json.dump(data, file, ensure_ascii = False, indent = 4)

    return data
