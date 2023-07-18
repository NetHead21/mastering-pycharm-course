from dataclasses import dataclass
from typing import Optional, Dict
from xml.etree import ElementTree

import requests


@dataclass
class Episode:
    title: str
    link: str
    date: str
    id: int


episodes: Dict[int, Episode] = {}


def download_info(url: str) -> None:
    """
    This will download episode information from the urls
    :param url: the source where all episodes are found
    :return: None
    """
    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    items = dom.findall("channel/item")

    for idx, item in enumerate(items, start=0):
        e = Episode(
            title=item.find("title").text,
            link=item.find("link").text.strip(),
            date=item.find("pubDate").text,
            id=len(items) - idx
        )

        episodes[e.id] = e


def get_min_episode_id() -> int:
    """
    Returns the minimum episode from episodes
    :return: min id
    """
    return min(episodes.keys())


def get_max_episode_id() -> int:
    """
    Returns the maximum episode from episodes
    :return: max id
    """
    return max(episodes.keys())


def get_details(episode_id) -> Optional[Episode]:
    """
    Returns the episode details for the episode with ID episode_id.
    :param episode_id: the episode id to look up
    :return: Episode Object
    """
    return episodes.get(episode_id)


if __name__ == '__main__':
    url: str = "https://talkpython.fm/episodes/rss"
    download_info(url)
    print(min(episodes.keys()))
    print(max(episodes.keys()))
