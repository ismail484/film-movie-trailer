import website_tv
import tv
import videos

toy_story= tv.TvShow("Toy Story",5,"this is season1", "this is  channel 1",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")
#print(toy_story.storyline)


avatar= tv.TvShow("Toy Story",5,"this is season1", "this is  channel 1",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

#avatar.show_trailer()


School_of_rock= tv.TvShow("Toy Story",5,"this is season1", "this is  channel 1",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

home_alone= tv.TvShow("Toy Story",5,"this is season1", "this is  channel 1",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")


the_rock= tv.TvShow("Toy Story",5,"this is season1", "this is  channel 1",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

midnight_in_paris= tv.TvShow("Toy Story",5,"this is season1", "this is  channel 1",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

hunger_games=tv.TvShow("Toy Story",5,"this is season1", "this is  channel 1",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=4KPTXpQehio")

programs=[toy_story,avatar,School_of_rock,home_alone,the_rock,midnight_in_paris,hunger_games]

website_tv.open_movies_page(programs)

#print(media.Movie.VALID_RATINGS)
#print( media.Movie.__doc__)
