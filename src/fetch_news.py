import feedparser
import json
import os
from datetime import datetime


RSS_URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"


def fetch_news():

    print("Fetching news from Google News RSS...")

    feed = feedparser.parse(RSS_URL)

    articles = []

    for entry in feed.entries[:30]:

        article = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "source": entry.source.title if "source" in entry else "Google News"
        }

        articles.append(article)

    os.makedirs("data", exist_ok=True)

    output = {
        "project": "dvc-news-37dcd",
        "fetched_at": datetime.now().isoformat(),
        "total_articles": len(articles),
        "articles": articles
    }

    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(f"Saved {len(articles)} articles to data/news.json")


if __name__ == "__main__":
    fetch_news()
