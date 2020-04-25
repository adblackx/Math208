import numpy as np

def Stepteun(t, x, h ,f):
    return x + h*f(t,x)

def StepEuler(t, x, h, f):
    """𝑡+ℎ:𝑆𝑡𝑒𝑝𝐸𝑢𝑙𝑒𝑟(𝑡,𝑥,ℎ,𝑓)=𝑥+ℎ𝑓(𝑡,𝑥)."""
    #oui bien
    return x + h*0.5*(f(t,x) + f(t+1, Stepteun(t,x,h,f))

def MyEuler(t0,x0, T, N, f):
    """Fonction """
    h = T/N
    #print(h)
    time = np.empty(N+1)
    x = np.empty(N+1)
    x[0] = x0
    time[0] = t0
    for n in np.arange(N):
        time[n+1] = t0 + (n+1)*h
        x[n+1] = StepEuler(time[n],x[n],h,f)
    return time , x
