import media
import fresh_tomatoes


toy_story= media.Movie("0",
					   "The Dark Knight",
					   "9/10",
					   "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
					   "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
					   "https://www.youtube.com/watch?v=EXeTwQWrcwY")

#print (toy_story.storyline)

avatar= media.Movie("1",
					"The Martian",
					"8/10",
					"An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.",
					"https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
					"https://www.youtube.com/watch?v=ej3ioOneTy8")

school_of_rock= media.Movie("2",
							"Mad Max: Fury Road",
							"8.1/10",
							"A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.",
							"https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
							"https://www.youtube.com/watch?v=hEJnMQG9ev8")

ratatouille= media.Movie("3",
						 "La La Land",
						 "8.1/10",
						 "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future.",
						 "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
						 "https://www.youtube.com/watch?v=0pdqf4P9MB8")

midnight_in_paris= media.Movie("4",
							   "The Revenant",
							   "8/10",
							   "A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.",
							   "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
							   "https://www.youtube.com/watch?v=LoebZZ8K5N0")

hunger_games= media.Movie("5",
						  "Zero Dark Thirty",
						  "7.4/10",
						  "A chronicle of the decade-long hunt for al-Qaeda terrorist leader Osama bin Laden after the September 2001 attacks, and his death at the hands of the Navy S.E.A.L.s Team 6 in May 2011.",
						  "https://upload.wikimedia.org/wikipedia/en/7/77/ZeroDarkThirty2012Poster.jpg",
						  "https://www.youtube.com/watch?v=EYFhFYoDAo4")
#print (avatar.storyline)
#avatar.show_trailer()

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)