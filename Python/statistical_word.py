"""Prints most two most frequent words in repo"""
import glob
import re
from collections import Counter
from typing import List, Tuple


def get_words_stats(path_glob: str) -> Tuple[Counter, str]:
    """calculate statistics for given glob"""
    counter: Counter = Counter()
    big_mess: List[str] = []

    for path in glob.glob(path_glob):
        with open(path) as steam:
            try:
                content = steam.read()
                big_mess.append(content)
                for raw in re.split(r"[^A-Za-z]", content):
                    for part in re.split(r"(?<=[a-z])(?=[A-Z])", raw):
                        if len(part) == 5:
                            counter.update((part.lower(),))
            except OSError:
                pass
    return counter, "\n".join(big_mess)


def get_next_char(needle: str, heystack: str) -> str:
    """Return most frequent next character"""
    stats: Counter = Counter()
    for match in re.findall(needle + r"(\S)", heystack):
        stats.update(match)
    data, _ = stats.most_common(1)[0]
    return data


if __name__ == "__main__":
    STATISTICS, MESS = get_words_stats("[A-Z]*/[A-Za-z]*.*")
    MOST_COMMON = STATISTICS.most_common(2)
    LINE = " ".join([c[0].capitalize() for c in MOST_COMMON])
    END = get_next_char(LINE, MESS)
    print(LINE + END)
