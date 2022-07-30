#This function makes sure that the user's input (year) is a leap year or not.
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

#This function takes True or False value that return the function is_leap and print whether It's a leap year or not
def message_leap(year):
    if year == True :
        print("It's a leap year")
    else:
        print("It isn't a leap year")

if __name__ == '__main__':
    year = int(input("What year would like to know if it's a leap year: ")) #Ask for user's input.
    is_leap(year) #Call function is_leap, this function take the user's input.
    message_leap(is_leap(year)) #Call function message_leap.

    
