high = "421cellDiffMixInterfaces/macplot/highMixed"
mid = "421cellDiffMixInterfaces/macplot/midMixed"
un = "421cellDiffMixInterfaces/macplot/unMixed"
unRough = "421cellDiffMixInterfaces/macplot"



configsDos = {
    'path_list': [high + str(i + 1) + '/' for i in range(3)] + [mid + str(i + 1) + '/' for i in range(3)] + [
        un + str(i + 1) + '/' for i in range(3)] + [unRough+ '/specularity/'] + [unRough + '/Si/', unRough + '/Ge/'],
    'case_name_list': ['Highly mixed', 'Highly mixed', 'Highly mixed', 'Moderately mixed', 'Moderately mixed',
                       'Moderately mixed', 'Unmixed', 'Unmixed', 'Unmixed', 'Smooth interface', 'Si', 'Ge']
}

# without Si Ge (和alloy 的gv 相差太大，画在一起不好看)
configsGv = {
    'path_list': [high + str(i + 1) + '/' for i in range(3)] + [mid + str(i + 1) + '/' for i in range(3)] + [
        un + str(i + 1) + '/' for i in range(3)] + [unRough+ '/specularity/'],
    'case_name_list': ['Highly mixed', 'Highly mixed', 'Highly mixed', 'Moderately mixed', 'Moderately mixed',
                       'Moderately mixed', 'Unmixed', 'Unmixed', 'Unmixed', 'Smooth interface']
}
