import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
fig=plt.figure()
camera=Camera(fig)
"""a=9
l=20
p=10"""
def beam_analysis(l,p):
    #a=9
    EI=200000*10**6*(0.5*0.5**3)/12
    #b=l-a
    #R1=p*b/l
    #R2=p*a/l
    x=np.linspace(0,l,100)
    for i in x:
        a=i
        b=l-a
        R1=p*b/l
        R2=p*a/l
        #shearforce
        v=np.linspace(0,0,100)
        v[x<a]=R1
        v[x>=a]=-R2
        #bending moment
        m=np.linspace(0,0,100)
        m[x<a]=R1*x[x<a]
        m[x>=a]=R2*(l-x[x>=a])
        #deflection
        d=np.linspace(0,0,100)
        d[x<a]=(p*b*x[x<a]/(6*l*EI))*(l**2-b**2-x[x<a]**2)
        d[x>=a]=(p*a*(l-x[x>=a]))/(6*l*EI)*(2*l*x[x>=a]-x[x>=a]**2-a**2)
        
        ax1=fig.add_subplot(311)
        plt.title("SHEAR FORCE")
        ax2=fig.add_subplot(312)
        plt.title("BENDING MOMENT")
        ax3=fig.add_subplot(313)
        plt.title("DEFLECTION")
        ax1.plot(x,v,color="red",linewidth=3)
        ax2.plot(x,m,color="green",linewidth=3)
        ax3.plot(x,-d,color="blue",linewidth=3)
        fig.tight_layout()
        camera.snap()
    animation=camera.animate()
    animation.save("beam_analysis.gif",writer='PillowWriter')
    plt.show()
    
beam_analysis(20,20)  

  




