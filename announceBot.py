#!/usr/bin/python3

import tweepy
import json
from pprint import pprint
import http.client



with open('twitterAPI.json') as twitterAPI:
	twitter = json.load(twitterAPI)

	'''
	consumerKey
	consumerSecret
	token
	tokenSecret
	'''
with open('discordAPI.json') as discordHook:
	discord = json.load(discordHook)

	'''
	server
	path
	'''
#pprint(discord)

auth = tweepy.OAuthHandler(twitter['consumerKey'], twitter['consumerSecret'])
auth.set_access_token(twitter['token'], twitter['tokenSecret'])
api = tweepy.API(auth)

tweet = 'Hello, world!'

discordChat = {"content":"Autoresovled wibble: https://www.youtube.com/watch?v=X73aGzh2_uQ"
			   }

'''
discordChat = { "embeds": [{"title": "Topic Title", "url": "https://example.com", 
						    "description": "This is a test for webhooks", 
						    "type": "link", 
						    "thumbnail": {"url": "https://meta-s3-cdn.global.ssl.fastly.net/original/3X/c/b/cb4bec8901221d4a646e45e1fa03db3a65e17f59.png"}
						    }
						    ]}
'''

connection = http.client.HTTPSConnection(discord['server'])
headers = {'Content-type': 'application/json'}
connection.request('POST', discord['path'], json.dumps(discordChat), headers)

response = connection.getresponse()
print(response.read().decode())

#api.update_status(status=tweet)


