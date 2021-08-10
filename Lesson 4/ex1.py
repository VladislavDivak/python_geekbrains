from sys import argv

working_hours, rate_in_hours, premium = argv

print("Working hours: ", working_hours)
print("Hourly rate: ", rate_in_hours)
print("Premium: ", premium)
print("Final salary: ", (working_hours * rate_in_hours) + premium)