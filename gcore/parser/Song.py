# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:16:50 2013

@author: God
"""

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