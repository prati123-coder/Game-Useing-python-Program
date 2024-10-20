day_num = int(input("enter a number"))

match day_num:
    case 1:
        print("today is monday")
    case 2:
        print("today is tuesday")
    case 3:
        print("today is wednesday")
    case 4:
        print("today is thuresday")
    case 5:
        print("today is friday")
    case 6:
        print("today is saturday")
    case 7:
        print("today is sunday")
    case _ :
        print("Invalid day number")