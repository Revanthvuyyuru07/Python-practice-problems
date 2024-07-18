def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not Leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

is_leap_year(2000)