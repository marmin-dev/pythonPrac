grade = [80, 75, 55]
print(sum(grade))
print(sum(grade)/len(grade))

a= "881120-1068234"
def gender_check(st):
    if type(st) == "<class 'int'>":
        str(st)
    print(st)
    if st[7] == "1" or st[7] == "3":
        print("male")
    elif st[7] == "2" or st[7] == "4":
        print("female")
    else:
        print("주민번호 치라고")
gender_check(a)
