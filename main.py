#! usr/bin/python3 
import praw 
import json

REDDIT_INSTANCE = None

def create_reddit_instance_from_config():
    '''Creates a instance of reddit from configuration json file described in README'''
    with open('reddit-app-config.json') as config_file:
        config = json.load(config_file)

        return praw.Reddit(
            client_id = config['client_id'], 
            client_secret = config['client_secret'], 
            user_agent = config['user_agent'],
            username = config['username'],
            password = config['password'])

def get_entries_from_thread(thread_url, reddit):
    submission = reddit.submission(url = thread_url)
    entries = dict()
    for comment in submission.comments:
        entries[comment.author.name] = comment.body
    return entries


if __name__ == "__main__":
    REDDIT_INSTANCE = create_reddit_instance_from_config()
    URL = 'https://www.reddit.com/r/ShitPostCrusaders/comments/caas0v/thanks_for_200k_subs_mod_applications/'
    entries = get_entries_from_thread(), REDDIT_INSTANCE)
    for key, val in entries.items():
        print(key + ': ' + val)