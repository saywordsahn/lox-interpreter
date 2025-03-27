import enum


tokens = {
    '(': 'LEFT_PAREN',
    ')': 'RIGHT_PAREN'
}

with open("program.lox", "r") as file:
    content = file.read()

start = 0
end = len(content)

while start < end:
    print(tokens[content[start]])
    start += 1