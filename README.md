# plotScatter

1. 2cell   
	1. 用于将生成的2cell中的min结构，max结构，amorphous结构的Dos weighted图(Dos-omega除外)。为了和dispersion图对应,DOS-omega图旋转90度。       
		* k-omega
		* gv-omega
		* Dos-omega,  
	2. 数据来源： cluster ~/Si_Ge_alloy/conv/2cell/2cell_CFC-1map/scatter_etal/rearrangeed_file/plotScatter-New/plotSIMPLE.py
	3. 画图脚本命令   
		* python3 DOS-2cell.py 2cell
		* python3 k.py
		* python3 gv.py 2cell

2. 421cell   
	1. 用于生成不同mixed 粗糙界面结构的Dos weighted图(Dos-omega除外)。   
		* gv-omega
		* Dos-omega
	2. 数据来源： cluster ~/Si_Ge_alloy/conv/421cell/kr_rough/klemens/....
	3. 画图脚本命令   
		* python3 DOS-421cell.py 421cell
		* python3 gv.py 421cell 


