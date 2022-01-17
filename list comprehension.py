students =[100,80,70,90,60,50,40,30,20]
passed= [i if i>=50 else "Try better next time" for i in students]
print(passed)