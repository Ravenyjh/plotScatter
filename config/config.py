# 211cell 的配置文件
configs211cellGv = {
    'pathFile': '2cellThreeTypicalStructure',
    'path_list': [
                  '2cellThreeTypicalStructure/macplot/ShortperiodSL/',
                  '2cellThreeTypicalStructure/macplot/Amorphousalloy/',
                  '2cellThreeTypicalStructure/macplot/Layerstructure/',
                  ],
    'case_name_list': ['Alternating monolayers','Disorder crystals','Layered structure'],
    'case_colors': ['blue', 'darkgray', 'red'],
    'case_types': ['s','v','o'],
    'line': [':', '--', '-'],
    'linewidth': [6, 6, 6]
}

configs211cellK = {
    'pathFile': '2cellThreeTypicalStructure',
    'path_list': [
                  '2cellThreeTypicalStructure/macplot/ShortperiodSL/',
                  '2cellThreeTypicalStructure/macplot/Amorphousalloy/',
                  '2cellThreeTypicalStructure/macplot/Layerstructure/',
                  ],
    'case_name_list': ['Alternating monolayers','Disordered crystal','Layered structure'],
    'case_colors': ['blue', 'darkgray', 'red'],
    'line': [(0, (5,0.5,0.5,0.5)), '--', '-'],
    'linewidth': [6, 6, 6]
}

configs211cellTau = {
    'pathFile': '2cellThreeTypicalStructure',
    'path_list': [
                  '2cellThreeTypicalStructure/macplot/ShortperiodSL/',
                  '2cellThreeTypicalStructure/macplot/Amorphousalloy/',
                  '2cellThreeTypicalStructure/macplot/Layerstructure/',
                  ],
    'case_name_list': ['Alternating monolayers','Disordered crystal','Layered structure'],
    'case_colors': ['blue', 'darkgray', 'red'],
    'case_types': ['s','v','o'],
    'line': [ (0, (5,0.5,0.5,0.5)), '--', '-'],
    'linewidth': [6, 6, 6]
}

configs211cellDosH = {
    'pathFile': '2cellThreeTypicalStructure',
    'path_list': ['2cellThreeTypicalStructure/macplot/ShortperiodSL/',
                  '2cellThreeTypicalStructure/macplot/Amorphousalloy/',
                  '2cellThreeTypicalStructure/macplot/Layerstructure/',
                  '2cellThreeTypicalStructure/macplot/Si/',
                  '2cellThreeTypicalStructure/macplot/Ge/',
                  ],
    'case_name_list': ['Alternating monolayers','Disordered crystal','Layered structure', 'Si', 'Ge'],
    'case_colors': ['blue', 'darkgray', 'red', 'purple', 'green'],
    'xAxis': [],
    'line': [(0, (5,0.5,0.5,0.5)), '--', '-', '--','--'],
    'linewidth': [6, 6, 6, 6, 6]
}

configs211cellDosV = {
    'pathFile': '2cellThreeTypicalStructure',
    'path_list': ['2cellThreeTypicalStructure/macplot/ShortperiodSL/',
                  '2cellThreeTypicalStructure/macplot/Amorphousalloy/',
                  '2cellThreeTypicalStructure/macplot/Layerstructure/'],
    'case_name_list': ['Alternating monolayers','Disordered crystal','Layered structure'],
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
        un + str(i + 1) + '/' for i in range(3)] +  [unRough + '/Si/', unRough + '/Ge/'],
    'case_name_list': ['Highly mixed', None, None, 'Moderately mixed', None,
                       None, 'Unmixed', None, None, 'Si', 'Ge'],
    'case_colors': ['blue', 'blue', 'blue', 'black', 'black', 'black', 'red', 'red', 'red', 'purple', 'green'],
    'line': ['-', '-', '-', '-', '-', '-', '-', '-', '-','--','--'],
    'linewidth': [2, 2, 2, 2, 2, 2, 3, 3, 3, 2 ,2]
}

# without Si Ge (和alloy 的gv 相差太大，画在一起不好看)
configs421cellGv = {
    'pathFile': '421cellDiffMixInterfaces',
    'path_list': [high + str(i + 1) + '/' for i in range(3)] + [mid + str(i + 1) + '/' for i in range(3)] + [
        un + str(i + 1) + '/' for i in range(3)],
    'case_name_list': ['Highly mixed (H)', None, None, 'Moderately mixed (M)', None, None, 'Unmixed (U)', None, None,
                       ],
    'case_colors': ['orange', 'orange', 'orange', 'black', 'black', 'black', 'red', 'red', 'red'],
    'line': ['-', '-', '-', '-', '-','-', '-', '-', '-'],
    'linewidth': [2, 2, 2, 2, 2, 2, 3, 3, 3]
}
