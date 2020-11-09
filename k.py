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
configs = config.configs211cellK

pathFile = configs['pathFile']
path_list=configs['path_list']
case_name_list=configs['case_name_list']
case_colors = configs['case_colors']
lineList=configs['line']
linewidthList=configs['linewidth']

ax_k = plt.subplot(1,1,1)
for i in range(len(path_list)):
	path = path_list[i]
	case_name = case_name_list[i]
	color = case_colors[i]
	line = lineList[i]
	linewidth = linewidthList[i]
	omega=np.loadtxt(path+'simplifiedOmega')
	k=np.loadtxt(path+'dosWeighedK')

	omegaTHZ=[x/(2*m.pi) for x in omega]
	###########
	# plot part
	############
	ax_k.set_xlim(0, 15.7)
	ax_k.set_ylim(0, 10)
	ax_k.plot(omegaTHZ, k, linestyle=line, color=color, linewidth=linewidth, label=case_name)
	# ax_k.plot(omegaTHZ, k, line, linewidth=linewidth, label=case_name)
	ax_k.set_xlabel('Frequency' +'(THz)')
	# ax_k.set_ylabel(r'$\kappa$'+'(W/(m-K))')
	ax_k.set_ylabel('Thermal conductivity' + ' <'+r'$\kappa$'+'> ' + '(W/(m-K))')
	ax_k.legend(loc=0)
	# ax_k.legend(loc="center left", bbox_to_anchor=(0, 0.7))
	print(case_name,":",sum(k))
plt.savefig('2cellThreeTypicalStructure'+'/K.png', bbox_inches='tight')
