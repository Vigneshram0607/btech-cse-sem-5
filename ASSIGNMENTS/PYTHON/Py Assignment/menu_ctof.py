

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{round(fahrenheit,2)} Fahrenheit is : {round(celsius,2)} Celsius")


def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{round(celsius, 2)} Celsius is : {round(fahrenheit, 2)} Fahrenheit")


def main():
    while True:
        print("MENU: \n1.Fahrenheit to Celsius \n2.Celsius to Fahrenheit")
        menu = int(input("Enter Menu option: "))
        if menu == 1:
            fahrenheit_to_celsius()
        else:
            celsius_to_fahrenheit()
        if input("Do You Want to Continue [y/n]: ").lower() == 'n':
            print("\nBye!")
            break


if __name__ == '__main__':
    main()