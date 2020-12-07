name = input("Victim Name: ")
city  = input("Victim Born Town/City: ")

newfilename = "generatedpasswords.txt"
output_file = open(newfilename,"x+")

for a in range(0, 100):
	passname = (name + str(a))
	passcity = (city + str(a))
	print(passname)
	print(passcity)
	output_file.write(passname +'\n')
	output_file.write(passcity +'\n')

for a in range(1900, 2020):
	yearname = (name + str(a))
	yearcity = (city + str(a))
	print(yearname)
	print(yearcity)
	output_file.write(yearname +'\n')
	output_file.write(yearcity +'\n')


output_file.write(newfilename)