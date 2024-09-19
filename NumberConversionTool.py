# Variable for match case of the original number type
Original = input("What type of number would you like to input? (Hexadecimal, Decimal, Binary, Octal): ")

# Variable to input the original number
if Original == "Hexadecimal":
    Hex = input("Enter the number you want: ")
else:
    Num = input("Enter the number you want: ")
    Num = int(Num)

# Variable for the match case of the output number type
Tipo = input("What type of number would you like to convert to? (Binary, Octal, Decimal, Hexadecimal): ")

#///DECIMAL///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Decimal to Binary
def Decimal_Binary(Num):
    List = []
    while Num > 0:
        Res = Num % 2
        List.insert(0, Res)
        Num = Num // 2
    Numstr = " "
    for i in List:
        Numstr = Numstr + str(i)
    return Numstr

# Decimal to Hexadecimal
def Decimal_Hex(Num):
    list = []
    while Num > 0:
        Residue = Num % 16
        Variable = Residue
        if Residue == 10:
            Variable = "A"
        elif Residue == 11:
            Variable = "B"
        elif Residue == 12:
            Variable = "C"
        elif Residue == 13:
            Variable = "D"
        elif Residue == 14:
            Variable = "E"
        elif Residue == 15:
            Variable = "F"
            
        list.insert(0, str(Variable))
        Num //= 16
    Numstr = ''
    for i in list:
        Numstr += str(i)
    return Numstr

# Decimal to Octal
def Decimal_Octal(Num):
    Octal = ""
    while Num > 0:
        Residue = Num % 8
        Octal = str(Residue) + Octal
        Num = int(Num / 8)
    return Octal

#///OCTAL///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Octal to Decimal
def Octal_Decimal(Num):
    dec = 0
    i = 0
    while Num > 0:
        if Num == 8:
            print("Error")
        else:
            Residue = Num % 10
            exp = Residue * (8 ** i)
            dec += exp
            Num //= 10
            i += 1
    return dec

# Octal to Binary
def Octal_Binary(Num):
    return 0

# Octal to Hexadecimal
def Octal_Hex(Num):
    return 0

#///HEXADECIMAL///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Hexadecimal to Binary
def Hex_Binary(Hex):
    return 0

# Hexadecimal to Decimal
def Hex_Decimal(Hex):
    list = []

    for i in Hex:
        if i == "A":
            v = 10
        elif i == "B":
            v = 11
        elif i == "C":
            v = 12   
        elif i == "D":
            v = 13
        elif i == "E":
            v = 14
        elif i == "F":
            v = 15
        else:
            v = int(i)
        list = list + [v]
    n = len(list) - 1
    dec = 0

    for i in range(len(list)):
        dec = dec + list[i] * 16 ** (n - i)
    return dec

# Hexadecimal to Octal
def Hex_Octal(Hex):
    return 0

#///BINARY/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Binary to Decimal
def Binary_Decimal(Num):
    dec = 0
    i = 0
    while Num > 0:
        Residue = Num % 10
        exp = Residue * (2 ** i)  # exp is the exponent operator
        dec += exp
        Num //= 10
        i += 1
    return dec

# Binary to Octal
def Binary_Octal(Num):
    Equivalents = [0, 1, 10, 11, 100, 101, 110, 111]
    List = []
    while Num != 0:
        reminder = Num % 1000
        List.append(Equivalents.index(reminder))
        Num = Num // 1000
    List.reverse()
    Ostr = ""
    for i in List:
        Ostr = Ostr + str(i)
    return Ostr

# Binary to Hexadecimal
def Binary_Hex(Num):
    return 0

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

match Original:
    case "Decimal":   
        if Tipo == "Binary":
            print(f"The binary conversion is: {Decimal_Binary(Num)}")
        elif Tipo == "Octal":
            print(f"The octal conversion is: {Decimal_Octal(Num)}")
        elif Tipo == "Hexadecimal":
            print(f"The hexadecimal conversion is: {Decimal_Hex(Num)}")
    case "Binary":
        if Tipo == "Decimal":
            print(f"The decimal conversion is: {Binary_Decimal(Num)}")
        elif Tipo == "Octal":
            print(f"The octal conversion is: {Binary_Octal(Num)}")
        elif Tipo == "Hexadecimal":
            print(f"The hexadecimal conversion is: {Binary_Hex(Num)}")
    case "Octal":
        if Tipo == "Decimal":
            print(f"The decimal conversion is: {Octal_Decimal(Num)}")
        elif Tipo == "Binary":
            print(f"The binary conversion is: {Octal_Binary(Num)}")
        elif Tipo == "Hexadecimal":
            print(f"The hexadecimal conversion is: {Octal_Hex(Num)}")
    case "Hexadecimal":
        if Tipo == "Decimal":
            print(f"The decimal conversion is: {Hex_Decimal(Hex)}")
        elif Tipo == "Octal":
            print(f"The octal conversion is: {Hex_Octal(Hex)}")
        elif Tipo == "Binary":
            print(f"The binary conversion is: {Hex_Binary(Hex)}")
