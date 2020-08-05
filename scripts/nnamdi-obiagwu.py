class Intern:
    def __init__(self, fullname, biostack, language, email, slackusername):
        self.fullname = fullname
        self.biostack = biostack
        self.language = language
        self.email = email
        self.slackusername =slackusername

intern = Intern("NnamdiObiagwu", "obiagwu.nnamdi@yahoo.com",
                "Python", "Data Analytics", "@obiagwuNnamdi")
print("{},{},{},{},{}".format(
    intern.fullname, intern.email, intern.language, intern.biostack, intern.slackusername))
