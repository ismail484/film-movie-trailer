import webbrowser
import videos

class TvShow(Video):
    


    def __init__(self,title,season,episode,tv_station):
        
       Video.__init__(self,title)
        self.season= season
        self.episode=episode
        self.tv_station=tv_station

    def get_local_listing(self):
        webbrowser.open(self.trailer_youtube_url)
        
