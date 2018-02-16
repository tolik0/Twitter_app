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
    
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    with open("file.json", "w", encoding = "utf-8") as file:
        json.dump(js, file, ensure_ascii = False, indent = 4)

    data = dict()
    for user in js["users"]:
        screen_name = user["screen_name"]
        data[screen_name] = dict()
        data[screen_name]["name"] = user["name"]
        data[screen_name]["location"] = user["location"]
        data[screen_name]["description"] = user["description"]
        data[screen_name]["lang"] = user["lang"]

    with open("file1.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)
