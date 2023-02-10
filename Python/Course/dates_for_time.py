# if input is 0 print Tuesday
# if input is -11 or less print Monday
# if input is 14 or more print Wednesday

offset = int(input()) # input offset
               
if offset <= -11:
    print("Monday")
elif offset >= 14:
    print("Wednesday")
else:
    print("Tuesday")
