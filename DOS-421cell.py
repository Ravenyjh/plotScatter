import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import configPlot
import numpy as np
import math as m
import sys
import os
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
configs = config.configsDos

path_list=configs['path_list']
case_name_list=configs['case_name_list']

ax_d = plt.subplot(1,1,1)

for i in range(len(path_list)):
	path=path_list[i]
	case_name=case_name_list[i]
	omega=np.loadtxt(path+'simplifiedOmega')
	DOS=np.loadtxt(path+'dos')
	omegaTHZ=[x/(2*m.pi) for x in omega]
	###########
	# plot part
	############
	# ax_d.set_yscale('log')
	ax_d.set_yticks([])
	line = '-'
	linewidth = 2
	if i % 3 == 0:
		label = case_name
	else:
		label = ''
	if i// 3 == 2:
		color = 'red'
		linewidth = 3
	elif i // 3 == 1:
		color = 'black'
	else:
		color = 'orange'

	if case_name  == 'Si':
		label = case_name
		line = '--'
		color = 'green'
	if case_name  == 'Ge':
		label = case_name
		line = '--'
		color = 'purple'
	if case_name  == 'Smooth interface':
		label = case_name
		line = '-'
		color = 'blue'
		linewidth = 3

	ax_d.plot(omegaTHZ, DOS, line , color=color, linewidth = linewidth, label=label)
ax_d.legend(loc=0, frameon=False)
ax_d.set_ylabel('DOS')
ax_d.set_xlabel(r'$\omega$' + '(THz)')
	# ax_d.set_xlim(0, 1200)
	# ax_d.set_ylim(2, 16)

# plt.yticks(size=30)
# plt.xticks(size=0)
#plt.show()
plt.savefig(pathFile+'/Dos.png',bbox_inches='tight')
