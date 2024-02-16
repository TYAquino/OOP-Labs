import os
#print(help(os))
print(dir(os))
cwd = os.getcwd()
print(cwd)
file_path = os.path.join(cwd,'test.txt')
print(file_path)

print(os.path.exists('test1.txt'))
if os.path.exists('test1.txt'):
    print('file exists')
else:
    print('file does not exist')
os.remove('x')
