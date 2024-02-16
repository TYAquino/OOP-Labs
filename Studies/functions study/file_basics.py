file_name = input('Please enter a file name: ')
#Step 1: open the file for writing using open()
#f_obj = open('test.txt',mode='w')
f_obj = open(file_name,mode='a')

#Step 2: Writing a message into a file
f_obj.write('Welcome in Ruby\n')

#Step 3: closing the file
f_obj.close()
print(f'{file_name} is written/created')

print('Reading test.txt file')
file_path = 'txt/'+file_name
f = open(file_path,'r')
#use loop to read line by line
for line in f:
    print(line, end='')
f.close()

print('reading using read()')
file_path = 'txt/'+file_name
f = open(file_path,'r')
#use read() or readlines()
#content = f.read()
content = f.readlines()
print(content)
f.close()