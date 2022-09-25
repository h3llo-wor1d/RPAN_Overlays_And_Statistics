# https://www.reddit.com/rpan/r/shortcircuit/xn3xd9
import os, requests, praw

urlPrefix = "https://strapi.reddit.com/videos/t3_"
clientID = "CnjCnliH6Az4NXLQ2LjuVg"

def genAuth():
    reddit = praw.Reddit(
        client_id="",
        client_secret="",
        redirect_uri="http://localhost:3000/redirect",
        user_agent="",
    )
    print("Please give access to the following URL ")
    print(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))
    code = input("What is the code?")
    return reddit.auth.authorize(code)

def main():
    token = genAuth()
    

main()