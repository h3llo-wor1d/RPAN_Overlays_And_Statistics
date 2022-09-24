## Authentication Code based on https://github.com/Spikeedoo/SnooKey/blob/master/snookey.py
## This is just a PROTOTYPE!!! 
## I plan on recreating this in a different, more optimized language (probably c-sharp using WS) in the near future!!!

import requests, json, time, bs4, flask, flask_cors, threading, re

config = json.load(open("options.json"))
reddit = requests.session()
redditData = {}

def get_v2_cookie():
    isNotCookie = True

    while isNotCookie:
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
            print(f"Got cookie, printing session cookie: {login_flow.cookies['reddit_session']}")
            isNotCookie = False
            return login_flow.cookies["reddit_session"]
        else:
            print(f'Got errors: {login_response["json"]["errors"]}. retrying in 2s...')
            time.sleep(2)

def fetchFollowerList():
    # Literally why the fuck is this private, reddit.
    # Whatever, I made it public lmao
    global redditData
    cookie = get_v2_cookie()
    headers = {
            'Cookie': 'reddit_session=' + cookie,
            'authorization': 'Basic b2hYcG9xclpZdWIxa2c6',
            'user-agent': 'Project SnooKey/0.2',
            'content-type': 'application/json; charset=UTF-8',
    }
    r = reddit.request("GET", f"https://www.reddit.com/user/{config['username']}/followers", headers=headers) # Get all of the followers!!!
    print(r)
    hin = r.text
    followOut = [i.split("/user/")[1] for i in re.findall("<a\\b(?=[^>]* class=\"[^\"]*(?<=[\" ])_2Q3rLIRb_ij54AEsabVm9L[\" ])(?=[^>]* href=\"([^\"]*))", hin)]
    print(followOut)
    print(len(followOut))

fetchFollowerList()