# 211cell 的配置文件
configs211cellGv = {
    'pathFile': '2cellThreeTypicalStructure',
    'path_list': ['2cellThreeTypicalStructure/macplot/ShortperiodSL/',
                  '2cellThreeTypicalStructure/macplot/Amorphousalloy/',
                  '2cellThreeTypicalStructure/macplot/Layerstructure/'],
    'case_name_list': ['Short period SL','Amorphous alloy','Layer structure'],
    'case_colors': ['blue', 'black', 'red'],
    'line': ['-', '-', '-'],
    'linewidth': [3, 3, 3]
}

configs211cellDos = {
    'pathFile': '2cellThreeTypicalStructure',
    'path_list': ['2cellThreeTypicalStructure/macplot/ShortperiodSL/',
                  '2cellThreeTypicalStructure/macplot/Amorphousalloy/',
                  '2cellThreeTypicalStructure/macplot/Layerstructure/'],
    'case_name_list': ['Short\n period SL', 'Amorphous\n alloy', 'Layer\n structure'],
    'case_colors': ['blue', 'black', 'red'],
    'xAxis': [],
    'line': ['-', '-', '-'],
    'linewidth': [2, 2, 2]
}

# 421cell 的配置文件
high = "421cellDiffMixInterfaces/macplot/highMixed"
mid = "421cellDiffMixInterfaces/macplot/midMixed"
un = "421cellDiffMixInterfaces/macplot/unMixed"
unRough = "421cellDiffMixInterfaces/macplot"

configs421cellDos = {
    'pathFile': '421cellDiffMixInterfaces',
    'path_list': [high + str(i + 1) + '/' for i in range(3)] + [mid + str(i + 1) + '/' for i in range(3)] + [
        un + str(i + 1) + '/' for i in range(3)] + [unRough+ '/specularity/'] + [unRough + '/Si/', unRough + '/Ge/'],
    'case_name_list': ['Highly mixed', None, None, 'Moderately mixed', None,
                       None, 'Unmixed', None, None, 'Smooth interface', 'Si', 'Ge'],
    'case_colors': ['orange', 'orange', 'orange', 'black', 'black', 'black', 'red', 'red', 'red', 'blue', 'purple', 'green'],
    'line': ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','--','--'],
    'linewidth': [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2 ,2]
}

# without Si Ge (和alloy 的gv 相差太大，画在一起不好看)
configs421cellGv = {
    'pathFile': '421cellDiffMixInterfaces',
    'path_list': [high + str(i + 1) + '/' for i in range(3)] + [mid + str(i + 1) + '/' for i in range(3)] + [
        un + str(i + 1) + '/' for i in range(3)] + [unRough+ '/specularity/'],
    'case_name_list': ['Highly mixed', None, None, 'Moderately mixed', None, None, 'Unmixed', None, None,
                       'Smooth interface'],
    'case_colors': ['orange', 'orange', 'orange', 'black', 'black', 'black', 'red', 'red', 'red', 'blue'],
    'line': ['-', '-', '-', '-', '-','-', '-', '-', '-', '-'],
    'linewidth': [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
}
