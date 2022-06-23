decimal_to_hex_map = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f"
}

binary_to_hex_map = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "a",
    "1011": "b",
    "1100": "c",
    "1101": "d",
    "1110": "e",
    "1111": "f"
}

hex_to_decimal_map ={
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
}

hex_to_binary_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"
}

def decimal_to_binary(decimal_number: str):
    decimal_temp = int(decimal_number)
    binary_digits = []
    binary_number = ""

    while decimal_temp > 0:
        binary_digits.append(decimal_temp % 2)
        decimal_temp //= 2

    binary_digits.reverse() # reverse() method does not return list, it alters list

    for digit in binary_digits:
        binary_number += str(digit)

    return binary_number

def decimal_to_hexadecimal(decimal_number: str):
    decimal_temp = int(decimal_number)
    hex_digits = []
    hex_number = ""

    while decimal_temp > 0:
        hex_digits.append(decimal_temp % 16)
        decimal_temp //= 16

    hex_digits.reverse() # reverse() method does not return list, it alters list

    for digit in hex_digits:
        hex_number += decimal_to_hex_map[digit]

    return hex_number

def binary_to_decimal(binary_number: str):
    binary_temp = binary_number[::-1] # string reversal using list slice necessary to start from rightmost digit
    decimal_number = 0
    digit_incrementer = 0

    for digit in binary_temp:
        if digit != "0" and digit != "1":
            raise ValueError("Number must be in binary")
        else:
            decimal_number += int(digit) * 2 ** digit_incrementer
            digit_incrementer += 1

    return decimal_number

def binary_to_hexadecimal(binary_number: str):
    original_digits = ""
    extra_digits = len(binary_number) % 4
    digit_counter = 0
    
    if extra_digits > 0:
        for _ in range(4 - extra_digits):
            original_digits += "0"
            digit_counter += 1

    for digit in binary_number:
        if digit_counter == 4:
            original_digits += " "
            digit_counter = 0
        
        if digit != "0" and digit != "1":
            raise ValueError("Number must be in binary")
        else:
            original_digits += digit
            digit_counter += 1
        
    binary_temp = original_digits.split(" ")

    hex_number = ""
    for temp in binary_temp:
        hex_number += binary_to_hex_map[temp]

    return hex_number

def hexadecimal_to_decimal(hex_number: str):
    hex_temp = hex_number[::-1] # string reversal using list slice necessary to start from rightmost digit
    decimal_number = 0
    digit_incrementer = 1

    for digit in hex_temp:
        decimal_number += hex_to_decimal_map[digit] * digit_incrementer
        digit_incrementer *= 16

    return decimal_number

def hexadecimal_to_binary(hex_number: str):
    if hex_number == "0":
        return "0"

    binary_temp = ""

    for digit in hex_number:
        binary_temp += hex_to_binary_map[digit]

    binary_number = binary_temp.lstrip("0")

    return binary_number

def main():
    print("(1) Convert decimal to binary\n(2) Convert decimal to hexadecimal\n(3) Convert binary to decimal\n(4) Convert binary to hexadecimal\n(5) Convert hexadecimal to decimal\n(6) Convert hexadecimal to binary\n(7) Exit\n")
    exit = False
    while not exit:
        selection = input("Selection: ")
        if selection == "1":
            decimal_number = input("Number: ")
            print("Result: " + decimal_to_binary(decimal_number) + "\n")
        elif selection == "2":
            decimal_number = input("Number: ")
            print("Result: " + decimal_to_hexadecimal(decimal_number) + "\n")
        elif selection == "3":
            binary_number = input("Number: ")
            try:
                print("Result: " + str(binary_to_decimal(binary_number)) + "\n")
            except ValueError as e:
                print(e + "\n")
        elif selection == "4":
            binary_number = input("Number: ")
            try:
                print("Result: " + binary_to_hexadecimal(binary_number) + "\n")
            except ValueError as e:
                print(e + "\n")
        elif selection == "5":
            hex_number = input("Number: ")
            print("Result: " + str(hexadecimal_to_decimal(hex_number)) + "\n")
        elif selection == "6":
            hex_number = input("Number: ")
            print("Result: " + hexadecimal_to_binary(hex_number) + "\n")
        elif selection == "7":
            exit = True
        else:
            print("Not a valid selection\n")
            continue
