class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)
    
    @classmethod
    def reset(cls):
        cls.count = 0
        cls.genres = []
        cls.artists = []
        cls.genre_count = {}
        cls.artist_count = {}   
    @classmethod
    def add_song_to_count(cls):
        #increment total song count
        cls.count += 1
    @classmethod
    def add_to_genres(cls, genre=None):
        if genre:
            if genre not in cls.genres:
                cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls, artist=None):
        if artist:
            if artist not in cls.artists:
                cls.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls, genre =None):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre]=1
    @classmethod
    def add_to_artist_count(cls, artist=None):
        if artist:
            if artist in cls.artist_count:
                cls.artist_count[artist] += 1
            else:
                cls.artist_count[artist] =1
    
    @classmethod
    def get_all_song_info(cls):
        #Return a summary of all tracked song data.
        return {
            "Total Songs": cls.count,
            "Artists": cls.artists,
            "Genres": cls.genres,
            "Genre Count": cls.genre_count,
            "Artist Count": cls.artist_count
        }
                

# Create songs
# song1 = Song("Halo", "Beyonce", "Pop")
# song2 = Song("Crazy in Love", "Beyonce", "Pop")
# song3 = Song("99 Problems", "Jay-Z", "Rap")

# # # View global stats
# print(Song.get_all_song_info())
