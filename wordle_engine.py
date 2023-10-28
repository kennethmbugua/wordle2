
#######################################################
# wordle_engine
#
# Name: zzNAMEzz (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################


# Container for color control codes.
import re
class wordle_colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


wordle_alphabet = "abcdefghijklmnopqrstuvwxyz"


def welcome_string():
    return f"Welcome to {wordle_colors.GREEN}W{wordle_colors.RED}o{wordle_colors.BLUE}r{wordle_colors.YELLOW}d{wordle_colors.CYAN}l{wordle_colors.MAGENTA}e{wordle_colors.ENDC}"


def create_letter_status():
    """ Return a new dictionary that maps each letter to
        wordle_colors.BLUE """
    ls = list(wordle_alphabet)
    new_dict = {}
    for item in ls:
        new_dict[item] = wordle_colors.BLUE

    return new_dict
    #


def load_words(filename: str):
    """ Load the words from the specified file and place them
        in a set.
        Ignore any lines that begin with "#"
        """
    f=open(filename)
    file_read=f.read().splitlines()
    file_set=set()
    for item in file_read:
        if '#' in item:
            continue
        else:
            item.strip().split('\n')
            file_set.add(item)


    return file_set



def format_guess(target, guess):
    """ Return a string that contains the user's guess formatted
        so that each letter is colored
        * GREEN:  The letter is placed correctly.
        * YELLOW: The letter appears in the target word,
                  but in a different location.
        * RED:    The letter does not appear in the target word
        Also, the string should end with wordle_colors.ENDC """
    print(target)
    guess_list=list(guess)
    target_list=list(target)
    target_dict={}
    for x,y in enumerate(target_list):
        target_dict[y]=x

    dict_n=""
    for i in range(5):
        a=guess_list[i]
        if guess_list[i] == target_list[i]:
            a = f"{wordle_colors.GREEN}{guess_list[i]}"
            dict_n = dict_n + a
        elif guess_list[i] in target_dict.keys() and guess_list.index(a)!=target_dict[a]:
            a = f"{wordle_colors.YELLOW}{guess_list[i]}"
            dict_n = dict_n + a
        else:
            a = f"{wordle_colors.RED}{guess_list[i]}"
            dict_n = dict_n + a


    dict_n=dict_n+wordle_colors.ENDC
    return dict_n
def update_letter_status(letter_status, target, guess):

    """ Update the letter status dictionary to show which letters
        have been used and whether they appear in the target word.
        Specifically:
        * BLUE:   Letter has not been used in a guess
        * GREEN:  Letter appears in the correct location in some guess.
        * YELLOW: Letter is in the target word and appears in some guess
                  (but not in the correct location)
        * RED:    Letter does  not appear in the target word, but has
                  been used in at least one guess."""
    guess_list = list(guess)
    target_list = list(target)
    target_dict = {}
    for x, y in enumerate(target_list):
        target_dict[y] = x

    for i in range(5):
        a=guess_list[i]
        if a in target_dict.keys():
            if guess_list.index(a) == target_dict[a]:
                letter_status.update({a: wordle_colors.GREEN})

            else:
                letter_status.update({a: wordle_colors.YELLOW})

        else:
            letter_status.update({a: wordle_colors.RED})

    return letter_status

    #


def format_letters(alphabet_dict):
    """ Generate a string that lists all the letters of the alphabet
        colored according to the rules given in update_letter_status.
        the string should end with wordle_colors.ENDC """
    stri=""
    format_let=alphabet_dict
    for x, y in format_let.items():
        stri=stri+y+x

    return stri+wordle_colors.ENDC
def initial_alphabet():
    initial_alpha=""
    b=create_letter_status()
    for x, y in b.items():
        initial_alpha=initial_alpha+y+x
    return initial_alpha

    #
