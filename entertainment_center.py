import website

import media
import videos

toy_story= media.Movie("Toy Story",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")
#print(toy_story.storyline)


avatar= media.Movie("Avatar",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

#avatar.show_trailer()


School_of_rock= media.Movie("school of rock",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

home_alone= media.Movie("home_alone",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")


the_rock= media.Movie("the rock",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

midnight_in_paris= media.Movie("midnight_in_paris",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

hunger_games= media.Movie("hunger_games",5,"a story of a boy and his toys",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

movies=[toy_story,avatar,School_of_rock,home_alone,the_rock,midnight_in_paris,hunger_games]

website.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print( media.Movie.__doc__)
