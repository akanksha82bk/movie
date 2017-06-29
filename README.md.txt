Movie Trailer Website
 
This is a server-side code written in Python scripting to store one's favourite movies imagery and a movie
trailer URL(from YouTube).It serves as viewing movie trailers.

Steps to open the website
1.Unzip the folder movies containing files.
2.Open folder named movies.
3.Open filename entertainment_centre with Python IDLE
4.Run file name entertainment_centre.py (Press F5)
5.Filename fresh_tomatoes.html gets opened up. 
or
Direct method:
1.Unzip the folder movies containing files.
2.Open folder named movies.
3.Run filename fresh_tomatoes.html to view the website.

Standard Python Libraries(STL):
webbrowser: import webbrowser
            webbrowser.open("youtube_link")
Opens up the youtube movie trailer.
where 'webbrowser' is a module and 'open' is a function to this module which pops
up a window of playing youtube movie trailer.


How to add Your Favourite Movie ?
>>Code is written in Python.
>>Open movies folder.
>>Open entertainment_centre.py with Python IDLE.
 
 school_of_rock=media.Movie("School of Rock",
                              "Rock Music",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=5afGGGsxvEA&t=55s")
>> school_of_rock is 'instance/object' here
>> movie_title=school of rock
>> movie_tagline=rock music
>> movie_image="https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg"
>> movie_url="https://www.youtube.com/watch?v=5afGGGsxvEA&t=55s"

Make changes to these four values provided above 
 
>>Create an instance of your own namely guardians_of_galaxy or bahubali.
example:
bahubali=media.Movie("","Romantic Tale","Image from the wikipedia .jpg format","youtube link of this movie trailer")

>>Then jump to the last step:
Pass your instance named "your_movie" to this list 
movies=[toy_story, avatar, zindagi_na_milegi_dobara,"your_movie"]
 Hit F5 to execute and here it is.


On that provocative note,enjoy your favourite list of movies on the website!!!
