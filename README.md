# plotScatter

1. 2cell相关   
	1. 用于将生成的2cell中的min结构，max结构，amorphous结构的      
		* k-omega
		* gv-omega
		* Dos-omega,  
	的Dos weighted图(Dos-omega除外)。    
	其中，为了和dispersion图对应,DOS旋转90度。   
	2. 数据来源： cluster ~/Si_Ge_alloy/conv/2cell/2cell_CFC-1map/scatter_etal/rearrangeed_file/3.0/plotSIMPLE.py
	3. 画图脚本命令   
	- python3 DOS-2cell.py 2cell
	- python3 k.py
	- python3 gv.py 2cell


2. 用于生成不同mixed 粗糙界面
- gv-omega
- Dos-omega   
的Dos weighted图(Dos-omega除外)。  
* 数据来源： cluster ~/Si_Ge_alloy/conv/421cell/kr_rough/klemens/....
* 画图脚本命令
- python3 DOS-421cell.py 421cell
- python3 gv.py 421cell 


