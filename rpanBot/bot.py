import os, requests
import requests, json, time, threading, re

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



urlPrefix = "https://strapi.reddit.com/videos/t3_"
reddit = requests.session()
cookie = get_v2_cookie()
payload = "{\"scopes\":[\"*\",\"email\",\"pii\"]}"
redditData = 0
        # Make request for access token

headers = {
    'Cookie': 'reddit_session=' + cookie,
    'authorization': 'Basic b2hYcG9xclpZdWIxa2c6',
    'user-agent': 'Project SnooKey/0.2',
    'content-type': 'application/json; charset=UTF-8',
    'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36",
    'referer': "https://www.reddit.com/",
    "reddit-user_id": "desktop2x",
    "content-type": "application/x-www-form-urlencoded"
}


at_req = requests.request("POST", url="https://accounts.reddit.com/api/access_token", headers=headers,
                                    data=payload)

headers['authorization'] = f"Bearer {at_req.json()['access_token']}"
headers['content-type'] = "application/json"
url = ""

currentData = 0

def getStream():
    url = input("What is the url of the stream to listen to?").split("r/")[1].split("/")[1]
    if os.path.exists(url) != True:
        r = reddit.post(f"https://strapi.reddit.com/broadcasts/t3_{url}/comment_v2", headers=headers, data=json.dumps({'text': "testing, test even!"}))
    else:
        ## Fetch websocket url from temp file
        print("placeholder")
    print(url)

def sendMessage(message):
    reddit.post(f"https://strapi.reddit.com/broadcasts/t3_{url}/comment_v2", headers=headers, data=json.dumps({'text': message}))

def fetchReddit():
    global redditData
    headers = {
        'Cookie': 'reddit_session=' + cookie,
        'authorization': 'Basic b2hYcG9xclpZdWIxa2c6',
        'user-agent': 'Project SnooKey/0.2',
        'content-type': 'application/json; charset=UTF-8',
    }
    while True:
        r = reddit.request("GET", url=f"https://www.reddit.com/user/{config['username']}/about.json", headers=headers)
        redditData = r.json()['data']['subreddit']['subscribers']
        time.sleep(2)

def fetchFollowerList():
    # Literally why the fuck is this private, reddit.
    # Whatever, I made it public lmao
    global redditData

    new_headers = {
        'Cookie': 'reddit_session=' + cookie,
        'authorization': 'Basic b2hYcG9xclpZdWIxa2c6',
        'user-agent': 'Project SnooKey/0.2',
        'content-type': 'application/json; charset=UTF-8'
    }
    r = reddit.request("GET", f"https://www.reddit.com/user/{config['username']}/followers", headers=new_headers) # Get all of the followers!!!
    hin = r.text
    return [i.split("/user/")[1] for i in re.findall("<a\\b(?=[^>]* class=\"[^\"]*(?<=[\" ])_2Q3rLIRb_ij54AEsabVm9L[\" ])(?=[^>]* href=\"([^\"]*))", hin)]

def runLogic():
    global currentData
    if redditData != currentData:
        if currentData != 0 and redditData > currentData:
            print("New Follow in Channel!")  
            followers = fetchFollowerList()
            sendMessage(f"Thank you /u/{followers[0]} for the follow!")
        currentData = redditData


def main():
    ## Main bot shit :3
    global url

    url = input("What is the url of the stream to post comments to?").split("r/")[1].split("/")[1]
    while True:
        runLogic()
        time.sleep(1)

threading.Thread(target=fetchReddit).start()
main()
