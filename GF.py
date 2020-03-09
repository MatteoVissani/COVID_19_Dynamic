import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataITA=pd.read_csv('COVID_19data.txt')

xdata=dataITA['Time']
ydata=dataITA['Infected']
ydata_death=dataITA['Deaths']
ydata_rec=dataITA['Recovered']



# data increment
deltaI = []


GFI = []
GFR = []
GFM = []

for i in range(3, len(ydata)):
    deltaI.append((ydata[i] - ydata[i - 1]))


for i in range(1,len(deltaI)):
    GFI.append(deltaI[i]/deltaI[i-1])
    #GFR.append(deltaR[i]/deltaR[i-1])
    #GFM.append(deltaM[i]/deltaM[i-1])


plt.figure()
plt.plot(xdata[xdata >= 3], deltaI,label='Infects')
plt.xlabel('Days from the beginning')
plt.ylabel('Variation(day - (day- 1)')
plt.xlim(0, 20)
#plt.ylim(-20 ,70)
plt.legend()
plt.savefig('variation_days.png', dpi=300)
plt.show()

plt.figure()
plt.plot(xdata[xdata >= 4], GFI,label='Infects')
plt.xlabel('Days from the beginning')
plt.ylabel('Growth Factor')
plt.xlim(0, 20)
#plt.ylim(-20 ,70)
plt.legend()
plt.savefig('GF.png', dpi=300)
plt.show()


print('mean GF value is',np.mean(GFI))
print('median GF value is',np.median(GFI))
print('std GF value is',np.median(GFI))


plt.figure()
plt.plot(ydata)
plt.plot(deltaI)

plt.yscale('log')
plt.show()