import json
import praw
from praw.models import MoreComments
import pprint

# Custom files
import userSession
import commandFuncs
import formatOutput

subId = []

# create an instance of reddit and subreddit using praw
# Zak's credentials lolz
reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                     client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                     user_agent='inter_webz')

def storeItems(subreddit, subreddit_sort):
    all_submissions_pre = "subreddit." + subreddit_sort + "(limit=100)"
    all_submissions = eval(all_submissions_pre)

    for submission in all_submissions:
        userSession.currentSession.itemsArr.append(submission)
        subId.append(submission.id)

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
    submission = reddit.submission(subId[itemNum-1])
    formatOutput.printPost(submission)

def readComments(itemNum):
    topComments = []
    usernames = []
    print formatOutput.displayTitle('Reading comments for: ', userSession.currentSession.itemsArr[itemNum-1].title)
    submission = reddit.submission(subId[itemNum - 1])
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        topComments.append(top_level_comment.body)
        usernames.append(top_level_comment.author.name)
    
    formatOutput.printList(usernames, topComments, 0, ["32;40m", "36;40m"])
    
