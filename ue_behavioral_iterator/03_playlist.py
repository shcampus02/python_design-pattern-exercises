"""
Übung 3 - Durchlaufen einer Playlist

Das Iterator-Muster ist ideal für Situationen, in denen Sie einen sequenziellen Zugriff auf Elemente in einer Kollektion benötigen.
In diesem Beispiel erstellen Sie einen Iterator, um durch eine Playlist von Songs zu gehen.

Implementieren Sie die Klassen 'Playlist', 'Song', 'Iterator' und 'PlaylistIterator'.
"""


class Playlist:
    pass


class Song:
    pass


class Iterator:
    pass


class PlaylistIterator:
    pass


if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song(Song("Yellow Submarine"))
    playlist.add_song(Song("Hey Jude"))
    iterator = playlist.create_iterator()
    while iterator.has_next():
        song = iterator.next()
        print(song.title)