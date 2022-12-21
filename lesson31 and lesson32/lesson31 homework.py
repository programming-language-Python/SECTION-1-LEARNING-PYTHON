# Написать функцию, которое получает дерево заданного каталога
import os

for root, dirs, files in os.walk('folder'):
    basename = os.path.basename(root)
    print(basename)
    if dirs:
        print(*['\t' + folder for folder in dirs], sep='\n')
    if files:
        print(*['\t' + file for file in files], sep='\n')
