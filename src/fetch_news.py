import feedparser

RSS_URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

def fetch_news():
    feed = feedparser.parse(RSS_URL)

    print(f"\nFeed Title: {feed.feed.title}")
    print("=" * 80)

    for index, entry in enumerate(feed.entries[:10], start=1):
        print(f"\n{index}. {entry.title}")
        print(f"Link: {entry.link}")

if __name__ == "__main__":
    fetch_news()
