

def decimal_to_binary(decimal):
    binary = ""
    binary_list = [128,64,32,16,8,4,2,1]
    
    for i in binary_list:
        if decimal >= i:
            decimal = decimal - i
            binary = binary + "1"
        else:
            binary = binary + "0"
        
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

