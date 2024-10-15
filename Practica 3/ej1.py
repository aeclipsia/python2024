def rectangulo(l,w,c="*"):
    for i in range(w):
        for j in range(l):
            print(c, end="")
        print("\n", end="")
            
rectangulo(10,5,"x")