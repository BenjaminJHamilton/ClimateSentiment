
import zstandard as zstd
import json
import io
from typing import TypedDict, Any

class RedditPost(TypedDict):
    id: str
    title: str
    subreddit: str
    created_utc: int
    score: int

def stream_submissions(file_path: str, keyword: str, max_lines: int = 1000) -> list[RedditPost]:
    
    matches = []

    with open(file_path, 'rb') as file:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(file) as reader:
            text_stream = io.TextIOWrapper(reader, encoding='utf-8')
            for line in text_stream:
                try:
                    post = json.loads(line)
                    if keyword.lower() in post.get('title').lower():
                        matches.append({
                            "id": post.get("id"),
                            "title": post.get("title"),
                            "subreddit": post.get("subreddit"),
                            "created_utc": post.get("created_utc"),
                            "score": post.get("score", 0)
                        })
                        if len(matches) >= max_lines:
                            break
                except json.JSONDecodeError:
                    continue

    return matches

    