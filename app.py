dic = {}

while(True):
	user = input("enter student name(or done to stop): ")
	if(user.lower() == "done"):
		break
	else:
		try:
			marks = int(input("enter marks: "))
		except:
			print("invalid input try again")
			continue
			
		dic[user] = marks
		
lst = list(dic.values())

if len(lst)==0:
	print("no data entered")
else:
	ave = sum(lst)/len(lst)
	maximum = max(lst)
	minimum = min(lst)

	print(dic)
	print("Average: ",ave)
	print("Minimum: ",minimum)
	print("Maximum: ",maximum)
	print("")

	if ave >= 50:
		print("class outcome: Pass ")
	else:
		print("class outcome: fail ")

	top_student = max(dic, key=dic.get)
	print("top student: ", top_student)
