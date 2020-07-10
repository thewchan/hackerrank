"""Balanced parentheses.

A bracket is considered to be any one of the following characters: (, ), {, },
[, or ].

Two brackets are considered to be a matched pair if the an opening bracket
(i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or })
of the exact same type. There are three types of matched pairs of brackets: [],
{}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses
are not matched. For example, {[(])} is not balanced because the contents in
between { and } are not balanced. The pair of square brackets encloses a
single, unbalanced opening bracket, (, and the pair of parentheses encloses a
single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following
conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of
brackets is also a matched pair of brackets.

Given N strings of brackets, determine whether each sequence of brackets is
balanced. If a string is balanced, return YES. Otherwise, return NO.

Function Description

Complete the function is_balanced() in the editor below. It must return a
string:
YES if the sequence is balanced or NO if it is not.

is_balanced() has the following parameter(s):

s: a string of brackets

Input Format

The first line contains a single integer , the number of strings.
Each of the next  lines contains a single string , a sequence of brackets.

Constraints

1 <= N <= 10**3
1 <= |s| <= 10**3, where |s| is the length of the sequence.
All characters in the sequences ∈ { {, }, (, ), [, ] }.

Output Format

For each string, return YES or NO.

Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}
Sample Output

YES
NO
YES

Explanation

The string {[()]} meets both criteria for being a balanced string, so we print
YES on a new line.
The string {[(])} is not balanced because the brackets enclosed by the matched
pair { and } are not balanced: [(]).
The string {{[[(())]]}} meets both criteria for being a balanced string, so we
print YES on a new line.
"""
# Global variable
BRACKETS = {'(': ')',
            '[': ']',
            '{': '}',
            }


def is_balanced(s):
    """Check to see if string is balanced using a stack."""
    stack = []

    for char in s:
        if char in BRACKETS.keys():
            stack.append(char)

        else:
            if (len(stack) == 0) or (char != BRACKETS[stack.pop()]):
                return 'NO'

    if len(stack) > 0:
        return 'NO'

    return 'YES'


def main():
    """Read data and run balance checks."""
    N = int(input())
    for i in range(N):
        s = input()
        result = is_balanced(s)
        print(result)


if __name__ == '__main__':
    main()
