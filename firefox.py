"""A function to get information about currently opened firefox tabs.

need pip install lz4

"""

import lz4.block

def urls_of(path_to_firefox_profile_dir: str) -> list[tuple[str, str]]:
    """Yield title and url of all tabs opened in given firefox session"""
    path = os.path.expanduser(os.path.join(path_to_firefox_profile_dir, "sessionstore-backups/recovery.jsonlz4"))
    with open(path, "rb") as fd:
        b = fd.read()
        if b[:8] == b'mozLz40\0':
            b = lz4.block.decompress(b[8:])
        jdata = json.loads(b)
        for w in jdata['windows']:
            for t in w['tabs']:
                i = t['index'] - 1
                yield t['entries'][i]['title'], t['entries'][i]['url']


for title, url in urls_of('~/.mozilla/firefox/??????.default'):
    print(title, url)
