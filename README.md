# Movie Picker! 

![GitHub repo size](https://img.shields.io/github/repo-size/peterkeres/movie-poster-tracker)
![GitHub last commit](https://img.shields.io/github/last-commit/peterkeres/movie-poster-tracker?color=red&style=flat-square)
![GitHub Development Status](https://img.shields.io/badge/Development_Status-Stopped-inactive)

For anyone who bought [this poster](https://www.amazon.com/Gift-Republic-GR630004-Bucket-Poster/dp/B075SDQ2K8) and would like a way to randomly pick a  movie, well your in the right place

![poster](movie_poster.png)

This poster was given to me as a present and quickly realized i wanted a way to randomly pick what movie to watch next. I also wanted a wait to rate the movies so when im done i can see what i liked and didn't. Thus, i came to python to solve my problem.

This app does the following functions based on the poster:

 - randomly pick a movie
 - keep track of ratings on each movie
 - see whats left/what you have watched.


## Installation
technologies/packages your going to need to run this

### Python v3.x
This is needed to... well.... run the code?

[Here](https://www.python.org/downloads/) if you hate the command line

or 
```bash
    $ sudo apt-get update
    $ sudo apt-get install python3.6
```

*Note this has not been tested on python v2.x so try at your own risk. but do feel free to leave a issue* :smirk: 

### Prettytable
Just a simple package that displays out the results from commands in a nice little table

[Here](https://pypi.org/project/prettytable/) if you hate the command line

or 
```bash
    $ pip install prettytable
```

*v2.0.0*

### Progress
Another small package that just shows a little loading animation while your pick is being retrieved

[Here](https://pypi.org/project/progress/) if you hate the command line

or 
```bash
    $ pip install progress
```

*v1.5*

## Usage
Generally speaking, there is 3 commands to the app and some initial setting values you have to set **BEFORE** you run the program

### Initial settings
this is only setting that you *need* to set. Its the names of the reviewers you want to keep track of the movie rating for.

```python
# Settings.py

    reviewers = ['person 1', 'person 2']
```
This setting needs to be set **BEFORE** running the app. If you happen to run it before adding in reviewers. Just simply delete the 'movie_database.csv' file, add in your reviewers, and run it again. 
*Note, adding in reviewers after movies have been reviewed is something not supported at this time.* :disappointed: *Open up an issue if this is a problem*

As to the max number of reviewers? well who knows. I tested up to 5 and it worked out just fine. just note that the display chart for looking at movie entries will start looking an little unwieldy. 

#### Other Settings
So there are some other settings you can change.
 - file path on the database file
 - charter used for star ratings
 - emoji used for watched value

```python
# Settings.py

    file_path = "movie_database.csv"

    rating_point = "*"
    rating_missing = "-"

    watched_emoji = "\u2705"
    unwatched_emoji = "\u274c"
```

*Note- changing the characters and emojis might throw off the table*

### Commands
Here is the list of commands you can use with this app to get things done. This app is a CLI app so commands are as you expected, if CLI confusing to you then check [this out](https://learn.co/lessons/intro-to-cli-applications)

#### **pick**
command that picks a random movie from the list that has not been watched yet.

```bash
    $ python3 MoviePicker.py pick
```

#### **list**
Command that will list movies depending on the optional flag appended.

``` bash
    $ python3 MoviePicker.py list -a
```
optional arguments are:
 - 'no argument'
   - this lists what movies are left to watch
 - -a,--all
   - displays all movies
 - -b,--best
   - displays movies watched from best to worst
 - -w,--worst
   - displays movies watched from worst to best
 - -s,--seen
   - displays moves you have watched so far

#### **watched**
command that sets a movie to a 'watched' status. aka knocking a movie off the list.

```bash
    $ python3 MoviePicker.py watched -m 12 angary men -r1 2 -r2 5
```

list of arguments:
- -m,--movie
  - the movie you watched
- -r#
  - the rating for that reviewer
  - *note, the amount of r tags will be the same amount as you set for reviewers in the settings file. so if you have 3 of them then you will have r1 # r2 # r3 #

### Other Arguments
Arguments that supersede the the above commands and arguments

#### Help Screen
Displays the help screen

-h,--help
``` bash
    $ python3 MoviePicker.py -h
```

#### Version number
Displays the version number

-v,--version 
``` bash
    $ python3 MoviePicker.py -v
```

## Contributing
Open an issue to talk about what on you want to change and then do your pull request.

## License
[MIT](https://choosealicense.com/licenses/mit/)


