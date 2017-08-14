#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Carga de los mÃ³dulos necesarios
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

#estas debeŕían ser las variables
vx = [0.1,0.17,0.27,0.35,0.39,0.42,0.43,0.44]   
vy = [10,20,30,40,50,60,70,80]

#invento

vn=len(vx)
vx=np.array(vx)
vy=np.array(vy)
vsumax=float(sum(vx))
vsumay=float(sum(vy))
vmayorX=max(vx)
vmayorY=max(vy)
#Metodo regresion Lineal simple
vsumaxx=float(sum(vx*vx))
vsumayy=float(sum(vy*vy))
vsumaxy=float(sum(vx*vy))
print vsumaxx
vpromx=float(vsumax/vn)
vpromy=float(vsumay/vn)

vm=(vsumax*vsumay - vn*vsumaxy) / (vsumax**2 - vn*vsumaxx)
vb=vpromy - vm*vpromx

#para determinar la correlacion par la  lineal
vsigmax=np.sqrt(vsumaxx/vn - vpromx**2)
vsigmay=np.sqrt(vsumayy/vn - vpromy**2)
vsigmaxy= vsumaxy/vn -vpromx*vpromy
vcoefienteLineal=(vsigmaxy/(vsigmax*vsigmay))

#METODO DE REGRESION NO LINEAL EXPONENCIAL
vlny=float(sum(np.log(vy)))
vpromlny=float(vlny/vn)
vxlny=float(sum(vx*np.log(vy)))

#Determinando la correlacion No lineal 


#encontraremos a=f y b=g
vg=(vxlny-vpromlny*vsumax)/(vsumaxx-vpromx*vsumax)
vf=np.exp(vpromlny-vg*vpromx)
#interpolacion lineal sería una funcion y = Kx + b y no lineal y = x^
print "Ecuacion Lineal de la forma y = Kx + b :"+" Y="+str(vm)+"X+"+str(vb) 
print "Ecuación Exponencial de la forma y = x^:"+" Y= "+str(vf)+"e**"+str(vg)
print "El valor de K con respecto a la regresion Lineal es:"+str(vm)

#.....
#graficando
plt.plot(vx,vy,'o',label='Datos' , color='blue')   
plt.plot(vx, vm*vx + vb, label='Regresion Lineal', color='red')
plt.plot(vx, vf*np.exp(vg*vx), label='Regresion Exponencial',color='yellow')
				
plt.title("Ley de hooke")   
plt.xlabel("Desplazamientos (m.)")    
plt.ylabel("Fuerza (10^4 N)")   
plt.grid()
plt.legend(loc=2)
# Mostramos en pantalla
plt.show()
