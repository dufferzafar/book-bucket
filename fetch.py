import os
import json

from facepy import GraphAPI
access_token = ""
graph = GraphAPI(access_token)

# Create the output folder if it doesn't already exist
folder_posts = 'data/posts'
folder_friends = 'data/friends'

if not os.path.isdir(folder_posts):
    os.makedirs(folder_posts)
if not os.path.isdir(folder_friends):
    os.makedirs(folder_friends)

# Gather friends
count = 1
friend_pages = graph.get("me/friends", page=True)
for friend_page in friend_pages:

    friend_file = os.path.join(folder_friends, str(count) + ".json")
    with open(friend_file, 'w') as f:
        json.dump(friend_page, f, indent=1)

    count = count + 1
    if count > 5:
        break

# Gather posts
count = 1
posts_pages = graph.get('me/posts', page=True)
for posts_page in posts_pages:

    post_file = os.path.join(folder_posts, str(count) + ".json")
    with open(post_file, 'w') as f:
        json.dump(posts_page, f, indent=1)

    count = count + 1
    if count > 5:
        break
