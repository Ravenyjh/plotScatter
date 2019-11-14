import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import math as m
import sys
import os

lib_path = os.path.abspath(os.path.join('./config'))
sys.path.append(lib_path)
import configPlot
import config

params = configPlot.params
pylab.rcParams.update(params)

case = sys.argv
if case[1] == '2cell':
	configs = config.configs211cellDos
elif case[1] == '421cell':
	configs = config.configs421cellDos
else:
	configs = config.configs211cellDos
	print('请输入2cell或者421cell，默认为2cell')


pathFile = configs['pathFile']
path_list=configs['path_list']
case_name_list=configs['case_name_list']
case_colors = configs['case_colors']
lineList=configs['line']
linewidthList=configs['linewidth']
ax_d = plt.subplot(1,1,1)

for i in range(len(path_list)):
	path=path_list[i]
	case_name=case_name_list[i]
	color = case_colors[i]
	line = lineList[i]
	linewidth = linewidthList[i]
	omega=np.loadtxt(path+'simplifiedOmega')
	DOS=np.loadtxt(path+'dos')
	omegaTHZ=[x/(2*m.pi) for x in omega]
	###########
	# plot part
	############
	# ax_d.set_yscale('log')
	ax_d.set_yticks([])
	ax_d.plot(omegaTHZ, DOS, line , color=color, linewidth = linewidth, label=case_name)



ax_d.legend(loc=0, frameon=False)
ax_d.set_ylabel('DOS')
ax_d.set_xlabel(r'$\omega$' + '(THz)')
# ax_d.set_xlim(0, 1200)
# ax_d.set_ylim(2, 16)

#plt.show()
plt.savefig(pathFile+'/Dos.png',bbox_inches='tight')
