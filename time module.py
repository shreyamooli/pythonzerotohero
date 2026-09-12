import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

if (time.strftime('%H')< '12'):
    print("Good Morning")
elif (time.strftime('%H') >='12'and time.strftime('%H') <='16'):
    print("Good Afternoon")
elif(time.strftime('%H')>= '16' and time.strftime('%H') <='20'):
    print("Good Evening")
else:
    print("Good Night")



