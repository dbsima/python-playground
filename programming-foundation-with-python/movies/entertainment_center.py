import media, fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his boys that comes to live",
                       "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

print media.Movie.__name__
print media.Movie.__module__