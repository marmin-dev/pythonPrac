# Validating User Input
def user_choice():
    # Initial
    choice ="WRONG"
    acceptable_range = range(0,10)
    within_range = False
    # TWO CONDITION TO CHECK
    # DIGIT OR WITHIN_RANGE == FALSE
    while choice.isdigit() == False or within_range==False:
        choice = input("Please enter a number(0-10)")
        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not digit")
        # RANGE CHECK
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print("sorry you are out of acceptable range")
    return int(choice)
user_choice()
# result = 'Wrong Value'
# acceptable_values = [0,1,2]
# print(result in acceptable_values)
# val = '100'
# print(val.isdigit()) # validate to cast to integer
