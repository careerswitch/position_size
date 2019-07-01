#! usr/bin/env python3
'''shares.py by Ahmet Bolat, 2019-25-06
This script will calculate your position size.
'''

def main():
    equity = float(input('Enter your equity = '))
    price = float(input('Enter stock price = '))

    if price < float(5) and equity < float(2500):
        print('Max position size for under $5 / under $2500 equity = ' + str(int(equity * float(2) / price)))
    elif price < float(5) and equity > float(2500):
        print('Max position size for under $5 / over $2500 equity = ' + str(int(equity * float(2) / price)))
    elif price > float(5) and equity < float(2500):
        print('Max position size for over $5 / under $2500 equity = ' + str(int(equity * float(4) / price)))
    else:
        print('Max position size for over $5 / over $2500 equity = ' + str(int(equity * float(6) / price)))


if __name__ == '__main__':
    main()
