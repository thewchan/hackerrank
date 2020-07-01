"""A newly opened multinational brand has decided to base their company logo on
the three most common characters in the company name. They are now trying out
various combinations of company names and logos based on this condition. 
Given a string S, which is the company name in lowercase letters, your task is
to find the top three most common characters in the string.

- Print the three most common characters along with their occurrence count.
- Sort in descending order of occurrence count.
- If the occurrence count is the same, sort the characters in alphabetical
  order.
- For example, according to the conditions described above,

GOOGLE would have it's logo with the letters G, O, E.

Input Format

A single line of input containing the string S.

Constraints

3 < len(S) <= 10**4

Output Format

Print the three most common characters along with their occurrence count each
on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde

Sample Output 0

b 3
a 2
c 2

Explanation 0

aabbbccde

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the
third line because a comes before c in the alphabet.

Note: The string S has at least 3 distinct characters.
"""
from collections import Counter


def flatten(lst):
    """Return flattened list."""
    return [item for sublist in lst for item in sublist]


if __name__ == '__main__':
    s = input()
    lst = list(s)
    counts = Counter(lst)

    # Sort counts
    sorted_counts = {letter: count for letter, count in \
                     sorted(counts.items(),
                            key=lambda letter_count_pair: letter_count_pair[1],
                            reverse=True)}

    # Accounting for ties
    unique_counts = sorted(list(set(sorted_counts.values())), reverse=True)
    break_ties = []

    # This loop builds a list of lists of grouped letters with the same counts.
    for unique_count in unique_counts:
        break_ties.append([])

        for letter, count in sorted_counts.items():

            if count == unique_count:
                break_ties[-1].append(letter)

    # Sort everything in the list of lists
    for unique_count_letters in break_ties:
        unique_count_letters.sort()

    # Flatten list of lists into just one list
    flatten_break_ties = flatten(break_ties)
    counter = 0

    for letter in flatten_break_ties:
        if counter == 3:
            break
        print(letter + ' ' + str(sorted_counts[letter]))
        counter += 1
