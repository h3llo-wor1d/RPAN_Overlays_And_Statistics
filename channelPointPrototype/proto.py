# https://www.reddit.com/rpan/r/shortcircuit/xn3xd9
import os, requests, praw

urlPrefix = "https://strapi.reddit.com/videos/t3_"
clientID = "CnjCnliH6Az4NXLQ2LjuVg"

def genAuth():
    reddit = praw.Reddit(
        client_id="6WEeuqqUXAT9dlgnxIhbfg",
        client_secret="4td21eC96le-FXn6uZKsHCvMwEe5BA",
        redirect_uri="http://localhost:3000/redirect",
        user_agent="Channel point-like system for rpan",
    )
    print("Please give access to the following URL ")
    print(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))
    code = input("What is the code?")
    return reddit.auth.authorize(code)

def main():
    token = genAuth()
    url = input("What is the url of the stream to listen to?").split("r/")[1].split("/")[1]
    if os.path.exists(url) != True:
        requests.post(f"https://strapi.reddit.com/videos/t3_{url}/heartbeat")
        r = requests.get(urlPrefix+url, headers={"Authorization": f"Bearer {token}"})
        print(r.json())
    else:
        ## Fetch websocket url from temp file
        print("placeholder")
    print(url)

main()