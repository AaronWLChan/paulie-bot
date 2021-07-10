import praw
from prawcore.exceptions import PrawcoreException as APIException
import os
from secrets import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD
import json
import random
import logging
import time


def get_username(author):
    if not author:
        name = "[deleted]"
    else:
        name = author.name

    return name

##Note: If you test a bot in your own subreddit, PRAW will pick up deleted comments.

def main():
    ## Constants
    SUBREDDIT = "u_USERNAME"
    USER_AGENT = "My_UserAgent"
    INTERVAL = 10

    logger = logging.getLogger('redditBot')

    ## Access Bot 
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=USERNAME,
        password=PASSWORD
    )

    subreddit = reddit.subreddit(SUBREDDIT)

    ## Load Block Users not to respond to
    with open("blocked_users.json") as file:
        blocked_users = json.load(file)

    ## Load triggers
    with open("triggers.json") as file:
        triggers = json.load(file)

    ## Load Quotes
    with open("quotes.json") as file:
        quotes = json.load(file)

    ## Load Comments Replied to
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []

    else:
        with open("comments_replied_to.txt", "r") as file:
            comments_replied_to = file.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    logger.info("Starting Bot...")

    while True:

        try:
            for comment in subreddit.stream.comments():
     
                ## If comment's user is not blocked and has not been replied to
                if (comment.id not in comments_replied_to and get_username(comment.author) not in blocked_users):

                    for trigger in triggers:
                        if (trigger in comment.body.lower()):
                            
                            ##Reply and break
                            comment.reply(random.choice(quotes))
                            comments_replied_to.append(comment.id)

                            with open("comments_replied_to.txt", "w") as file:
                                file.write(comment.id + "\n")
                            break


            ## Wait 10 seconds before going again
            time.sleep(INTERVAL)

        except KeyboardInterrupt:
            logger.exception("Ctrl+C event. Stopping bot.")
            break

        except APIException as e:
            logger.exception("Encountered PRAW error: " + e)
            time.sleep(5) # Sleep and retry

if __name__ == "__main__":
    main()