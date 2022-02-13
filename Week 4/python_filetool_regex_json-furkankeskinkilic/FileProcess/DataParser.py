import json
from os import sep
from Models.user import User
 
class DataParser:
    def __init__(self,filename):
        self.filename=filename
    
    def getJsonContent(self):
        """
        Reads the Json content and return it
        """
        with open(self.filename) as json_file:
            data = json.load(json_file)
            return data
    
    def createUsersFromJSON(self):
        """
        Returns list of user objects that is read from json file 
        """
        data=self.getJsonContent()        
        allUsers = list()
        for user in data:
            email=user["email"]
            username=user["username"]
            fullName=user["profile"]["name"]
            yobData=user["profile"]["dob"].split("-")
            yearOfBirth=int(yobData[0])
            birthMonth=int(yobData[1].lstrip("0"))
            birthDay=int(yobData[2].lstrip("0"))
            emailUsrLk=1 if len("".join([i for i in set(email.split("@")[0]) if i in username]))>2 else 0
            usernamelk=1 if len([1 for i in fullName.split() if username.find(i.lower())!=-1])>0 else 0
            country=user["profile"]["address"].split()[-1]
            currentUser = User(email,username,fullName,yearOfBirth,emailUsrLk, usernamelk,birthMonth,birthDay,country)
            allUsers.append(currentUser)
        return allUsers

