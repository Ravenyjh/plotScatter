#########################################
#this code study the k gv[x] lifetime versue omeg scat_combine_bands_DOSW_addk.py
#########################################

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import math as m
import os
import sys
lib_path = os.path.abspath(os.path.join('./config'))
sys.path.append(lib_path)
import configPlot
import config

params = configPlot.params
pylab.rcParams.update(params)
configs = config.configs211cell

path_list=configs['path_list']
case_name_list=configs['case_name_list']

# plt.rc('font',family='Times New Roman')

# path_list=['macplot/ShortperiodSL/','macplot/Amorphousalloy/','macplot/Layerstructure/']
# case_name_list=['Short period SL','Amorphous alloy','Layered structure']

ax_k = plt.subplot(1,1,1)
for i in range(len(path_list)):
	path=path_list[i]
	case_name=case_name_list[i]

	omega=np.loadtxt(path+'simplifiedOmega')
	k=np.loadtxt(path+'dosWeighedK')

	omegaTHZ=[x/(2*m.pi) for x in omega]
	###########
	# plot part
	############
	ax_k.plot(omegaTHZ,k,'-',label=case_name)
	ax_k.set_xlabel(r'$\omega$' +'(THz)')
	ax_k.set_ylabel(r'$k$'+'(W/(m-K))')
	print(case_name,":",sum(k))
plt.savefig('2cellThreeTypicalStructure'+'/K.png', bbox_inches='tight')
