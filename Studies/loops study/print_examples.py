print('Line 1',end='\n')
print('Line 2')
print('Line 3','Line 4',sep="//")
value = 6412345.6789
print(format(value, ",.2f"))

mon = 5
print ("Enter electricity usage for month", mon, "enter kwh:", end='')
kwh = float ( input())
price_elect = kwh * 0.0097
print ("Price of electricity is $", format(price_elect, ".2f"), sep = '')

# put in a file and run
print ("12345678901234")
print (format (123456.789, ",.2f"))
print (format (123456.789, "20.2f"))

print (format (123456.789, ".2e"))
print (format (0.5, "%"))
print (format (0.5, ".2%"))
print (format (123, "d"))
print (format (123, "7d"))
print (format ("Hello", "10s"))

name = "Eric" 
age = 74 
print("Hello, %s. You are %d." % (name, age))

course = "Python"
print(f'{course}')
print(f'{course:>20}')
print(f'{course:<20}')
print('-'*20)
print(f'{course:^20}')

print('-'*100)
print(f'{"Welcome in Oil/Gas Program":^100}')
print('-'*100)



