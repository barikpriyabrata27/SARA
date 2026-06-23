import json


def save_news(news, filename):
    """
    Save news articles to a JSON file.

    Args:
        news (list): List of news articles.
        filename (str): Destination JSON file.
    """

    with open(filename, "w") as file:
        json.dump(news, file, indent=4)

