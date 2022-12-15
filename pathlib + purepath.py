# pathlib used to work with paths(file path, url path, etc.) in windows, mac and linux

import pathlib

path = pathlib.Path(__file__)  #__file__ returns a path to this present file/script
print(path)

'''
Pure paths provide computational operations, and windows path provide input/output operations. 
Pure paths only manipulate paths, rather than creating a new file or directory. They do not have 
OS-accessing operations.
'''

windows_path = pathlib.WindowsPath(__file__)
pure_windows_path = pathlib.PureWindowsPath(__file__)

print(windows_path)
print(pure_windows_path)

print(windows_path.parts) #break the path into its parts/components
print(windows_path.parent) #get the folder above the file in which we are currently working
print(windows_path.parents[0])
print(windows_path.parents[1])
print(windows_path.parents[2])

data_folder = pathlib.Path(__file__).parents[0].joinpath('join_method_sample')
if not data_folder.exists():
    data_folder.mkdir()  #create new directory folder

data_folder.joinpath('data.txt').touch(exist_ok=True) #create new .txt file, if already exists, overwrite
data_folder.joinpath('data.csv').touch(exist_ok=True)
data_folder.joinpath('data.json').touch(exist_ok=True)
data_folder.joinpath('data_sample').mkdir(exist_ok=True)

print(pathlib.Path.cwd()) #current working directory
