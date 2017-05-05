import webbrowser
import videos

class TvShow(videos.Video):
    


    def __init__(self,title,duration,season,tv_station,episode_url):
        
        videos.Video.__init__(self,title,duration)
        self.season= season
        self.tv_station=tv_station
        self.episode_url=episode_url

    def get_local_listing(self):
        webbrowser.open(self.episode_url)
        
