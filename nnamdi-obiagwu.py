class Intern:
    def __init__(self, fullname, biostack, language, email, slackusername):
        self.fullname = fullname
        self.biostack = biostack
        self.language = language
        self.email = email
        self.slackusername =slackusername

intern = Intern("NnamdiObiagwu", "DataAnalytics",
                "Python", "obiagwu.nnamdi@yahoo.com", "@obiagwuNnamdi")
print("Hello World, this is {} with biostack {} and email {} using {} for stage 0 task with slackusername {}.".format(
    intern.fullname, intern.biostack, intern.email, intern.language, intern.slackusername))