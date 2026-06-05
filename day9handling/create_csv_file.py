import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

  
    writer.writerow(["Name", "Marks"])


    writer.writerow(["Naman", 85])
    writer.writerow(["Rahul", 90])

print("CSV file 'students.csv' created successfully!")
