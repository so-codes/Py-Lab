# Regular Expressions

import re
# make a code explaining regex
regex = '''
    .       - Any Character Except New Line
    \d      - Digit (0-9)
    \D      - Not a Digit (0-9)
    \w      - Word Character (a-z, A-Z, 0-9, _)
    \W      - Not a Word Character
    \s      - Whitespace (space, tab, newline)
    \S      - Not Whitespace (space, tab, newline)
    
    \b      - Word Boundary
    \B      - Not a Word Boundary
    ^       - Beginning of a String
    $       - End of a String
    
    []      - Matches Characters in brackets
    [^ ]    - Matches Characters NOT in brackets
    |       - Either Or
    ( )     - Group
    
    Quantifiers:
    *       - 0 or More
    +       - 1 or More
    ?       - 0 or One
    {3}     - Exact Number
    {3,4}   - Range of Numbers (Minimum, Maximum)
    
    Sample Regexs:
    [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
    https?://(www\.)?\w+\.\w+
    
    re.compile() - Compile Regex Pattern
    re.search() - Search the Text for the First Match
    re.findall() - Return a List of All Matches
    re.sub() - Substitute Strings or Replace Matches
    
    Flags:
    re.IGNORECASE - Ignores Case
    re.DOTALL - Makes . Match New Lines
    re.MULTILINE - Makes ^ and $ Match the Beginning and End of Each Line
    re.VERBOSE - Ignores Whitespace and Comments
    
    re.compile() - Compile Regex Pattern
    re.search() - Search the Text for the First Match
    re.findall() - Return a List of All Matches
    re.sub() - Substitute Strings or Replace Matches
'''

# make a string to search
text = '''
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1234567890
'''
# make a pattern to search for
pattern = re.compile(r'[a-zA-Z0-9]+')
# make a variable to store the matches
matches = pattern.finditer(text)
# loop through the matches
for match in matches:
    # print the match
    print(match)