# -*- coding: utf-8 *-*

import xml.etree.ElementTree as et
import glob

class Song:
    def __init__(self, name="", artist="", image="", points=0, _id=0):
        self.name = name
        self.artist = artist
        self.points = points
        self.image = image
        self._id = _id
    
    def __str__(self):
        return "\"%s\" by %s -- %d points" % (self.name, self.artist, self.points)
        
    def add_points(self, value):
        """Adds a certain amount of points to a song"""
        self.points = self.points + value
    
    def subtract_points(self, value):
        """Subtracts a certain amount of points from a song"""
        self.points = self.points - value
        if self.points < 0:
            # Value cannot be less than 0!
            self.points = 0
            
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


def read_songs_data(main_directory=None, songs_directory=None):
    songs_location = get_songs_directory(main_directory, songs_directory)
    songs_data = get_all_songs_data(songs_location)
    return songs_data
    
def read_songs(songs_data):
    """From the songs data, return a list of 'Songs'"""
    
    all_songs = {}
    for song in songs_data:
        # Get the attributes
        name = song["name"]
        artist = song["artist"]
        image = song["image"]
        _id = song["id"]
        points = 0 # Each song starts with 0 points
        
        # Make a new 'Song'
        s = Song(name, artist, image, points, _id)
        all_songs[_id] = s
    return all_songs       


def main():
    songs_data = read_songs_data()
    all_songs = read_songs(songs_data)
    for i in range(len(all_songs)):
        print all_songs[i]
    

if __name__ == '__main__':
    main()
