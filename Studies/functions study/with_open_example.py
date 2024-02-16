with open('txt/test.txt') as f:
    for line in f:
        print(line,end='')
    print('Is the file closed inside with-open= ',f.closed)
print('Is the file closed out of with-open= ',f.closed)