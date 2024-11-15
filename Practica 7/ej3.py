lista=[("Alex",22),("Jared",22),("Sergio",23),("Pedro",20)]

l=list(map(lambda t: (t[0],t[1]+1), lista))
print(l)