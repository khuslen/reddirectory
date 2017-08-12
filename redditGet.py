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

itemsArr = []

# create an instance of reddit and subreddit using praw
# Zak's credentials lolz
reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                     client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                     user_agent='inter_webz')

def main_api_logic(subReddit):
    # Stores the listed items in an array so we can access them with a number
    global itemsArr
    

    subreddit = reddit.subreddit(subReddit)
    
    itemNum = 1
    for submission in subreddit.top(limit=10):
        commandFuncs.print_line()
        
        itemsArr.append(submission)

        print (str(itemNum) + '. Title: ')
        print(submission.title[0:10])  # Submission title
        print ('Score: ')
        print (submission.score)  # Submission Score
        itemNum += 1

def readPost(itemNum):
    global itemsArr
    
    # Add code here that displays the main post and its comments
    print('Reading post number', itemNum)
    
    # TO-DO: Display the contents of itemsArr[itemNum]