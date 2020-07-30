import glob

root_dir = '/home/nightingale/Documents/jeff_dev/Hobby_Projects/'

for filename in glob.iglob(root_dir + '**/*.pdf', recursive=True):
     print(filename)