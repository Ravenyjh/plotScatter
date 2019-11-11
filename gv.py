#########################################
#this code study the k gv[x] lifetime versue omeg scat_combine_bands_DOSW_addk.py
#########################################

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import configPlot
import numpy as np
import math as m
import os
import sys

params = configPlot.params
pylab.rcParams.update(params)

case = sys.argv
if case[1] == '2cell':
	pathFile = '2cellThreeTypicalStructure'
elif case[1] == '421cell':
	pathFile = '421cellDiffMixInterfaces'
else:
	pathFile = '2cellThreeTypicalStructure'
	print('请输入2cell或者421cell，默认为2cell')

lib_path = os.path.abspath(os.path.join(pathFile))
sys.path.append(lib_path)
import config
configs = config.configs

path_list=configs['path_list']
case_name_list=configs['case_name_list']


#path_list=['macplot/ShortperiodSL/','macplot/Amorphousalloy/','macplot/Layerstructure/']
#case_name_list=['Short \nperiod SL','Amorphous \nalloy','Layered \nstructure']

ax_g = plt.subplot(1,1,1)
for i in range(len(path_list)):
	path=path_list[i]
	case_name=case_name_list[i]
	omega=np.loadtxt(path+'simplifiedOmega')
	gv=np.loadtxt(path+'dosWeighedGv')
	omegaTHZ=[x/(2*m.pi) for x in omega]
	###########
	# plot part
	###########
	line = '-'
	if (i + 1) % 3 == 0:
		label = case_name
	else:
		label = ''
	if i//3 == 0:
		color = 'black'
	elif i//3 == 1:
		color = 'red'
	else:
		color = 'blue'

	if case_name  == 'Si':
		label = case_name
		line = '--'
		color = 'green'
	if case_name  == 'Ge':
		label = case_name
		line = '--'
		color = 'purple'
	ax_g.plot(omegaTHZ,gv,line ,color=color,ms=3,mew=0,label=label)
	ax_g.legend(loc=0,frameon=False)

ax_g.set_xlabel(r'$\omega$' +'(THz)')
ax_g.set_ylabel('<'+r'$v_g^2$'+'>'+'('+r'$ \mathrm{km}^2/ \mathrm{s}^2$'+')')
plt.savefig(pathFile + '/gv.png', bbox_inches='tight')
