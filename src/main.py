from collectors.google_news import fetch_top_stories
from collectors.google_news import fetch_top_stories
from storage.json_storage import save_news

def main():
    news = fetch_top_stories()
    save_news(news, "data/top_stories.json")

    print("\nTop Stories")
    print("=" * 80)

    for index, article in enumerate(news, start=1):
        print(f"\n{index}. {article['title']}")
        print(article["link"])


if __name__ == "__main__":
    main()
