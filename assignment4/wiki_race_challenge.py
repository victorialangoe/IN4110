"""
Bonus task
"""
from __future__ import annotations
from ast import Dict, List, Tuple
from collections import deque

from pyparsing import Optional
from requesting_urls import get_html
from filter_urls import find_articles


def is_english_wikipedia(url: str) -> bool:
    """Check if the URL is from English Wikipedia.

    Arguments:
        url (str): the url to check

    Returns:
        bool: True if the url is from English Wikipedia, False otherwise
    """

    return "https://en.wikipedia.org/wiki/" in url


def find_path(start: str, finish: str) -> list[str]:
    """Find the shortest path from `start` to `finish`

    Arguments:
      start (str): wikipedia article URL to start from
      finish (str): wikipedia article URL to stop at

    Returns:
      urls (list[str]):
        List of URLs representing the path from `start` to `finish`.
        The first item should be `start`.
        The last item should be `finish`.
        All items of the list should be URLs for wikipedia articles.
        Each article should have a direct link to the next article in the list.
    """
    # For this task I will be using the BFS algorithm
    # This is because the articles (graphs) are unweighted

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_url, path = queue.popleft()

        if current_url == finish:
            return path

        if current_url in visited:
            continue

        visited.add(current_url)
        html = get_html(current_url)
        neighbors = find_articles(html)

        for neighbor in neighbors:
            if is_english_wikipedia(neighbor) and neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None


if __name__ == "__main__":
    start = "https://en.wikipedia.org/wiki/Nobel_Prize"
    finish = "https://en.wikipedia.org/wiki/Array_data_structure"
    urls = find_path(start, finish)

    if urls:
        print(f"Got from {start} to {finish} in {len(urls)-1} links. Here's the path:")
        for url in urls:
            print(url, "->")
    else:
        print("No path found between the given URLs.")
