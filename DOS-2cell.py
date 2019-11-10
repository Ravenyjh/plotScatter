#########################################
#this code study the k gv[x] lifetime versue omeg scat_combine_bands_DOSW_addk.py
#########################################
import matplotlib.pyplot as plt
import numpy as np
import math as m
import sys
import os

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

plt.rc('font',family='Times New Roman')
plt.rcParams['mathtext.fontset'] = 'stix'

path_list=configs['path_list']
case_name_list=configs['case_name_list']

font={'size':'35', 'weight':'normal'}
plt.figure(figsize=(8,9))
ax_d = plt.subplot(1,1,1)
plt.subplots_adjust(left=0.3, bottom=0.1, right=0.8, top=0.9)
	
for i in range(len(path_list)):
	path=path_list[i]
	case_name=case_name_list[i]
	omega=np.loadtxt(path+'simplifiedOmega')
	DOS=np.loadtxt(path+'dos')
	omegaTHZ=[x/(2*m.pi) for x in omega]
	###########
	# plot part
	############
	ax_d.plot(DOS,omegaTHZ,'-',ms=2,mew=1,label=case_name)
	ax_d.set_xlabel('DOS', font)
	ax_d.set_xlim(0, 1200)
	ax_d.set_ylim(2, 16)

plt.yticks(size=30)
plt.xticks(size=0)
#plt.show()
plt.savefig(pathFile+'/Dos.png',bbox_inches='tight')
