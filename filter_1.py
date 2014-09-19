import os
import json

# The folders
folder = 'data/posts'
filter_1 = 'data/filter_1'

if not os.path.isdir(filter_1):
    os.makedirs(filter_1)

# Iterate over files
for friend_id in os.listdir(folder):

    friend_posts = []
    posts_folder = os.path.join(folder, friend_id)

    print("Reading: " + friend_id)

    for pages in os.listdir(posts_folder):

        pages_file = os.path.join(posts_folder, pages)
        with open(pages_file) as f:
            data = json.load(f)

        for post in data['data']:
            if 'message' in post:
                friend_posts.append(post['message'])

    friend_file = os.path.join(filter_1, friend_id + ".json")
    with open(friend_file, 'w') as f:
        json.dump({"data": friend_posts}, f, indent=1)
