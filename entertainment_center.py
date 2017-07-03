import media
import fresh_tomatoes

# Creating instances of the class Movie to store our movie data.

star_wars_the_last_jedi = media.Movie("Star Wars: The Last Jedi",
                                      "Rey continues her epic journey with Finn, Poe and Luke Skywalker in the next chapter of the saga.",
                                      "https://images-na.ssl-images-amazon.com/images/M/MV5BOTE5NzYyNjM0Ml5BMl5BanBnXkFtZTgwNjk4MDIwMjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                      "https://www.youtube.com/watch?v=zB4I68XVPzQ")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                      "https://www.youtube.com/watch?v=d96cjJhvlMA")

freedom_writers = media.Movie("Freedom Writers",
                              "A teacher in a racially divided school who gives her students what they've always needed - a voice",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTIxMzExNTgxMV5BMl5BanBnXkFtZTcwNDUxODM0MQ@@._V1_.jpg",
                              "https://www.youtube.com/watch?v=JhXMJlm852A")

mean_girls = media.Movie("Mean Girls",
                         "Story about a girl who try to make it in the popular clique at her new school.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE1MDQ4MjI1OV5BMl5BanBnXkFtZTcwNzcwODAzMw@@._V1_UY268_CR3,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=KAOmTMCtGkI")

the_heat = media.Movie("The Heat",
                       "An uptight FBI Special Agent is paired with a foul-mouthed Boston cop to take down a ruthless drug lord.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA2MDQ2ODM3MV5BMl5BanBnXkFtZTcwNDUzMTQ3OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=c-KKx0lcn2A")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                       "https://www.youtube.com/watch?v=6hB3S9bIaco")

movies = [star_wars_the_last_jedi, guardians_of_the_galaxy, freedom_writers, mean_girls, the_heat, the_shawshank_redemption]

fresh_tomatoes.open_movies_page(movies)
