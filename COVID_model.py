from scipy.integrate import odeint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# SIR modeel
def SIR(y, t, Ntot, b, a1, a2, Qstart=22):
    S, I, R = y

    if t <= (Qstart):
        B = a1
    else:
        B = a1 * np.exp(-(t - Qstart) / a2)

    print(B)

    dSdt = -(B * I / Ntot) * S
    dIdt = (B * S / Ntot) * I - b * I
    dRdt = b * I

    return dSdt, dIdt, dRdt


def compute_ODE(Ntot, a1, a2, b, letality, Qstart = 22,I0=1, R0=0, t=np.arange(0, 365)):
    S0 = Ntot - I0 - R0  #
    y0 = S0, I0, R0
    ret = odeint(SIR, y0, t, args=(Ntot, b, a1, a2, Qstart))
    S, I, R = np.transpose(ret)

    return t, S, I, (1 - letality / 100) * R, R * letality / 100


dataITA=pd.read_csv('COVID_19data.txt')

xdata=dataITA['Time']
ydata=dataITA['Infected']
ydata_death=dataITA['Deaths']
ydata_rec=dataITA['Recovered']


output=compute_ODE(60*10**6,0.415,25,1/14,4.5,Qstart=17,I0 = 2,t = np.arange(0,720)) #beta2 = 25 default beta1=0.415

t=output[0]
S_vec=output[1]
I_vec=output[2]
R_vec=output[3]
M_vec=output[4]


plt.figure()
plt.errorbar(xdata+14,ydata-ydata_rec,np.sqrt(ydata-ydata_rec),color='green',linestyle='--',marker='o')
plt.errorbar(xdata+14,ydata_death,np.sqrt(ydata_death),color='black',linestyle='--',marker='o')
plt.errorbar(xdata+14,ydata_rec,np.sqrt(ydata_rec),color='blue',linestyle='--',marker='o')
plt.plot(t, I_vec/3, 'g--', label='Infected/3')
plt.plot(t, S_vec, 'm--', label='Susceptible')
plt.plot(t, R_vec, 'b--', label='Recovered with immunity')
plt.plot(t, M_vec, 'k--', label='Deaths')
plt.xlabel('Number of days after the first infect')
plt.ylabel('Number')
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.yscale('log')
plt.xlim(0,180)
plt.ylim(1,0.2*10**8)
#plt.savefig('SIR_output.png',dpi=300)
plt.show()



print('Deaths',int(M_vec[-1]))
print('Total infected ',int(M_vec[-1]+R_vec[-1]))
print('Max. infected ',int(I_vec.max()))
print('Max. infected (hospitalized)',int(I_vec.max()/3*20/100))

print(I_vec)




