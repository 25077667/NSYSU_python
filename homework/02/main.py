#! /usr/bin/python3

print("B073040047")
x = "A quick brown fox jumps over the lazy dog."
print(sorted(list(set(x.lower()) - {' '} - {'.'}), reverse=True))
y = """print(sorted(list(set(x.lower()) - {' '} - {'.'}), reverse=True))"""
y += """!$#"""
