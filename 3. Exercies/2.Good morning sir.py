import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if(hour>=5 and hour<12):
    print("Good morning sir!!")
elif(hour>=12 and hour<18):
    print("Good afternoon sir!!")    
elif(hour>=18 and hour<21):
    print("Good evening sir!!")    
else:
    print("Good night sir!!")    