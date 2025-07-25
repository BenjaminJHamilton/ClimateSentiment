
from psaw import PushshiftAPI
from praw import Reddit
from praw.models import Submission, Comment
from typing import Any, TypedDict

class RedditPost(TypedDict):
    id: str
    title: str
    score: int
    created_utc: int
    comments: list[str]

def fetch_posts(
    reddit: Reddit, 
    search: dict[str, Any], 
    n_comments: int = 10
) -> list[RedditPost]:

    api = PushshiftAPI(reddit)

    submissions: Any = api.search_submissions(**search)
    results: list[RedditPost] = []

    for result in submissions:
        if not hasattr(result, 'title'):
            continue
        
        # Rehydrate with full comment info
        submission: Submission = reddit.submission(id=result.id)
        submission.comment_sort = 'top'
        submission.comments.replace_more(limit=0)

        top_comments = [
            comment.body
            for comment in submission.comments.list()
            if isinstance(comment, Comment) and not comment.is_submitter
        ][:n_comments]

        results.append({
            "id": result.id,
            "title": result.title,
            "score": result.score,
            "created_utc": result.created_utc,
            "comments": top_comments
        })

    return results