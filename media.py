import webbrowser
import videos

class Movie(videos.Video):
    """ THIS IS TO STORE INFORMATION"""

    
    VALID_RATINGS=["G","PG","PG-13","R"]


    def __init__(self,title,duration,movie_storyline,poster_image,trailer_youtube):
        
        #initialize title from  Video class
        videos.Video.__init__(self,title,duration)
        self.duration= duration
        self.storyline= movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
