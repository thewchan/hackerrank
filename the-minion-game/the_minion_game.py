"""Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, s.
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

our task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string s.
Note: The string s will contain only uppercase letters: .

Constraints

0 < len(s) <= 10**6

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input

BANANA

Sample Output

Stuart 12

Note :
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
"""


def minion_game(string):
    """Implement the minion game."""
    s = string.lower()
    vow = 'aeiou'
    stuart_score = 0
    kevin_score = 0

    for index, character in enumerate(s):
        if character in vow:
            kevin_score += len(string) - index
        else:
            stuart_score += len(string) - index

    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    elif stuart_score < kevin_score:
        print(f'Kevin {kevin_score}')
    else:
        print('Draw')


if __name__ == '__main__':
