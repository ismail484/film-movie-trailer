import website

import media
import videos

toy_story= media.Movie("Toy Story",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")
#print(toy_story.storyline)


avatar= media.Movie("Avatar",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#avatar.show_trailer()


School_of_rock= media.Movie("School of Rock",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

home_alone= media.Movie("Home alone 2",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/Home_Alone_2.jpg",
                     "https://www.youtube.com/watch?v=z_An3W-oO2k")


the_rock= media.Movie("The Rock",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/8/82/The_Rock_%28movie%29.jpg",
                     "https://www.youtube.com/watch?v=313n0wga2xo")

midnight_in_paris= media.Movie("Midnight in Paris",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games= media.Movie("Hunger Games",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                     "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies=[toy_story,avatar,School_of_rock,home_alone,the_rock,midnight_in_paris,hunger_games]

website.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print( media.Movie.__doc__)
