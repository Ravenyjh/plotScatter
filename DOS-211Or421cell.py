import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import math as m
import sys
import os
from scipy.interpolate import interp1d

lib_path = os.path.abspath(os.path.join('./config'))
sys.path.append(lib_path)
import configPlot
import config

params = configPlot.params
pylab.rcParams.update(params)

case = sys.argv
if case[1] == '2cell':
	configs = config.configs211cellDosH
elif case[1] == '421cell':
	configs = config.configs421cellDos
else:
	configs = config.configs211cellDosH
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
	if case[1] == '2cell' and (case_name == 'Si' or case_name == 'Ge'):
		omegaTHZ1 = np.linspace(min(omegaTHZ), max(omegaTHZ), 100)
		DOS1 = []
		for i in range(len(omegaTHZ1)):
			temp = []
			for j in range(len(omegaTHZ)):
				if omegaTHZ1[j] > omegaTHZ[i] -0.2 and omegaTHZ1[j] < omegaTHZ[i] + 0.2:
					temp.append(DOS[j])
			DOS1.append(np.average(temp))
		omegaTHZ = omegaTHZ1
		DOS = DOS1
	elif case[1] == '2cell':
		omegaTHZ1 = np.linspace(min(omegaTHZ), max(omegaTHZ), 100)
		DOS1 = []
		for i in range(len(omegaTHZ1)):
			temp = []
			for j in range(len(omegaTHZ)):
				if omegaTHZ1[j] > omegaTHZ[i] -0.2 and omegaTHZ1[j] < omegaTHZ[i] + 0.2:
					temp.append(DOS[j])
			DOS1.append(np.average(temp))
		omegaTHZ = omegaTHZ1
		DOS = DOS1

	if case_name != 'Si' and case_name != 'Ge':
		li = interp1d(omegaTHZ, DOS, kind='cubic')
		omegaTHZnew = np.linspace(min(omegaTHZ), max(omegaTHZ), 2000)
		DOSnew = li(omegaTHZnew)
		ax_d.plot(omegaTHZnew, DOSnew, linestyle=line, color=color, linewidth = linewidth, label=case_name)
	else:
		li = interp1d(omegaTHZ, DOS, kind = 'cubic')
		omegaTHZnew = np.linspace(min(omegaTHZ), max(omegaTHZ), 2000)
		print((max(omegaTHZ)-min(omegaTHZ))/2000.0)
		DOSnew = li(omegaTHZnew)
		ax_d.bar(omegaTHZnew, DOSnew, width=0.00787816968304884, color = color, label = case_name, alpha=0.3)

# ax_d.legend(loc=0)
# ax_d.legend(loc="center left", bbox_to_anchor=(0, 0.65))
ax_d.set_ylabel('DOS')
ax_d.set_xlabel('Frequency' + '(THz)')
ax_d.set_xlim(2, 5)
ax_d.set_ylim(0, 2e26)
# ax_d.set_ylim(0, 4E25)
# ax_d.set_ylim(0, 7E25)
# ax_d.set_xticks([2, 3, 4, 5])

#plt.show()
plt.savefig(pathFile+'/Dos.png',bbox_inches='tight')
