
import praw
from psaw import PushshiftAPI
from dotenv import load_dotenv
import os

from sentiment.data import fetch_posts


def main():

    # Load environment variables
    load_dotenv()

    reddit = praw.Reddit(
        client_id=os.getenv("client-id"),
        client_secret=os.getenv("client-secret"),
        user_agent=os.getenv("user-agent"),
    )

    api = PushshiftAPI(reddit)

    posts = fetch_posts(api)


if __name__ == "__main__":
    main()
