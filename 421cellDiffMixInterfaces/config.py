high = "421cellDiffMixInterfaces/macplot/highMixed"
mid = "421cellDiffMixInterfaces/macplot/midMixed"
un = "421cellDiffMixInterfaces/macplot/unMixed"
pure = "421cellDiffMixInterfaces/macplot"

configs = {
    'path_list': [un + str(i + 1) + '/' for i in range(3)] + [mid + str(i + 1) + '/' for i in range(3)] + [
        high + str(i + 1) + '/' for i in range(3)] + [pure + '/Si/', pure + '/Ge/'],
    'case_name_list': ['Unmixed', 'Unmixed', 'Unmixed', 'Moderately mixed', 'Moderately mixed', 'Moderately mixed',
                       'Highly mixed', 'Highly mixed', 'Highly mixed', 'Si', 'Ge']
}