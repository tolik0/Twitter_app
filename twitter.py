import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def list_friends(acct):

    # https://apps.twitter.com/
    # Create App and get the four strings, put them in hidden.py

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '40'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    with open("file.json", "w", encoding = "utf-8") as file:
        json.dump(js, file, ensure_ascii = False, indent = 4)

    data = []
    for user in js["users"]:
        user_info = dict()
        user_info["screen_name"] = user["screen_name"]
        user_info["name"] = user["name"]
        user_info["location"] = user["location"]
        user_info["description"] = user["description"]
        user_info["lang"] = user["lang"]
        data.append(user_info)

    with open("file1.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)

    return data
