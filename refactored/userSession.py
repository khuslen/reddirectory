class userSession:
    def __init__(self, subreddit):
        self.currentSubreddit = subreddit
        self.currentThread = 'hot'
        self.currentSubmission = ''
        self.currentComment = ''
        self.currentState = 'thread' # are we in a subreddit, submission or a comment?
        self.nextNum = 0
        self.nextNumComment = 0
        self.itemsArr = []

    def returnCurrentDirectory(self):
        string = self.currentSubreddit + "/"
        if self.currentThread != "":
            string += str(self.currentThread) + "/"
        if self.currentSubmission != "":
            string += str(self.currentSubmission) + "/"
        if self.currentComment != "":
            string += str(self.currentComment) + "/"
        return string

    def resetSession(self):
        self.currentSubreddit = 'popular'
        self.currentThread = 'hot'
        self.currentSubmission = ''
        self.currentComment = ''
        self.currentState = 'attheverystartoftheprogram' 
        self.nextNum = 0
        self.nextNumComment = 0
        self.itemsArr = []

    def resetThread(self):
        self.currentSubmission = ''
        self.currentComment = ''
        self.currentState = 'thread' 
        self.nextNum = 0
        self.nextNumComment = 0
        self.itemsArr = []

currentSession = userSession("popular") # Default subreddit is all