import fresh_tomatoes
import media
toy_story = media.Movie("Toy Story", "Toys come to life", "https://" +
                        "upload.wikimedia.org/wikipedia/en/thumb/1/" +
                        "13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b" +
                     "/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
znmd = media.Movie("Zindagi Na Milegi Dobara", "Live Life" +
                   "each moment spreading smiles all over",
                   "https://upload.wikimedia.org/wikiped" +
                   "ia/en/3/3d/Zindaginamilegidobara.jpg",
                   "https://www.youtube.com/watch?v=FJrpcD" +
                   "gC3zU")
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia" +
                          "/en/5/50/RatatouillePoster.jpg", 
                          "https://www.youtube.com/watch?v=niD-ja" +
                          "hFURU")
midnight_in_paris = media.Movie("Midnight In Paris", "Going back in the" +
                                "time to meet authors",
                                "https://upload.wikimedia.org/wikipedia" +
                                "/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8o" +
                                "mt-CY")
hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia" +
                           "/en/9/9d/Mockingjay_Part_2_Poster.jpg",
                           "https://www.youtube.com/watch?v=n-7K_OjsDCQ")
school_of_rock = media.Movie("School of Rock", "An amateur rock " +
                             "enthusiast,slyly takes his friends" +
                             "substitute teachers job.Bearing no" + 
                             "qualifications for it, starts a ba" +
                             "nd instead.", "https://upload.wiki" +
                             "media.org/wikipedia/en/1/11/School" +
                             "_of_Rock_Poster.jpg", "https://www" +
                             ".youtube.com/watch?v=5afGGGsxvEA&t" +
                             "=55s")
logan = media.Movie("Logan", "American SuperHero Film Marvel Ani.", 
                    "https://upload.wikimedia.org/wikipedia/en/3" +
                    "/37/Logan_2017_poster.jpg", 
                    "https://www.youtube.com/watch?v=ny3hScFgCIQ")
return_of_xander_cage = media.Movie("Return of Xander Cage",
                                    "Story of Xander Cage conspiracy mistake", 
                                    "https://upload.wikimedia.org/wikipedia" +
                                    "/en/9/9c/Xxx_return_of_xander_cage_fil" +
                                    "m_poster.jpeg", 
                                    "https://www.youtube.com/watch?v=xEuM4I" +
                                    "UFWu8&t=4s")
movies = [toy_story, avatar, znmd, ratatouille, midnight_in_paris,
          hunger_games, school_of_rock, logan, return_of_xander_cage]
fresh_tomatoes.open_movies_page(movies)
