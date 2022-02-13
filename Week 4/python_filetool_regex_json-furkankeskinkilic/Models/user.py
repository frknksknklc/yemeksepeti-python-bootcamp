class User:
    def __init__(self, email, username, fullname,yearOfBirth, emailuserlk=1, usernamelk=1, birthMonth=0, birthDay=0, country="bos", ap=1):
        self.email = email
        self.username = username
        self.fullName = fullname
        self.emailUsrLk = emailuserlk
        self.userNameLk=usernamelk
        self.yearOfBirth = yearOfBirth
        self.birthMonth=birthMonth
        self.birthDay=birthDay
        self.country=country
        self.ap=ap


