class Track():
    def __init__(self, performer, song, album, year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year
    
    def __str__(self):
        return "Performer: " + self.performer + "\n" + "Song: " + self.song + "\n" + "Album: " + self.album + "\n" + "Year: " + self.year + "\n"

piece = Track("War","Low Rider","Why Can't We Be Friends","1975")
print(piece)