def main():
    #geeting input in fahrenheit
    degrees_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    #celcius conversion
    degrees_celsius = (degrees_fahrenheit -32) * (5/9)
    #output
    print(f"Temperature: \033[1m\033[3m{degrees_fahrenheit}F = {degrees_celsius}\033[0mC")

if __name__ == '__main__':
    main()