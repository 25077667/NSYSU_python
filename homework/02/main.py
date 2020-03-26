#B073040047
z = charactersUsed = 'print({*z})'
exec(charactersUsed)
# {'n', '*', 'i', 'r', 'z', '}', '(', ')', 't', '{', 'p'}

x = "hello"
d = {}
z="d[[*x*5][5]] = d"
exec(z); print(d)
# {'h': {...}}
exec(charactersUsed)
# {'d', '*', ']', '[', '5', 'x', '='}

z = "d['h'] is d"
exec("print("+z+")")
# True
print(eval(z))
# True
exec(charactersUsed)
# {'d', ']', 'h', '[', 'i', 's', ' ', "'"}
