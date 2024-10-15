def triangulo(w,c="*"):
    current_width=1
    #up=True
    while (current_width!=w):
        for i in range(current_width):
            print(c, end="")
        print("\n", end="")
        current_width+=1
        if (current_width==w):
            triangulo2(w,c)
            """up=False
        if(up):
            current_width+=1
        else:
            current_width-=1
            """
def triangulo2(w,c="*"):
    current_width=w-2
    while (current_width!=0):
        for i in range(current_width):
            print(c, end="")
        print("\n", end="")
        current_width-=1
triangulo(5)