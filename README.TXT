Project: Movie Trailer Website  - Marcus Willemsen
================================

Required Libraries and Dependencies
-----------------------------------
Requires Python 2.7.x to be installed

Depends on the following versions of the Bootstrap framework and jquery
https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css
https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css
http://code.jquery.com/jquery-1.10.1.min.js
https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js
Internet Browser installed (Chrome, Safari, Firefox, or IE > IE 9.x) with javascript enabled
Working internet Connection, otherwise Bootstrap and the Movie Resources won't load
The project contains the following files and directories:

MovieTrailerWebsites
|
|--img
|   |-budapest.jpg
|   |-captain_future.jpg
|   |-day_of_the_tentacle.jpeg
|   |-down_by_law.jpg
|   |-dragonage.jpeg
|   |-firefly.jpg
|   |-indy_atlantis.jpeg
|   |-inquisition.jpg
|   |-lego_starwars.jpeg
|   |-life_on_mars.jpg
|   |-masseffect.jpeg
|   |-mystery_train.jpg
|   |-night_on_earth.jpg
|   |-oh_brother_where_art_thou.jpg
|   |-sopranos.jpg
|   |-tatortreiniger.jpg
|   |-the_godfather.jpg
|   |-the_wire.jpg
|   |-wild_at_heart.jpg
|   |-witcher3.jpeg
|
|-entertainment_center.py
|-fresh_tomatoes.py
|-media.py
|-README.TXT


How to Run Project
------------------
- Unzip MovieTrailerWebsite into a directory using your favorite unzipper e.g. on the commandline use "unzip MovieTrailerWebsite.zip"
- Open a console and navigate to the Projects Root Directory 'MovieTrailerWebsite'
- Type 'python entertainment_center.py' at the prompt
- Your systems default webbrowser opens and display the page
- By clicking on the tabs you can change from movies to tv-shows and games


Extra Credit Description
------------------------
- Added a General Class DigitalAsset to media.py from which classes Movie, TvShow and Game inherit
- Added additional attributes to Movie, TvShow and Game to
- Added method Movie.get_cast() to get a formatted list of Movie Actors
- Added method Game.get_platform() to get formatted list of available Game Platforms
- Added Tabs to webfrontend to present movie tiles and tv-show tiles and game tiles on the same page on two different Tabs
- Added some additional CSS to properly display the additional information on tiles and to enable tabs


Miscellaneous
-------------
Contrary to the PEP8 Python Styleguide I have added a 'coding=utf-8' at the beginning of every python file. It was
the only way to display the german umlaut characters

All movie and tv show plot summaries are taken from imdb unless otherwise stated
All game descriptions are quoted from wikipedia
