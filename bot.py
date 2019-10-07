import random, os, sys
import tweepy, time
 
INTERVAL = 30

consumer_secret = "7Vjq7JwIXK9CC8E2voKersTAUg9PPqf6HegTQsDPKpD561R3on"
consumer_key = "rcocZOCcbmAQKfsi4tPkitjqY"
access_token = "831745212108124160-bP4J8jiowLpGpn9OpWRc61tro5la9Ai"
access_token_secret = "iKx7C7aIUAn3htv8c8lbxr8hr7OaABJvFdwigrukdKDBM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print ("Im running")

while True:
    
    api.update_status(media_ids=media, status='ronaldo')
    time.sleep(INTERVAL)
    
#os.remove('arquivos/' + str(foto))
