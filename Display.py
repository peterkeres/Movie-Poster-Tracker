from prettytable import PrettyTable
from progress.spinner import PixelSpinner
import time
import Settings

"""
Display Class:
    Handles all output for the program
"""


class Display:
    """
    Displays the output of a movie pick
    """

    def display_pick(pick):
        # Note: this does noting really, commit out if you dont want wait for the loading bar
        spinner = PixelSpinner('Finding a movie! ')
        for i in range(10):
            time.sleep(.3)
            spinner.next()

        print(f'\nGet ready to watch! {pick[1]}')

    """
    Displays a table output for whatever action is entered
    """

    def display_table(movie_list):
        table = PrettyTable()
        table.field_names = Settings.column_names + Settings.reviewers

        for movie in movie_list:
            watched = ""
            rating = ""
            row = [movie[0], movie[1], movie[2]]

            # filles the watched column
            if movie[3] == Settings.watched_symbol:
                watched = Settings.watched_emoji
            else:
                watched = Settings.unwatched_emoji

            row.append(watched)

            # fills out each revier's column
            for reviewer in range(4, len(movie)):
                if reviewer == Settings.unwatched_symbol:
                    pass
                else:
                    for index in range(0, int(movie[reviewer])):
                        rating += Settings.rating_point + " "
                    for index in range(0, (5 - int(movie[reviewer]))):
                        rating += Settings.rating_missing + " "

                row.append(rating)
                rating = ""

            table.add_row(row)

        print(table)
