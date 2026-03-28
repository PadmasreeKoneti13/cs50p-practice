def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if 2 <= len(plate) <= 6 and plate.isalnum():
        if plate[0:2].isalpha():
            for i in range(len(plate)):
                if plate[i].isdigit():
                    if plate[i] == '0':
                        return False
                    if not plate[i:].isdigit():
                        return False
                    break

            return True
    return False

main()
