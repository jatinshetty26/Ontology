from owlready2 import *

class Song(Thing):
    def __init__(self, name):
        self.name = name

songNames = ['song1', 'song2', 'song3']

songs = []
for name in songNames:
    Song(name)