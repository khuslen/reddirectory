import json
#import urllib2
#import httplib
#import time
import praw

# Custom files
import commandFuncs

##################################################

#####   LOGIC FOR API   ##########################

##################################################

# returns top subs with title and score

# create an instance of reddit and subreddit using praw
# Zak's credentials lolz
reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                     client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                     user_agent='inter_webz')

def main_api_logic(subReddit, nextNum):
    # Stores the listed items in an array so we can access them with a number
    global itemsArr
    subreddit = reddit.subreddit(subReddit)
    
    if nextNum == 0:
        storeItems(subreddit)

    itemNum = nextNum + 1
    for i in range(nextNum, nextNum + 10):
        print str(itemNum) + '. ' + commandFuncs.itemsArr[i].title
        itemNum += 1

def storeItems(subreddit):
    for submission in subreddit.top(limit=100):
        commandFuncs.itemsArr.append(submission)

def readPost(itemNum):
   # Add code here that displays the main post and its comments
    print('Reading post number', itemNum)
    
    # TO-DO: Display the contents of itemsArr[itemNum]
