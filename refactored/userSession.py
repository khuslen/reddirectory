class userSession:
    def __init__(self, subreddit):
        self.currentSubreddit = 'all'
        self.currentThread = 'hot'
        self.currentSubmission = ''
        self.currentComment = ''
        self.directories = []
        self.currentState = 'attheverystartoftheprogram' # are we in a subreddit, submission or a comment?
        self.nextNum = 0
        self.itemsArr = []
        self.layer = 1
        
    def changeThread(self):
        print "thread"

    def changeSubreddit(self):
        print "subreddit"

    def changeSubmission(self):
        print "submission"

    def changeComment(self):
        print "comment"

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
        self.currentSubreddit = 'all'
        self.currentThread = 'hot'
        self.currentSubmission = ''
        self.currentComment = ''
        self.directories = []
        self.currentState = 'attheverystartoftheprogram' 
        self.nextNum = 0
        self.itemsArr = []
        self.layer = 1

currentSession = userSession("all") # Default subreddit is all