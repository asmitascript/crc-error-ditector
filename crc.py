def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


def crc_division(dividend, divisor):
    pick = len(divisor)
    temp = dividend[0:pick]

    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp) + dividend[pick]
        pick += 1

    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)

    return temp


def generate_crc(data, divisor):
    appended_data = data + '0' * (len(divisor) - 1)
    remainder = crc_division(appended_data, divisor)
    codeword = data + remainder
    return remainder, codeword


def check_crc(received_data, divisor):
    remainder = crc_division(received_data, divisor)

    if set(remainder) == {'0'}:
        return True
    return False


# Main Program
print("===== CRC Error Detection Simulator =====")

data = input("Enter Data Bits: ")
divisor = input("Enter Generator Polynomial: ")

remainder, transmitted_data = generate_crc(data, divisor)

print("\nCRC Remainder :", remainder)
print("Transmitted Data :", transmitted_data)

received_data = input("\nEnter Received Data: ")

if check_crc(received_data, divisor):
    print("\nNo Error Detected!")
else:
    print("\nError Detected!")
