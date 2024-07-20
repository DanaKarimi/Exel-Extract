# aval file ro dorost mikonim

file = open("./Exel_file.csv","a")

# tedad soton haro malom mikoni
add = 1
add = eval(input("If you want to add to file enter 0:\n(if you want to create new file enter 1)"))
number_of_column = eval(input("Enter the number of column:(if you want to add to file enter 0) "))
i = 0
while i< number_of_column and add != 0:
    i = i + 1
    column = input("Enter your "+ str(i) + " column: ")
    file.write(column + ",")

if add != 0:
    file.write("\n")
# dade haro be radif ha midim
row = str
i = 0
while True:
    row = input("Press enter for continue (Write close to stop.) ")
    if row == "close":
        break
    i = i + 1
    a = 0
    while a < number_of_column:
        a = a + 1
        row_column = input("Enter your "+ str(i)+ " row for "+ str(a) +" column: ")
        file.write(row_column + ",")
    file.write("\n")    

file.close()