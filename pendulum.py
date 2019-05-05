def main():
    from math import sin
    import numpy as np
    import matplotlib.pyplot as plt
    N=1000
    h=0.01
    y0=1
    v0=np.array([1,1.2,1.752555,1.7527,1.8])
    t=np.linspace(0,h*N,N)
    for i in range(0,len(v0)):
        y=prop(y0,v0[i],df,h,N)
        plt.plot(t,y)
    plt.show()

def df(x):
    from math import sin
    return -sin(x)

def step(y0,y1,dy,h):
    return (h**2)*dy(y0)+2*y1-y0

def prop(y0,v0,dy,h,N):
    import numpy as np
    y1=v0*h+y0
    y=np.array([y0,y1])
    for i in range(2,N):
        y=np.append(y,step(y[i-2],y[i-1],dy,h))
    return y

if __name__ == "__main__":
  main()