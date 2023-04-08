print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

part_without_tip = total_bill / num_people
tip_value = (percentage_tip * total_bill) / (100 * num_people)
part_with_tip = round(part_without_tip + tip_value, 2)

print(f"Each person shoul pay: ${part_with_tip}")
