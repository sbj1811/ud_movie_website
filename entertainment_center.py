# This is the Main python module

# importing 
# media module that is used to store movies info
# fresh_tomatoes will generate html sections for each movies

import media
import fresh_tomatoes

# multiple instances of that Python Class "Movie" from module Media to represent various movies
the_dark_knight= media.Movie("0",
					   "The Dark Knight",
					   "When the menace known as the Joker emerges from his mysterious past, he wreaks \
					   havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest \
					   psychological and physical tests of his ability to fight injustice.",
					   "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
					   "https://www.youtube.com/watch?v=EXeTwQWrcwY",
					   "July 18, 2008",
					   "Christopher Nolan",
				  	   "Christian Bale, Heath Ledger, Gary Oldman, Aaron Eckhart",
				  	   "9/10")

the_martian= media.Movie("1",
					"The Martian",
					"An astronaut becomes stranded on Mars after his team assume him dead, and must rely on \
					his ingenuity to find a way to signal to Earth that he is alive.",
					"https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
					"https://www.youtube.com/watch?v=ej3ioOneTy8",
					"October 2, 2015",
					"Ridley Scott",
				    "Matt Damon, Jessica Chastain, Kristen Wiig, Jeff Daniels",
					"8/10")

mad_max= media.Movie("2",
							"Mad Max: Fury Road",
							"A woman rebels against a tyrannical ruler in postapocalyptic Australia in search \
							for her home-land with the help of a group of female prisoners, a psychotic \
							worshipper, and a drifter named Max.",
							"https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
							"https://www.youtube.com/watch?v=hEJnMQG9ev8",
							"May 15, 2015",
							"George Miller",
							"Tom Hardy, Charlize Theron, Nicholas Hoult, Hugh Keays-Byrne",
							"8.1/10")

la_la_land= media.Movie("3",
						 "La La Land",
						 "While navigating their careers in Los Angeles, a pianist and an actress fall \
						 in love while attempting to reconcile their aspirations for the future.",
						 "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
						 "https://www.youtube.com/watch?v=0pdqf4P9MB8",
						 "December 9, 2016",
						 "Damien Chazelle",
						 "Ryan Gosling, Emma Stone",
						 "8.1/10")

the_revenant= media.Movie("4",
							   "The Revenant",
							   "A frontiersman on a fur trading expedition in the 1820s fights for survival \
							   after being mauled by a bear and left for dead by members of his own hunting team.",
							   "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
							   "https://www.youtube.com/watch?v=LoebZZ8K5N0",
							   "December 25, 2015",
							   "Alejandro G. Iñárritu",
							   "Leonardo DiCaprio, Tom Hardy",
							   "8/10")

zero_dark_thirty= media.Movie("5",
						  "Zero Dark Thirty",
						  "A chronicle of the decade-long hunt for al-Qaeda terrorist leader Osama bin Laden \
						  after the September 2001 attacks, and his death at the hands of the Navy S.E.A.L.s \
						  Team 6 in May 2011.",
						  "https://upload.wikimedia.org/wikipedia/en/7/77/ZeroDarkThirty2012Poster.jpg",
						  "https://www.youtube.com/watch?v=EYFhFYoDAo4",
						  "December 19, 2012",
						  "Kathryn Bigelow",
						  "Jessica Chastain, Jason Clarke, Joel Edgerton",
						  "8/10")

# grouping all the instances together in a list
movies = [the_dark_knight, the_martian, mad_max, la_la_land, the_revenant, zero_dark_thirty]

# open_movies_page from fresh_tomatoes module that takes in one argument, which is a list of movies and 
# creates an HTML file which visualizes all of your favorite movies
fresh_tomatoes.open_movies_page(movies)