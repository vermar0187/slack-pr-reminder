# Posting to a Slack channel
def send_message_to_slack(text):
    from urllib import request, parse
    import json
 
    post = {"text": "{0}".format(text)}
 
    try:
        json_data = json.dumps(post)
        webhook_url = ''
        req = request.Request(webhook_url,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as e:
        print("EXCEPTION: " + str(e))

from github import Github
import os

open_prs = ''

# Environment variable SUPER_SECRET
g = Github(os.environ['SUPER_SECRET'])

repo_name = ''
repo = g.get_repo(repo_name)

branch = ''
pulls = repo.get_pulls(state='open', sort='created', base=branch)

repo_url = ''
for pr in pulls:
	open_prs += "OPEN PR: " + pr.title + " | " + repo_url + str(pr.number) + "\n"

if open_prs:
    open_prs = "```" + open_prs + "```"
    send_message_to_slack(open_prs)
