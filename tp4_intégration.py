#!/usr/bin/python
#-*- coding: utf-8 -*-
from math import *
import numpy as np
import matplotlib.pyplot as plt




    # PARTIE 1, QUESTION A)
a=0.
b=2*pi
    
n=1000
t=np.linspace(a,b,n)
x=np.sin(t)
plt.plot(t,x,'r',label='sin(x)',linewidth=1.2)

plt.xlabel('Axes des x')
plt.ylabel('f(x)=sin(x)')
plt.title("Fonction sinus entre 0 et 2pi")
plt.legend()
plt.show()





    # PARTIE 1, QUESTIONS B, C ET D)

a=0
b=2*pi
n=100
h=(b-a)/float(n) # h le pas, n le nombre d'itérations
print('a, b, n, h =',a,b,n,h)

tt = np.zeros(n, dtype=float)
eax = np.zeros(n, dtype=float)
S = np.zeros(n, dtype=float)

def f(t):
    return cos(t)

def trapezes(f,a,b,n) :
    S[0]=sin(a)
    I=0
    tt[0]=a
    for i in range(1,n):
        S[i]=S[i-1]+(h/2)*(f(tt[i-1])+f(tt[i-1]+h)) # pour le tracé de la courbe d'intégration
        I=I+(h/2)*(f(tt[i-1])+f(tt[i-1]+h)) # I le calcul de l'intégration approchée
        tt[i]=tt[i-1]+h
        eax[i]=abs(S[i]-sin(tt[i])) # eax l'erreur absolue en fonction de x
   
    # Calcul de l'erreur sur intégration entre a et b :
    Se=sin(b)-sin(a) # Se la solution exacte
    if abs(Se)>0.1: # car on ne peut pas calculer l'ER si Se=0
        ER=abs((I-Se)*100/Se)
        print('I,Se,Erreur relative ER(%)=',I,Se,ER)
    else:
        EA=abs(I-Se)
        print('I,Se,Erreur absolue EA=',I,Se,EA)
   

trapezes(f,a,b,n)

t=np.linspace(a,b,1000)
plt.plot(tt,eax,'g',label='EA(x)')
plt.plot(tt,S,'bx',label='I(x)=int[a,b](cos(x))')
plt.plot(t,np.sin(t),'r',label='sin(x) exact',linewidth=1)

plt.xlabel('Axes des x')
plt.ylabel('Ordonnees')
plt.title("Comparaison entre I(x) et sin(x)")
plt.legend()
plt.show()

    
    
    
    
    
    
    
    # PARTIE 2 : CALCUL DE L'INTÉGRALE D'UNE FONCTION DONNÉE NUMÉRIQUEMENT

with open('donnees.dat','r') as f:
    line=f.readlines()
    n=int(line[0])
    x = np.zeros(n, dtype=float)
    f = np.zeros(n, dtype=float)  
    S = np.zeros(n, dtype=float)
    for i in range(0,n):
        linesplit=line[i+1].split()
        x[i]=float(linesplit[0])
        f[i]=float(linesplit[1])
        #print('i,x[i],f[i]=',i,x[i],f[i])
        
def trapezes(f,a,b,n) :
    S[0]=f[1]
    I=0
    for i in range(0,n):
        S[i]=S[i-1]+h*(f[i-1]) # pour le tracé de la courbe d'intégration
        I=I+h*f[i-1]
        #print('i,x[i],f[i],S[i],I=',i,x[i],f[i],S[i],I)
    print("L'integrale I=",I)


a=x[1]
b=x[n-1]
h=(b-a)/float(n)
trapezes(f,a,b,n)

plt.plot(x,S,'bx',label='I(x)=int[x0,xn](f(t)dt)')
plt.plot(x,f,'r',label='f(x)')
    
plt.xlabel('Axes des x')
plt.ylabel('Ordonnees')
plt.title("Integrale I(x) par la methode des trapezes")
plt.legend()
plt.show()
