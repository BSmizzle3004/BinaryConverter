

def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary

try:
    decimal = int(input("Enter a decimal number between 0 and 255: "))
    if 0 <= decimal <= 255:
        binary = decimal_to_binary(decimal)
        print(f"The binary representation of {decimal} is: {binary}")
    else:
        print("Please enter a valid decimal number between 0 and 255.")
except ValueError:
    print("Invalid input. Please enter a valid decimal number.")
