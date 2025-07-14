class User:
    
    def __init__(self, user_id, username):
        print("User is being created ...")
        self.id = user_id # self id name does not need to be the same as var passed in
        self.username = username
        self.follers = 0 # This is a default value that does not need to be passed into the object creation

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Trevor"

user_1 = User("001", "Trevor")

print(user_1.username, user_1.follers)
