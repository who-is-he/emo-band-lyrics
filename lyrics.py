import codecs, re, lyricsgenius
from os import environ

GENIUSKEY = environ['GENIUSKEY']

path = 'artists.txt'
genius = lyricsgenius.Genius(GENIUSKEY)
genius.remove_section_headers = True
# genius.verbose = False
genius.skip_non_songs = True

with codecs.open(path, 'r', encoding='utf-8', errors='ignore') as f:
    with codecs.open('corpus.txt', 'w', encoding='utf-8', errors='ignore') as out:
        for line in f:
            if line[0] == '#':
                continue
            artist = genius.search_artist(line, max_songs=5, sort='popularity')
            for song in artist.songs:
                out.write(song.lyrics)
                out.write('\n')
    out.close()
