class Music():
    def __init__(self,id, title, typeOfSong):
        self.id = id
        self.title = title
        self.typeOfSong = typeOfSong

    def getData(self,id, title, typeOfSong):

    def putData(self):

    def editData(self,id, title, typeOfSong):


class Singer():
    def __init__(self, singerId, singerName):
        self.singerId = singerId
        self.singerName = singerName

    def getSingerDetail(self, singerId, singerName):


    def putSingerDetail(self, singerId, singerName):

class Song(Music, Singer):
    def __init__(self,id, title, typeOfSong, singerId, singerName):
        Singer.__init__(self, singerId, singerName)
        Music.__init__(self,id, title, typeOfSong)

    def display(self, singerName, typeOfSong):
        return "SINGERNAME: "+singerName+"\nTYPE OF SONG: "+typeOfSong





