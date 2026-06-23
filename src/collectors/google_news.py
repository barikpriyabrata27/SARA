import feedparser

RSS_URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"


def fetch_top_stories(limit=10):
    """
    Fetch the latest top stories from Google News RSS.

    Args:
        limit (int): Number of news articles to return.

    Returns:
        list: List of dictionaries containing title and link.
    """

    feed = feedparser.parse(RSS_URL)

    news_list = []

    for entry in feed.entries[:limit]:
        news_list.append({
            "title": entry.title,
            "link": entry.link
        })

    return news_list
