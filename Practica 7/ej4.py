lista=[("Alex",22),("Jared",22),("Sergio",23),("Pedro",20),("Alberto",5)]

l=list(filter(lambda t: t[1]<=18, lista))
print(l)