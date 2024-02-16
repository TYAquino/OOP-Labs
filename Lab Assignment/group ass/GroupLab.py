'''
file name: Group lab assignment.py
Authors: Trisha Aquino, Robert Hansen, Kaleb Berhane
Description: A group lab assignment in Object-Oriented Programming
Version: Oct. 8, 2023
'''
print('-'*40)
print('**Welcome to Gas Station Program!**')
print('-'*40)
print('Select the type of purchase: \nG: Gas \nO: Oil')

# Step 1 - let the user choose between gas or oil
gas = 'g'
oil = 'o'

choice = input('>>> ').lower()
    
if choice == 'g':
    L_gas = int(input('Enter the number of litres of gas: '))
    prov = input('Enter your province (abbreviation): ').upper()
    print('-'*60)
    gas_amount = (L_gas * 1.07)
    gas_max = 4000

    if (gas_amount > gas_amount):
        discount = gas_amount - ((10 * gas_amount) / 100)
 
        if prov == 'AB' or prov == 'BC' or prov == 'MB' or prov == 'NT' or prov == 'NU' or prov == 'QC' or prov == 'SK' or prov == 'YT':
            gst = discount * 0.05
            total = discount + gst
            print(f'{L_gas}, {gas_amount}, {discount}, {gst}, {total}')
        elif prov == 'ON':
            gst = discount * 0.13
            total = discount + gst
            print(f'{L_gas}, {gas_amount}, {discount}, {gst}, {total}')
        else:
            gst = discount * 0.15
            total = discount + gst
            print(f'{L_gas}, {gas_amount}, {discount}, {gst}, {total}')
        print('-'*60)
        print('Thanks for your business. Good Bye!')
    
    else:
        if prov == prov == 'AB' or prov == 'BC' or prov == 'MB' or prov == 'NT' or prov == 'NU' or prov == 'QC' or prov == 'SK' or prov == 'YT':
            gst = gas_amount * 0.05
            total = gas_amount + gst
            print(f'{L_gas}, {gas_amount}, {gas_amount}, {gst}, {total}')
        elif prov == 'ON':
            gst = gas_amount * 0.13
            total = gas_amount + gst
            print(f'{L_gas}, {gas_amount}, {gas_amount}, {gst}, {total}')
        else:
            gst = gas_amount * 0.15
            total = gas_amount + gst
            print(f'{L_gas}, {gas_amount}, {gas_amount}, {gst}, {total}')
        print('-'*60)
        print('Thanks for your business. Good Bye!')

elif choice == 'o':
    cases_oil = int(input('Enter the number of cases of oil: '))
    oil_prices = cases_oil * 12
    prov = input('Enter your province (abbreviation): ').upper()
    print('-'*60)
    oil_total = (12 * 1.27) * cases_oil
    oil_max = 8

    if (oil_total > oil_max):
        discount_oil = oil_total - (10 * oil_total / 100)

        if (prov == prov == prov == 'AB' or prov == 'BC' or prov == 'MB' or prov == 'NT' or prov == 'NU' or prov == 'QC' or prov == 'SK' or prov == 'YT'):
            gst = discount_oil * 0.05
            total = discount_oil + gst
            print(f'{oil_prices}, {oil_total}, {discount_oil}, {gst: .2f}, {total: .2f}')
        elif prov == 'ON':
            gst = discount_oil * 0.13
            total = discount_oil + gst
            print(f'{oil_prices}, {oil_total}, {discount_oil}, {gst: .2f}, {total: .2f}')
        else:
            gst = discount_oil * 0.15
            total = discount_oil + gst
            print(f'{oil_prices}, {oil_total}, {discount_oil}, {gst: .2f}, {total: .2f}')
        print('-'*60)
        print('Thanks for your business. Good Bye!')

    elif (oil_total < oil_max):
        if (prov == prov == prov == 'AB' or prov == 'BC' or prov == 'MB' or prov == 'NT' or prov == 'NU' or prov == 'QC' or prov == 'SK' or prov == 'YT'):
            gst = oil_total * 0.05
            total = oil_total + gst
            print(f'Product\t # of litres\t Price before discount\t Price after discount\t GST\t Total price\n Gas\t\t {oil_prices}\t\t\t {oil_total}\t\t\t {oil_total}\t\t\t {gst: .2f}\t\t\t {total: .2f}')
        
        elif prov == 'ON':
            gst = oil_total * 0.13
            total = oil_total + gst
            print(f'Product\t # of litres\t Price before discount\t Price after discount\t GST\t Total price\n Gas\t\t {oil_prices}\t\t\t {oil_total}\t\t\t {oil_total}\t\t\t {gst: .2f}\t\t\t {total: .2f}')
            
        else:
            gst = oil_total * 0.15
            total = oil_total + gst
            print(f'Product\t # of litres\t Price before discount\t Price after discount\t GST\t Total price\n Gas\t\t {oil_prices}\t\t\t {oil_total}\t\t\t {oil_total}\t\t\t {gst: .2f}\t\t\t {total: .2f}')
        print('-'*60)
        print('Thanks for your business. Good Bye!')
else:
    print('Invalid input, you should enter g/G or o/O')