#########################################
#this code study the k gv[x] lifetime versue omeg scat_combine_bands_DOSW_addk.py
#########################################

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import configPlot
import numpy as np
import math as m
params = configPlot.params
pylab.rcParams.update(params)

path_list=['macplot/ShortperiodSL/','macplot/Amorphousalloy/','macplot/Layerstructure/']
case_name_list=['Short \nperiod SL','Amorphous \nalloy','Layered \nstructure']
ax_g = plt.subplot(1,1,1)
for i in range(len(path_list)):
	path=path_list[i]
	case_name=case_name_list[i]
	omega=np.loadtxt(path+'simplifiedOmega')
	gv=np.loadtxt(path+'dosWeighedGv')
	omegaTHZ=[x/(2*m.pi) for x in omega]
	###########
	# plot part
	############
	ax_g.plot(omegaTHZ,gv,'-',ms=3,mew=0,label=case_name)
	ax_g.legend(loc=0,frameon=False)
	ax_g.set_xlabel(r'$\omega$' +'(THz)')
	ax_g.set_ylabel('<'+r'$v_g^2$'+'>'+'('+r'$ \mathrm{km}^2/ \mathrm{s}^2$'+')')
plt.savefig('gv.png', bbox_inches='tight')
