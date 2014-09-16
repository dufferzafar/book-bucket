import os
import json
from facepy import GraphAPI

# Function added to avoid Decimal() serialization issues
# http://stackoverflow.com/a/16957370/2043048
import decimal
def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

access_token = ""
graph = GraphAPI(access_token)
me = graph.get("me")

# The folders
folder = 'data/posts'

# Gather friends
friend_list = [me['id']]
pages = graph.get("me/friends", page=True)
for page in pages:
    for friend in page['data']:
        friend_list.append(friend['id'])

# Gather posts
for friend_id in friend_list:

    print("Fetching: " + friend_id)

    posts_folder = os.path.join(folder, friend_id)
    if not os.path.isdir(posts_folder):
        os.makedirs(posts_folder)

    count = 1
    pages = graph.get(str(friend_id) + '/posts', page=True)

    for page in pages:

        post = os.path.join(posts_folder, str(count) + ".json")
        with open(post, 'w') as f:
            json.dump(page, f, indent=1, default=decimal_default)

        count = count + 1
        if count > 5:
            break
