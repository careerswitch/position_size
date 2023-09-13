def calculate_position_size(equity, price):
    if price < 5 and equity < 2500:
        return int(equity * 2 / price)
    elif price < 5 and equity >= 2500:
        return int(equity * 2 / price)
    elif price >= 5 and equity < 2500:
        return int(equity * 4 / price)
    else:
        return int(equity * 6 / price)


def main():
    while True:
        try:
            equity = float(input('Enter your equity: $'))
            price = float(input('Enter stock price: $'))

            if equity < 0 or price < 0:
                print("Both equity and price must be non-negative values.")
            else:
                position_size = calculate_position_size(equity, price)
                print(f'Max position size: {position_size} shares')

            response = input("Do you want to calculate again? (yes/no): ").strip().lower()
            if response != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter valid numeric values for equity and stock price.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    main()
