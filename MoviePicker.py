import argparse
import os.path
import Settings
import FileMaker

from Commands import Command


"""
Sets up and runs the IO of the program
"""
def grab_command():
    usage = '''   MoviePicker.py pick [-h] [--version] 
          MoviePicker.py list [-a | -b | -w | -s] [-h] [--version]
        '''

    usage += '  MoviePicker.py watched -m (movie) '
    for index, reviewer in enumerate(Settings.reviewers):
        usage += f'r{index+1} ( {reviewer.capitalize()} \'s rating) '

    """
    Sets up the Parser and some settings in the help menu
    """
    parser = argparse.ArgumentParser(
        prog='Movie Picker',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage=usage,
        description='''
        A program that helps you figure out what movies you feel like watching!
        
        The list of movies available to pick from are based from a bucket list poster, which can be found at:
        https://www.amazon.com/Gift-Republic-GR630004-Bucket-Poster/dp/B075SDQ2K8
        ''',
        epilog='Copyrights @Peter Keres',
    )

    """
    Sets up all the arguments and optional flags in the program
    """
    parser.add_argument('action',
                        type=str,
                        help='''
                        What action do you want the program to preform
                             Choices are:
                                pick [Which picks a random movie that has not been watched]
                                list [Display all movies based on option]
                                watched [sets a movie to a watched status and adds rating to the record]
                        ''',
                        metavar='Action',
                        choices=['pick', 'list', 'watched'], )

    parser.add_argument('-a',
                        '--all',
                        dest='all',
                        help="Optional: this is to see all movies for pick command",
                        action="store_true", )

    parser.add_argument('-b',
                        '--best',
                        dest='best',
                        help="Optional: this is to see the best movies for pick command",
                        action="store_true", )

    parser.add_argument('-w',
                        '--worst',
                        dest='worst',
                        help="Optional: this is to see the worst movies for pick command",
                        action="store_true", )

    parser.add_argument('-s',
                        '--seen',
                        dest='seen',
                        help="Optional: this is to see all movies watched so far for pick command",
                        action="store_true", )

    parser.add_argument('-m',
                        '--movie',
                        dest='movie',
                        nargs='*',
                        help="Optional: This is the title of the movie", )

    for index, reviewer in enumerate(Settings.reviewers):
        parser.add_argument('-r'+f'{index+1}',
                            '--'+reviewer.lower(),
                            type=int,
                            choices=[0, 1, 2, 3, 4, 5],
                            dest=reviewer.lower(),
                            help=f'Optional: {reviewer.capitalize()}\'s ranking of the movie', )

    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s 1.0')

    """Adds al the arguments and optional arguments to the parser object and sends the user action request to the 
    command file """
    arg = parser.parse_args()
    Command(arg)


"""
Checks to see if the database file has be created yet
"""
def file_check():
    if not os.path.exists(Settings.file_path):
        FileMaker.create_database()


"""
Creates the database file based on fields in the settings file
"""
if __name__ == '__main__':
    file_check()
    grab_command()
