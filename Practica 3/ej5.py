def sec(h,m,s):
    return (h*3600) + (m*60) + s

def reloj(s):
    h = s//3600
    m = (s%3600)//60
    seg = (s%3600)%60
    return (str(h) +" horas, "+ str(m) +" minutos,"+ str(seg)+" segundos")

print(sec(1,1,1))
print(reloj(3661))