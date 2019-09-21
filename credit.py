card_number = str(input("Number: "))
#card_number = str(378282246310005) ==> AMEX

valid = (sum([sum(int(j) for j in i) for i in map(list, map(str, [int(i)*2 for i in card_number[1::2]]))]) + sum(int(i) for i in card_number[::2])) % 10 == 0

if valid:
    if card_number[0] == "4":
        print("VISA")

    elif 51 <= int(card_number[0:2]) <= 55:
        print("MASTERCARD")

    elif card_number[0:2] in ["34", "37"]:
        print("AMEX")

    else:
        print("INVALID")

else:
    print("INVALID")
