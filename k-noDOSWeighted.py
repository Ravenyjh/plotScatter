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

case = sys.argv
if case[1] == '211cell':
	configs = config.configs211cellGv
elif case[1] == '421cell':
	configs = config.configs421cellGv
else:
	configs = config.configs211cellGv
	print('请输入2cell或者421cell，默认为2cell')

pathFile = configs['pathFile']
path_list=configs['path_list']
case_name_list=configs['case_name_list']
case_colors = configs['case_colors']
lineList=configs['line']
linewidthList=configs['linewidth']

ax_g = plt.subplot(1,1,1)
for i in range(len(path_list)):
    path=path_list[i]
    case_name=case_name_list[i]
    color=case_colors[i]
    line=lineList[i]
    linewidth=linewidthList[i]
    omega=np.loadtxt(path+'omega_full1')
    gv = np.loadtxt(path+'k_reduced')
    gv = [x for x in gv]
    omegaTHZ=[x/(2*m.pi) for x in omega]
    ###########
    # plot part
    ###########

    # ax_g.plot(omegaTHZ,gv,'o' ,color=color,markersize=10, mew=2, mfc='none',label=case_name)
    # ax_g.semilogy(omegaTHZ,gv,'o' ,color=color,markersize=8, mew=1,label=case_name)
    ax_g.plot(omegaTHZ,gv,'o' ,color=color,markersize=8, mew=1,label=case_name)
    # ax_g.plot(omegaTHZ,gv,'o',markersize=8, mew=1,label=case_name)
    ax_g.legend(loc=0)

ax_g.set_xlim(0, 15.7)
# ax_g.set_ylim(0, 50)
# ax_g.set_yscale('log')
ax_g.set_xticks([0, 5, 10, 15])
# ax_g.set_yticks([200])
ax_g.set_xlabel('Frequency' +'(THz)')
ax_g.set_ylabel('Square of group velocity' + ' '+r'$v_g^2$'+' '+'('+r'$ \mathrm{km}^2/ \mathrm{s}^2$'+')')
plt.savefig(pathFile + '/k-noDOS.png', bbox_inches='tight')
