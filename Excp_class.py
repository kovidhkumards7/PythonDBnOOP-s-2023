class InvalidAge(Exception):
    pass

class VoterId(Exception):
    pass

age = int(input("enter age: "))

try:
    if age <= 18:
        raise InvalidAge
    else:
        v_id = input("do u have voter id?\n y or n :")
        if v_id == "n":
            raise VoterId
        print("u r eligible to vote")

except VoterId:
    print("u can't vote without id")

except InvalidAge:
    print("u r underaged")

