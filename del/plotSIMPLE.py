#########################################
#this code study the k gv[x] lifetime versue omeg scat_combine_bands_DOSW_addk.py
#########################################



#from  scat_combine_bands_DOSW_addk import scat_etal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import math as m

path_list=['macplot/ShortperiodSL/','macplot/Amorphousalloy/','macplot/Layerstructure/']
case_name_list=['Short period SL','Amorphous alloy','Layer structure']
#font={'family': 'Times', 'weight':'normal'}
font={'weight':'normal'}
for i in range(len(path_list)):
	path=path_list[i]
	case_name=case_name_list[i]

	x_g_1=np.loadtxt(path+'x_g_1')
	y_g1_1=np.loadtxt(path+'y_g1_1')
	y_l2_1=np.loadtxt(path+'y_l2_1')
	y_k1_1=np.loadtxt(path+'y_k1_1')
	#x_g_1,y_g1_1,x_l_1,y_l1_1,x_k_1,y_k1_1,y_l2_1=scat_etal(path)
	"""
	np.savetxt('macplot/x_g_1'+case_name,x_g_1)
	np.savetxt('macplot/y_g1_1'+case_name,y_g1_1)
	np.savetxt('macplot/y_l2_1'+case_name,y_l2_1)
	np.savetxt('macplot/y_k1_1'+case_name,y_k1_1)
	"""
	x_g_1=[x/(2*m.pi) for x in x_g_1]
	
	###########
	# plot part
	############


	plt.figure(1)

	ax_d = plt.subplot(1,1,1)
	plt.figure(1)
	ax_k = plt.subplot(1,1,1)
	plt.figure(1)
	ax_g = plt.subplot(1,1,1)
	plt.figure(1)
	ax_l = plt.subplot(1,1,1)
	plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.3, hspace=0.8)

	ax_d.plot(x_g_1,y_l2_1,'-',ms=1,mew=0,label=case_name)
	ax_d.legend(loc=0,prop={'size':6})
	ax_d.set_xlabel(r'$\omega$' +'(THZ)',font)
	ax_d.set_ylabel('DOS',font)
	#ax_d.set_title('DOS_BTE.dos')
	ax_d.set_xlim(0, 5)
	#ax_d.xaxis([0, 6])

	ax_g.plot(x_g_1,y_g1_1,'-',ms=3,mew=0,label=case_name)
	ax_g.legend(loc=0,prop={'size':6})
	ax_g.set_xlabel(r'$\omega$' +'(THZ)',font)
	ax_g.set_ylabel('<'+r'$v_g^2$'+'>'+'('+r'${km}^2/s^2$'+')',font)
	#ax_g.set_title('gv^2-w(DOS weighted)')
	ax_g.set_xlim(0, 5)


	ax_k.plot(x_g_1,y_k1_1,'-',ms=3,mew=0,label=case_name)
	ax_k.legend(loc=0,prop={'size':6})
	#ax2.scatter(x,y, c='r', s = 1)
	ax_k.set_xlabel(r'$\omega$' +'(THZ)',font)
	ax_k.set_ylabel('<K>',font)
	ax_k.set_xlim(0, 5)
	#ax_k.set_title('K-w (DOS weighted)')
	#ax_g1.axis([0, 100])

	print case_name,":",sum(y_k1_1)

plt.savefig('revised'+str(case_name_list[0])+str(case_name_list[1])+str(case_name_list[2])+'.png', dpi = 300)
