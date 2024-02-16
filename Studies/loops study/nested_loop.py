'''Nested Loop
write a program which displays the multiplication table
1X1=1
1X2=2
2X1=2
2X2=4'''
for i in range(1,13):  # outer loop
    for j in range(i,13):   # inner loop
        print(f'{i}X{j}={i*j}')