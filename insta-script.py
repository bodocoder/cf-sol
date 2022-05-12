import instaloader
import datetime
L = instaloader.Instaloader()

L.login('','')

username = ""
profile = instaloader.Profile.from_username(L.context, username)

filename = username + "followers" + str(datetime.datetime.now()) + ".txt"
followers = open(filename,"a+")

for follower in profile.get_followers():
    followers.write(follower.username)
    followers.write("\n")
followers.close()

filename = username + "followees" + str(datetime.datetime.now()) + ".txt"
followees = open(filename,"a+")

for followee in profile.get_followees():
    followees.write(followee.username)
    followees.write("\n")
followees.close()