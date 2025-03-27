import enum


tokens = {
    '(': 'LEFT_PAREN',
    ')': 'RIGHT_PAREN',
    '{': 'LEFT_BRACE',
    '}': 'RIGHT_BRACE',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'STAR',
    '.': 'DOT',
    ',': 'COMMA'
}

with open("program.lox", "r") as file:
    content = file.read()
    print(content)

start = 0
end = len(content)

while start < end:
    print(tokens[content[start]])
    start += 1