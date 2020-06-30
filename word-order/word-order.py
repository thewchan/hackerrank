r"""Hacker rank word order challenge.

You are given n words. Some words may repeat. For each word, output its number
of occurrences. The output order should correspond with the input order of
appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

1 <= n <= 10**5

The sum of the lengths of all the words do not exceed 10**6
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, n.
The next n lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word
according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1

Explanation

There are 3 distinct words. Here, "bcdef" appears twice in the input at the
first and last positions. The other words appear once each. The order of the
first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the
output.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


SAMPLE_INPUT = '4\nbcdef\nabcdefg\nbcde\nbcdef\n'


def word_order():
    """Print word order as instructed"""

    raw_words = []
    num_words = input()

    for i in range(int(num_words)):
        raw_words.append(input())
    
    counts = Counter(raw_words)

    for k, v in counts.items():
        counts[k] = str(v)

    line_one = str(len(counts))
    line_two = ' '.join(counts.values())
    print(line_one + '\n' + line_two)

word_order()
