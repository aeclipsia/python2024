"""def sec(s,h=0,m=0):
    if h==0 and m==0:
        hora = s//3600
        mins = (s%3600)//60
        seg = (s%3600)%60
        #return (str(hora) +" horas, "+ str(mins) +" minutos,"+ str(seg)+" segundos")
        return ("%02d:%02d:%02d"%(hora,mins,seg)) #formato hh:mm:ss
    else:
        return (h*3600) + (m*60) + s
"""

def sec(s, **kwargs):
    if len(kwargs)!=2 & len(kwargs)!=0:
        return "error"
    elif len(kwargs)==0:
        hora = s//3600
        mins = (s%3600)//60
        seg = (s%3600)%60
        #return (str(hora) +" horas, "+ str(mins) +" minutos,"+ str(seg)+" segundos")
        return ("%02d:%02d:%02d"%(hora,mins,seg)) #formato hh:mm:ss
    else:
        h=kwargs.get('h', 0)
        m=kwargs.get('m',0)
        return (h*3600) + (m*60) + s
    
    
print(sec(3661))
print(sec(1,m=1,h=1))
print(sec(1,m=1))