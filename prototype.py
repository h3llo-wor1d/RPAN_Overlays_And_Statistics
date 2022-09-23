## Code based on https://github.com/Spikeedoo/SnooKey/blob/master/snookey.py
import requests, json, os
import time

full_token = ""
config = json.load(open("options.json"))
cookie = ""
reddit = requests.session()

def get_v2_cookie():
    global full_token
    global config
    global cookie

    username = config['username']
    password = config['password']
    url = "https://ssl.reddit.com/api/login/" + username

    payload = {
        'api_type': 'json',
        'user': username,
        'passwd': password
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Project SnooKey/0.2'
    }

    # Make login request
    login_flow = reddit.request("POST", url, headers=headers, data=payload)
    login_response = login_flow.json()
    if len(login_response["json"]["errors"]) == 0:
        # Login worked
        # Capture session cookie
        print(f"Got cookie, printing session cookie: {login_flow.cookies['reddit_session']}")
        return login_flow.cookies["reddit_session"]
    else:
        print(login_response["json"]["errors"])

def getFollowers():
    global full_token
    cookie = get_v2_cookie()
    headers = {
            'Cookie': 'reddit_session=' + cookie,
            'authorization': 'Basic b2hYcG9xclpZdWIxa2c6',
            'user-agent': 'Project SnooKey/0.2',
            'content-type': 'application/json; charset=UTF-8',
    }
    while True:
        r = reddit.request("GET", url=f"https://www.reddit.com/user/h3llo_wor1d/about.json", headers=headers)
        headers = {
            'User-Agent': 'Project SnooKey/0.2',
            'Authorization': "Bearer " + full_token
        }
        json.dump(r.json(), open("reddit_out.json", "w+"), indent=4)
        time.sleep(1)

getFollowers()