import os
import json

# The folders
folder = 'data/posts'
filter_1 = 'data/filter_1'

keywords = ['books', 'bucket', 'challenge', 'top', '10']

bucket_posts = []

# Iterate over files
for friend_id in os.listdir(filter_1):

    print("Reading: " + friend_id)

    friend_file = os.path.join(filter_1, friend_id)
    with open(friend_file) as f:
        data = json.load(f)

    for message in data['data']:
        for keyword in keywords:
            if keyword in message:
                bucket_posts.append(message)
                break

with open('data/bucket.json', 'w') as f:
    json.dump({"data": bucket_posts}, f, indent=1)
