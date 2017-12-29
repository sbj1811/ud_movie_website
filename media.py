# importing webbrowser module module to open URLs
import webbrowser

# Class movie
class Movie():
	def __init__(self, movie_id, movie_title, movie_storyline, poster_image, \
		trailer_youtube, movie_rel_date, movie_director, movie_cast, movie_imdb):
		"""
    	This function initializes the object 
    	:inputs: movie_id        - index for movie
    			 movie_title     - Movie title
    			 movie_storyline - Movie Synopsis
    			 poster_image    - Movie Poster
    			 trailer_youtube - Youtube Trailer URL
    			 movie_rel_date  - Release Date
    			 movie_director  - Director
    			 movie_cast      - Movie Cast 
    			 movie_imdb      - IMDB rating 
    	"""
		self.mid = movie_id
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_date = movie_rel_date
		self.director = movie_director
		self.cast = movie_cast
		self.imdb = movie_imdb

	def show_trailer(self):
		"""
    	This function openes trailer URL for the movie object
    	:inputs: self - movie object 
    	"""
		webbrowser.open(self.trailer_youtube_url)