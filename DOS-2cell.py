import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import math as m
import sys
import os
import matplotlib.ticker as ticker

lib_path = os.path.abspath(os.path.join('./config'))
sys.path.append(lib_path)
import configPlot
import config

params = configPlot.params
pylab.rcParams.update(params)

case = sys.argv
if case[1] == '2cell':
	configs = config.configs211cellDosV
elif case[1] == '421cell':
	configs = config.configs421cellDos
else:
	configs = config.configs211cellDosV
	print('请输入2cell或者421cell，默认为2cell')

pathFile = configs['pathFile']
path_list=configs['path_list']
case_name_list=configs['case_name_list']
case_colors = configs['case_colors']
lineList=configs['line']
linewidthList=configs['linewidth']

plt.figure(figsize=(4.5,8))
ax_d = plt.subplot(1,1,1)
plt.subplots_adjust(left=0.3, bottom=0.1, right=0.8, top=0.9)
	
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
	ax_d.plot(DOS,omegaTHZ,line , color=color, linewidth = linewidth, label=case_name)
	# ax_d.legend(loc="center right", bbox_to_anchor=(1, 0.3))
	ax_d.set_xlabel('DOS')
	ax_d.set_xlim(0, 7e25)
	ax_d.set_ylim(1, 16.224090)
	ax_d.set_xticklabels(configs['xAxis'])
	ax_d.yaxis.set_major_locator(ticker.MultipleLocator(5))

plt.savefig(pathFile+'/Dos.png',bbox_inches='tight')
