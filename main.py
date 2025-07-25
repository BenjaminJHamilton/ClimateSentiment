
import praw
from dotenv import load_dotenv
import os

from sentiment.data import fetch_posts
from sentiment.dates import _to_timestamp


def main():

    # Load environment variables
    load_dotenv()

    reddit = praw.Reddit(
        client_id=os.getenv("client-id"),
        client_secret=os.getenv("client-secret"),
        user_agent=os.getenv("user-agent"),
    )

    search_params = {
        "subreddit": "Climate",
        "q": "climate change",
        "limit": 3,
        "sort": "top",
        "after": _to_timestamp("2021-01-01"),
        "before": _to_timestamp("2023-12-31"),
    }

    posts = fetch_posts(reddit, search=search_params)

    for post in posts:
        print(f"Title: {post['title']}")
        print(f"Score: {post['score']}")
        print(f"Created at: {post['created_utc']}")
        print("Top Comments:")
        for comment in post['comments']:
            print(f"- {comment}")
        print("\n")


if __name__ == "__main__":
    main()
