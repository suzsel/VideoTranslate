'''
    This is for deepl api, but know I am not sure is there limit on number of characters in file
'''

import math 

def split_txt(file):
    with open(file,  encoding='utf-8', mode = 'r') as file:
        data = file.read().replace('\n', '')
        print('f check for cyrillic {data[:5]}')
        
        n_files =  math.ceil(len(data) / 5000)
        for i in range(0, n_files):
            z = i * 5000
            j = (i+1) * 5000
            with open('res'+str(i), mode = 'w', encoding='utf-8') as res:
                res.write(data[z:j])
            print(f'i = {i}, z = {z}, j = {j}')
