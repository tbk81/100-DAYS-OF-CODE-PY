class User:

    def __init__(self, user_id, username):
        print("User is being created ...")
        self.id = user_id  # self id name does not need to be the same as var passed in
        self.username = username
        self.followers = 0  # This is a default value that does not need to be passed into the object creation
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Trevor"

user_1 = User("001", "Trevor")
user_2 = User("002", "Zora")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# https://opentdb.com/api_config.php