from tabulate import tabulate

namesList = []
gradesList = []
lettersList = []

for x in range (0, 5):
	nameInput = input("Enter the name of the Student: ")
	enablingInput = input(f"Enter {nameInput}'s 5 Enabling Assessment grades separated by spaces: ")
	summativeInput = input(f"Enter {nameInput}'s 3 Summative Assessment grades separated by spaces: ")
	finalInput = int(input(f"Enter {nameInput}'s Final Examination grade: "))

	Enabling_list = enablingInput.split()
	for i in range(len(Enabling_list)):
		Enabling_list[i] = int(Enabling_list[i])
	for i in range(len(Enabling_list)):
		Enabling_list[i] = float(Enabling_list[i])

	Summative_list = summativeInput.split()
	for i in range(len(Summative_list)):
		Summative_list[i] = int(Summative_list[i])
	for i in range(len(Summative_list)):
		Summative_list[i] = float(Summative_list[i])

	enablingAverage= ((sum(Enabling_list)/5) * 0.3)
	summativeAverage = ((sum(Summative_list)/3) * 0.3)
	finalPart= finalInput * 0.4

	Grade = enablingAverage+summativeAverage+finalPart

	if Grade>=90:
		Letter = 'A'
	elif Grade>=80 and Grade<90:
		Letter = 'B' 
	elif Grade>=70 and Grade<80:
		Letter = 'C' 
	elif Grade>=60 and Grade<70:
		Letter = 'D' 
	else:
		Letter = 'F' 

	namesList.insert(x, nameInput)
	gradesList.insert(x, Grade)
	lettersList.insert(x, Letter)
	
print("\n")
table = {'Name': namesList, 'Grades': gradesList, 'Letter Grades': lettersList}
print(tabulate(table, headers='keys'))


