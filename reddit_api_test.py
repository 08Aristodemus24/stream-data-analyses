import requests

import os
import praw 

from praw.models.comment_forest import CommentForest, MoreComments

from uuid import uuid4
from pathlib import Path
from dotenv import load_dotenv

from kafka import KafkaProducer

if __name__ == "__main__":
    # load env variables
    env_dir = Path('./').resolve()
    load_dotenv(os.path.join(env_dir, '.env'))

    # http://localhost:65010/reddit_callback
    # https://www.reddit.com/api/v1/authorize?client_id=CLIENT_ID&response_type=TYPE&state=RANDOM_STRING&redirect_uri=URI&duration=DURATION&scope=SCOPE_STRING
    

    # getting an access token to access the reddit api
    # reddit@reddit-VirtualBox:~$ curl -X POST -d 'grant_type=password&username=reddit_bot&password=snoo' --user 'p-jcoLKBynTLew:gko_LXELoV07ZBNUXrvWZfzE3aI' https://www.reddit.com/api/v1/access_token
    # {
    #     "access_token": "J1qK1c18UUGJFAzz9xnH56584l4", 
    #     "expires_in": 3600, 
    #     "scope": "*", 
    #     "token_type": "bearer"
    # }
    

    # equivalent python code to this curl request is the ff.
    
    # load env variables
    client_id = os.environ['REDDIT_CLIENT_ID'] 
    client_secret = os.environ['REDDIT_CLIENT_SECRET']
    username = os.environ['REDDIT_USERNAME']
    password = os.environ['REDDIT_PASSWORD']
    user_agent = f"desktop:com.sr-analyses-pipeline:0.1 (by u/{username})"

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent=user_agent,
    )

    subreddit = reddit.subreddit("Philippines")
    
    for submission in subreddit.hot(limit=2):
        # print(submission.__dict__)
        print(f"title: {submission.title}")
        print(f"score: {submission.score}")
        print(f"id: {submission.id}")
        print(f"url: {submission.url}")
        # this is a list of comments
        for i, comment in enumerate(submission.comments):
            if hasattr(comment, "body"): 
                print(f"comment {i}: {comment.body}")


    # flush() is a blocking operation. It will pause the 
    # execution of the calling thread until all previously 
    # sent records have completed their journey, meaning 
    # they have been successfully acknowledged by the Kafka
    # brokers