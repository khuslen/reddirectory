![img](https://github.com/khuslen/reddirectory/blob/master/reddirectory.png)

~ Terminal browser

- go to reddit home page or a specified subreddit
- use cd, cd .., ls, next, prev, etc. to browse subreddits, submissions and read comments
- use mkdir to post to a subreddit

- using the PRAW reddit API wrapper https://praw.readthedocs.io/en/latest/index.html
- Follow the steps here to create an app 
- https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

- replace the fields on the redditGet.py to be able to browse reddit
  ```reddit = praw.Reddit(client_id='**************',```
  ```client_secret='**************',```
  ```user_agent='user_name')```

                     
- replace the fields on the redditPost.py to be able to post 
  ```reddit = praw.Reddit(client_id='*************', ```
  ```client_secret='*******************', ```
  ```user_agent='user_name',```
  ```username='user_name', password='**************')```

