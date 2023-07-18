import service


def main():
    url: str = "https://talkpython.fm/episodes/rss"
    print_header()
    service.download_info(url)
    show_titles()


def print_header():
    print("-" * 20)
    print("     Hello World")
    print("-" * 20)


def show_titles():
    start = service.get_min_episode_id()
    end = service.get_max_episode_id()

    for episode_id in range(start, end + 1):
        show_episode_details(episode_id)


def show_episode_details(episode_id: int) -> None:
    episode = service.get_details(episode_id)
    print(f"#{episode.id} -> {episode.title}")


if __name__ == '__main__':
    main()
