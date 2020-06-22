## Slack Reminder 

This script will notify a specified slack channel of the open pull requests against a specified branch. It does use Github Actions to run
a cron job everyday at 20:00 UTC and requires the creation of a github personal access token with repo-access in order to 
authenticate with the github API. The last requirement is the creation of a Slack Application in the channel space to integrate with a webhook url.

### Links

Incoming Webhooks for Slack: https://slack.com/help/articles/115005265063-Incoming-Webhooks-for-Slack
Creating a Personal Access Token: https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line 
