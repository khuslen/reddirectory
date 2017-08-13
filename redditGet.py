import json
import praw
from praw.models import MoreComments
import pprint

# Custom files
import userSession
import commandFuncs
import formatOutput

# create an instance of reddit and subreddit using praw

#### EDIT DETAILS ################################################
reddit = praw.Reddit(client_id='your_id',
                     client_secret='your_key',
                     user_agent='your_username')
##################################################################

def storeItems(subreddit, subreddit_sort):
    all_submissions_pre = "subreddit." + subreddit_sort + "(limit=100)"
    all_submissions = eval(all_submissions_pre)

    userSession.currentSession.itemsArr = []

    for submission in all_submissions:
        userSession.currentSession.itemsArr.append(submission)
        userSession.currentSession.subId.append(submission.id)

def main_api_logic(subReddit, subreddit_sort, nextNum):
    this_subreddit = reddit.subreddit(userSession.currentSession.currentSubreddit)

    if userSession.currentSession.nextNum == 0:
        storeItems(this_subreddit, subreddit_sort)

    itemsData = []
    usernames = []
    for item in userSession.currentSession.itemsArr:
        itemsData.append(item.title)
        try:
            usernames.append(item.author.name)
        except AttributeError:
            usernames.append("Deleted user")
    formatOutput.printList(usernames, itemsData, nextNum, ["37;40m", "35;40m"])

def readPost(itemNum):
    print formatOutput.displayTitle('Reading post: ', userSession.currentSession.itemsArr[itemNum-1].title)
# <<<<<<< HEAD
#     submission = reddit.submission(subId[itemNum-1])
#     if (submission.url):
#         print submission.url
#     else:
#         formatOutput.printPost(submission)
# =======

    submission = reddit.submission(userSession.currentSession.subId[itemNum-1])
    if (submission.selftext):
        formatOutput.printPost(submission)
    else:
        print submission.url

    # formatOutput.printPost(submission)
# >>>>>>> 0cec61483b3ca682423d9af593fd2dac91d05be1

def readComments(itemNum, nextNum):
    topComments = []
    usernames = []
    print formatOutput.displayTitle('Reading comments for: ', userSession.currentSession.itemsArr[itemNum-1].title)
    submission = reddit.submission(userSession.currentSession.subId[itemNum - 1])
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        try:
            usernames.append(top_level_comment.author.name)
        except AttributeError:
            usernames.append("Deleted user")
        topComments.append(top_level_comment.body)

    formatOutput.printList(usernames, topComments, nextNum, ["32;40m", "36;40m"])
    
