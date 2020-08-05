class Intern:
    def __init__(self, fullname, biostack, language, email, slackusername):
        self.fullname = fullname
        self.biostack = biostack
        self.language = language
        self.email = email
        self.slackusername =slackusername

intern = Intern("NnamdiObiagwu", "Data Analytics",
                "Python", "obiagwu.nnamdi@yahoo.com", "@obiagwuNnamdi")
print("{},{},{},{},{}".format(
    intern.fullname, intern.email, intern.language, intern.biostack, intern.slackusername))
