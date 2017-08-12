import json
#import urllib2
#import httplib
#import time
import praw
from praw.models import MoreComments

# Custom files
import commandFuncs


##################################################

#####   LOGIC FOR API   ##########################

##################################################

# returns top subs with title and score

itemsArr = []
subId = []

# create an instance of reddit and subreddit using praw
# Zak's credentials lolz
reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                     client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                     user_agent='inter_webz')

def main_api_logic(subReddit, subreddit_sort, nextNum):

    # Stores the listed items in an array so we can access them with a number
    global itemsArr

    this_subreddit = reddit.subreddit(subReddit[1])

    if nextNum == 0:
        storeItems(this_subreddit, subreddit_sort)

    itemNum = nextNum + 1
    for i in range(nextNum, nextNum + 10):
        print str(itemNum) + '. ' + commandFuncs.itemsArr[i].title
        itemNum += 1
# =======
    """
    mystring = "fullName (name = 'Joe', family = 'Brand')"
    result = eval(mystring)

    """


def storeItems(subreddit, subreddit_sort):


    all_submissions_pre = "subreddit." + subreddit_sort + "(limit=100)"
    all_submissions = eval(all_submissions_pre)

    # for submission in subreddit.top(limit=100):
    for submission in all_submissions:
        commandFuncs.itemsArr.append(submission)
        subId.append(submission.id)

def readPost(itemNum):
    counter = 1
    print 'reading post'
    print itemNum
    submission = reddit.submission(subId[itemNum -1])
    print (submission.selftext)

    # for top_level_comment in submission.comments:
    #     if isinstance(top_level_comment, MoreComments):
    #         continue
    #     print(str(counter) + '. '+ top_level_comment.body)
    #     counter += 1
    # Add code here that displays the main post and its comments
# <<<<<<< HEAD

    # TO-DO: Display the contents of itemsArr[itemNum]

def readComments(itemNum):
    counter = 1
    print 'read comments'
    submission = reddit.submission(subId[itemNum - 1])
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        print(str(counter) + '. ' + top_level_comment.body)
        counter += 1
        # Add code here that displays the main post and its comments

        # TO-DO: Display the contents of itemsArr[itemNum]
# =======
    print('Reading post number', itemNum)
    
    # TO-DO: Display the contents of itemsArr[itemNum]
# >>>>>>> post-pagination
