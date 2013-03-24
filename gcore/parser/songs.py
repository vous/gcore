# -*- coding: utf-8 *-*

import xml.etree.ElementTree as et
import glob


def get_song_data(filename):
    """Given a location, return the song data"""
    tree = et.parse(filename)
    root = tree.getroot()
    data = {}
    for item in root:
        # a song should have all of these values
        if item.tag == "artist":
            data["artist"] = item.text
        elif item.tag == "name":
            data["name"] = item.text
        elif item.tag == "image":
            data["image"] = item.text
    return data


def get_songs_directory(main_directory=None, songs_directory=None):
    if main_directory is None:
        main_directory = "data"
    else:
        pass

    if songs_directory is None:
        songs_directory = "/songs"
    base_directory = main_directory + songs_directory

    return base_directory


def get_all_songs_data(songs_directory):
    song_files = glob.glob(songs_directory + "/*.xml")
    all_song_data = []
    number = 0
    for song in song_files:
        song_data = get_song_data(song)
        song_data["id"] = number
        all_song_data.append(song_data)
        number = number + 1
    print "Read %d songs" % (number + 1)
    return all_song_data


def read_songs(main_directory=None, songs_directory=None):
    songs_location = get_songs_directory(main_directory, songs_directory)
    songs_data = get_all_songs_data(songs_location)
    return songs_data


def main():
    print(read_songs())

if __name__ == '__main__':
    main()
