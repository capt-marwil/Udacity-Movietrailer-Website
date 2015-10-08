__author__ = 'marwil'
import media
import fresh_tomatoes
wild_at_heart = media.Movie("Wild at Heart",  "An impossible Love", 1, "The story of Lula and Sailor", "img/wild_at_heart.jpg", "https://www.youtube.com/watch?v=QCQwumNQL9E", "David Lynch", "Nicolas Cage, Laura Dern")


down_by_law = media.Movie("Down by Law",  "The convicts try to escape from prison", 2, "I Scream, you scream, we all scream for icecream", "img/down_by_law.jpg", "www.youtube.com/watch?v=1H9zlFH7UhA", "Jim Jarmusch", "Roberto Benigni, John Lurie, Tom Waits")

night_on_earth = media.Movie("Night on Earth", "A collection of five stories involving cab drivers in five different cities.", 15, "Helmet,that\'s not a name", "img/night_on_earth.jpg", "https://www.youtube.com/watch?v=F1m6GlPyOSU", "Jim Jarmush", "Roberto Bengini, Armin Müller-Stahl, Joe Strummer")


#the_witcher = media.Game("The Witcher", "The world doesn't need a hero, it needs a professional!", 5, 'XBOX One')

#print(the_witcher.title)
#print(the_witcher.synopsis)
#print(the_witcher.rating)
#print(the_witcher.platform)

movies = []
movies.append(wild_at_heart)
movies.append(down_by_law)
movies.append(night_on_earth)

# Create an new html page and open it in the systems standard browser by calling open_movies in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)