
def is_leap(year):
    leap= False
    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return leap
    if year % 4 == 0:
        return True
    else:
        return False
    
    return leap

def message_leap(year):
    if year == True :
        print("It's a leap year")
    else:
        print("It isn't a leap year")

if __name__ == '__main__':
    year = int(input("What year would like to know if it's a leap year: "))
    is_leap(year)
    message_leap(is_leap(year))

    
