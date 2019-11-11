# plotScatter

用于将生成的2cell中的min结构，max结构，amorphous结构的1.热导率、2.gv、3.DOS，化成图。
其中，DOS为旋转后的，为了和dispersion图对应
数据来源： cluster ~/Si_Ge_alloy/conv/2cell/2cell_CFC-1map/scatter_etal/rearrangeed_file/3.0/plotSIMPLE.py
python3 DOS-2cell.py 2cell
python3 k.py
python3 gv.py 2cell


用于生成不同mixed 粗糙界面的DOS（需要修改config.py）
python3 DOS-421cell.py 421cell
python3 gv.py 421cell 


