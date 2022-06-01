from turtle import pos
import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile

L = instaloader.Instaloader()

L.login('','')

username = ""
profile = instaloader.Profile.from_username(L.context, username)
# posts = profile.get_posts()
# #print(posts)
# SINCE = datetime(2021, 1, 1)
# UNTIL = datetime(2022, 4, 4)

#for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
#    print(post.date)
#    L.download_post(post, "")

# for post in posts:
#     print(post.date)
#     L.download_post(post, "")
# stories = L.get_stories()
# for story in stories:
#     for story_item in story.get_items():
#         L.download_storyitem(story_item,"instagram")
# print(profile)
# for highlight in L.get_highlights(user=profile):
#     for item in highlight.get_items():
#         L.download_storyitem(item, "instagram")

L.download_profile(profile_name="")