#########################################
#this code study the k gv[x] lifetime versue omeg scat_combine_bands_DOSW_addk.py
#########################################
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math as m
plt.rc('font',family='Times New Roman')
plt.rcParams['mathtext.fontset'] = 'stix'

path_list=['macplot/ShortperiodSL/','macplot/Amorphousalloy/','macplot/Layerstructure/']
case_name_list=['Short period SL','Amorphous alloy','Layer structure']

font={'size':'35', 'weight':'normal'}
plt.figure(figsize=(8,9))
ax_d = plt.subplot(1,1,1)
plt.subplots_adjust(left=0.3, bottom=0.1, right=0.8, top=0.9)
	
for i in range(len(path_list)):
	path=path_list[i]
	case_name=case_name_list[i]
	omega=np.loadtxt(path+'x_g_1')
	y_g1_1=np.loadtxt(path+'y_g1_1')
	DOS=np.loadtxt(path+'y_l2_1')
	y_k1_1=np.loadtxt(path+'y_k1_1')
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
plt.savefig('Dos.png',bbox_inches='tight')
