"""Day 2 notes."""


def stuff(*args, **kwargs):
    """Any list of things."""
    print(args)
    print(kwargs)


stuff(*[1, 2, 3, 4, ])  # add a * when unpacking a list --same with kwargs use **[1, 2,]


def recurse_ex():
    """Would get a max call stack."""
    recurse_ex()


def factorial(x):
    """Calculate the factorial of x recursively."""
    total = 1
    if x < 0:
        raise ValueError("Ener a number greater than 0.")
    while x > 0:
        total *= x
        x -= 1
        print x
        print total
    return total


letters = ['a', 'b', 'c']


for idx, item in enumerate(letters):
    print(letters[idx])


[num for num in range(1, 101)]
# makes a list of numbers 1-100


range(0, 101, 10)
# counts by ten to 100


if __name__ == "__main__":
    # if script is run from the command line do stuff or not
    print()

# create an '__init__.py' for importing modules
# from importlib import reload
# !/usr/bin/env python put line in top of module


"""journal:
    Week 1 day 2:
    I learned a lot about booleans,
    how to ping pong pair program,
    how to run certain things if from the command line,
    test driven pythoning,
    how to set up environments,
    *args and **kwargs,
    I could keep going...
"""


def HQ9(code):
    code = input('Awaiting your response: ')
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9' or code == 9:
        song = beer_song()
        return song


def beer_song():
    lyr_a, lyr_b, lyr_c, lyr_d, lyr_e, lyr_f, lyr_g = (
        'bottles of beer on the wall, ',
        'bottles of beer.\n',
        'Take one down and pass it around, ',
        'bottles of beer on the wall.\n',
        'Take one down and pass it around, 1 bottle of beer on the wall.\n',
        '1 bottle of beer on the wall, 1 bottle of beer.\n',
        'Take one down and pass it around, no more bottles of beer on the wall.')
    bottles = int(input('How many bottles of beer? '))
    song = ''
    for i in range(bottles, 0, -1):
        lyrics_1 = '{0} {1}{0} {2}'.format(bottles, lyr_a, lyr_b)
        song += lyrics_1
        bottles -= 1
        if bottles == 1:
            song += lyr_e + lyr_f + lyr_g
            break
        lyrics_2 = '{1}{0} {2}'.format(bottles, lyr_c, lyr_d)
        song += lyrics_2
    print(song)
    return song
