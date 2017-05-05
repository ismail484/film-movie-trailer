# film-movie-trailer
Project: Movie Trailer Website  - [Mohamed Ismail]
================================

Description
-----------------------------------

'''it's object oriented started with file videos with a parent class Video , then inherited to class  Movie () in a media file and TvShow() in a tv file
''' A new file media.py with class Movie() is created with a constructor init with instance variables or attributes such as poster_image, youtube_url, title, storyline, ratings, review etc..

An instance of every movie is created in another file entertainment_center.py where show.Movie class is invoked with unique object and the parameter values are passed '''

''' init constructor, when ever an instance of the class movie is created, all the variables are initialized their values accordingly to the arguments passed.Create instance methods/functions like show trailer, read review, comment review etc.. In zoom.py, instances are created with respect to	the class movie(). For example, to every movie that should be	listed on the web page(website.py) an instance is created and arguments are passed so that the values are initialized.

All the instances created are added to a list (movies) and movies list is passed as argument into the method (open_movies_page). website.py is a html file, with css and script tags to perfectly manage the outlook of the page. For every instance(Movie object) created are displayed in the webpage by website.py file with invoking open_movies_page(movies list) '''

Required Libraries and Dependencies
-----------------------------------

it just needs pyton 2.7v or higher to run the application 
[In this section list your project’s dependencies. A basic Movie Website Trailer project requires Python v2.* to be installed]


How to Run Project
------------------
just donload the zip project and run entertainment_center.py using command (python entertainment_center.py)
[In this section, explicitly describe the steps necessary to run your project from Github repo to the program execution. Make sure you try out these steps to verify that you didn’t overlook anything.]


Extra Credit Description
------------------------
the following features are implemented:
1-OOP data structure with different objects and methods
2- HTML file and CSS tags &Bootstrap files .

[If your project includes any features that exceed specifications, (such as including addition information about the movies or personalizing the website with additional HTML/CSS) or if your project deviates from the description in some other interesting way, describe that here.]


Miscellaneous
-------------
just README.md file and run the program
[If there is any additional information you’d like to include, feel free to add additional sections to the README.]
