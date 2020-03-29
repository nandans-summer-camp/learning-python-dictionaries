#
# INSTRUCTIONS:
# For this exercise we will work with a
# "scoreboard" for an imaginary game.
# You will be required to write functions
# that operate on the "scoreboard" data
# structure and compute certain results.



######################################
# TUPLES
#
# For these functions, the "scoreboard"
# will be a list of tuples, where each
# tuple is of the form (str, int)
# representing (player_name, score)
#
# For example:
# [('kewld00d1', 100), ('pumpkin', 550)]
######################################


#
# 1)
# Create a function "get_scores"
# that has one parameter, the scoreboard,
# and returns a list of the same size
# with just the scores for each player
# (a list of ints)

def get_scores(scoreboard):
    return [s for p, s in scoreboard]


#
# 2)
# Create a function "top_score"
# that has one parameter, the scoreboard,
# and returns an int, the highest score
# on the scoreboard

def top_score(scoreboard):
    score = 0
    for _, s in scoreboard:
        if s > score:
            score = s
    return score


#
# 3)
# Create a function "top_player"
# that has one parameter, the scoreboard,
# and returns the player_name that has
# the highest score

def top_player(scoreboard):
    teacher, score = scoreboard[0]
    for t, s in scoreboard:
        if s > score:
            teacher, score = t, s
    return teacher


######################################
# DICTIONARIES
#
# For these functions, the "scoreboard"
# will be a list of dictionaries, where each
# dictionary represents information
# about a single player.
#
# The keys of the dictionary are:
# "player", "score", "country", "levels"
#
# For example, one dictionary:
#
# {
#    'player': 'tr0llhuntah',
#    'score': 200,
#    'country': 'no',
#    'levels': ['Choco Mountain', 'Rainbow Road']
# }
#
######################################


#
# 4)
# Create a function "top_player_from_dict"
# that has one parameter, the scoreboard,
# and returns the player_name that has
# the highest score

def top_player_from_dict(scoreboard):
    teacher = scoreboard[0]['player']
    score = scoreboard[0]['score']

    for s in scoreboard:
        if s['score'] > score:
            teacher, score = s['player'], s['score']
    return teacher

#
# 5)
# Create a function "get_good_players"
# that has two parameters:
# 1. scoreboard
# 2. an int (limit)
#
# "get_good_players" returns a list of
# strings, with the names of the players
# who have a score greater than or equal to
# limit.

def get_good_players(scoreboard, lim):
    return [s['player'] for s in scoreboard if s['score'] >= lim]


#
# 6)
# Create a function "top_player_by_country"
# that has two parameters:
# 1. scoreboard
# 2. a string (country)
#
# "top_player_by_country" returns a string
# with the name of the player with the highest
# score in the provided country.

def _country_matches(a, b):
    if b is None:
        return True
    return a == b

def top_player_by_country(scoreboard, country):
    scoreboard = [s for s in scoreboard
                  if _country_matches(s['country'], country)]
    return top_player_from_dict(scoreboard)


#
# 7)
# Create a function "most_levels_played"
# that has one parameter: "scoreboard".
# and returns a tuple (str, int) with the name of
# the player that has played the most levels
# and the number of levels they played

def most_levels_played(scoreboard):
    scoreboard = [(s['player'], len(s['levels'])) for s in scoreboard]
    player, score = '', 0
    for p, s in scoreboard:
        if s > score:
            player, score = p, s
    return player, score

#
# 8)
# Create a function "played_levels"
# that has one parameter: "scoreboard".
# and returns a list of strings with the
# names of all the levels that have been
# played by any user.
#
# The list of levels can have duplicates.

def played_levels(scoreboard):
    levels = []
    for s in scoreboard:
        levels += s['levels']
    return levels


######################################
# BONUS QUESTIONS
######################################

#
# 9)
# Create a function "distinct" that
# takes a list of elements and returns
# a list of only the unique elements.
#
# Example:
# [1,2,2,2,1,3] -> [1,2,3]
#
# NOTE: Use only the tools we have learned
# so far:
# dictionaries, lists, for loop, try/except

def distinct(elements):
    uniq = []
    d = {}
    for el in elements:
        try:
            d[el]
        except KeyError:
            uniq += [el]
            d[el] = True
    return uniq

#
# 10)
# Create a function "distinct_played_levels"
# That is just like "played_levels" except
# that it returns a list of the unique
# levels played (a list without duplicates)
#
# HINT: just use the two functions you've
# already written!

def distinct_played_levels(scoreboard):
    return distinct(played_levels(scoreboard))

#
# 11)
# Modify your function "top_player_by_country":
#
# Now, the second parameter ("country") should
# be either the country code OR None. If it
# is None, the function should return the top
# player across all countries



# 12)
# Create a function called "country_leaderboard"
#
# This function will return a "leaderboard" that
# provides information about the top player
# per country.
#
# The "leaderboard" should be a dictionary.
# See the test_exercises.py file for the format.

def country_leaderboard(scoreboard):
    leaderboard = {}

    for s in scoreboard:
        c, p, s = s['country'], s['player'], s['score']
        try:
            curr_score = leaderboard[c]['score']
        except KeyError:
            curr_score = None
        if not curr_score or s > curr_score:
            leaderboard[c] = {'player': p, 'score': s}

    return leaderboard
