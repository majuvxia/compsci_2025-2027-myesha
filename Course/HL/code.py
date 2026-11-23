# Base Conversion Program
# Reads decimal numbers from decimals.txt
# Converts valid numbers into binary and hexadecimal
# Writes the results to results.txt


def decimal_to_binary(number):
    """Convert a decimal integer into binary without using bin()."""
    if number == 0:
        return "0"

    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    return binary


def decimal_to_hex(number):
    """Convert a decimal integer into hexadecimal without using hex()."""
    if number == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while number > 0:
        remainder = number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        number = number // 16
    return hexadecimal


def convert_number(value):
    """Check the input and convert it if it is valid."""
    try:
        number = int(value.strip())
        if number < 0:
            return "N/A", "N/A"
        return decimal_to_binary(number), decimal_to_hex(number)
    except (AttributeError, ValueError):
        return "N/A", "N/A"


def main():
    """Read decimal values, convert them, and write the results."""
    with open("decimals.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    with open("results.txt", "w", encoding="utf-8") as output_file:
        for line in lines:
            binary, hexadecimal = convert_number(line)
            output_file.write(f" {binary} | {hexadecimal} \n")

    print("Conversion completed successfully!")
    print("Results have been saved to results.txt")


if __name__ == "__main__":
    main()
