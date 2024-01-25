age = int(input("enter age: "))

try:
    if age <= 18:
        raise Exception("age")
    else:
        v_id = input("do u have voter id?\n y or n :")
        if v_id == "n":
            raise Exception("id")
        print("u r eligible to vote")
except Exception as e:

    if (str(e) == "age"):
        print("u r under aged")
    elif (str(e) == "id"):
        print("u r not eligible bcoz u don't have id")
    else:
        print("err occured")