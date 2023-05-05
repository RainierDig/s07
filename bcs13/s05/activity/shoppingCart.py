i = 0
addAnother = "a"
total = 0
while i == 0:
	item = input("Please enter the name of the item: ")

	try:
		price = float(input("Please enter the price of the item: "))
		if price <= 0:
			print("Positive numbers only")
			continue
		elif price > 0:
			total+=price

	except ValueError:
		print("Invalid Input, numbers only")
		print("")
		continue

	print(item, " was added to your shopping cart." ,sep="")
	print("")

	while addAnother != "n" or addAnother != "y":

		addAnother = input("Do you want to add another item? (y/n) ")
		addAnother.lower()

		if addAnother == "n":
			print("")
			roundedTotal=format(total,".2f")
			print("Thank you for shopping with us! Your total cost is $", roundedTotal, sep="")
			break
		elif addAnother == "y":
			break
		else:
			print("invalid input, y or n only")
			print("")

	if addAnother == "n":
		break
			
