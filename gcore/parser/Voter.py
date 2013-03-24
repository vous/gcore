# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:17:38 2013

@author: Siddhartha
"""

class Voter:
    def __init__(self, name="", image="", points=dict(), _id=0):
        self.name = name
        self.image = image
        self.points = points
        self._id = _id
        
    def __str__(self):
        return "%s is the voter" % self.name
