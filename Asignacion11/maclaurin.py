import math

def seno(entrada,num):
    v = 0.0
    for i in range(1,num,4):
            v += (entrada*math.pi/180)**i/math.factorial(i)
    for i in range(3,num,4):
            v += -1*(entrada*math.pi/180)**i/math.factorial(i)        
    return v

def exp(entrada,num):  
    v = 0.0
    for i in range(num):
            v += float(entrada**i)/math.factorial(i)
    return v      

def tabularFuncion(f,entrada,a,b,incr):
    
    if f == 'S' or f == 's':
        for i in range(a,b,incr):
            print(seno(entrada,i))
        
    if f == 'E' or f == 'e': 
        for i in range(a,b,incr):
            print(exp(entrada,i))
               
    return -1