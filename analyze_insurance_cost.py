names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add a new patient named Priscilla with an associated insurance cost
names.append("Priscilla")
insurance_costs.append(8320.0)

# Create Medical Records combined list
medical_records = list(zip(names, insurance_costs))

# Store the number of records
num_medical_records = len(medical_records)
print("There are {} medical records.\n".format(num_medical_records))

# Save and print first record
first_medical_record = medical_records[0]
print("Here is the first medical record: {}\n".format(first_medical_record))

# Sort records by ascending cost
medical_records.sort(key = lambda record: record[1])
print("Here are the medical records sorted by insurance cost: {}\n".format(medical_records))

# Select and print the cheapest three costs
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: {}\n".format(cheapest_three))

# Select and print the costliest three costs
priciest_three = medical_records[:3]
print("Here are the three most expensive insurance costs in our medical records: {}\n".format(priciest_three))

# Count and print instances of "Paul"
occurrences_paul = names.count("Paul")
print("There are {} individuals with the name Paul in our medical records.\n".format(occurrences_paul))

# Sort medical records by name alphabetically
medical_records.sort(key = lambda record: record[0])
print(medical_records)
print("\n")

# Select the middle five records
middle_five_records = medical_records[3:8]
print(middle_five_records)
print("\n")

# Function analyze_smoker function
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Good work! Smoking is not an issue for you.")
    
# Function to analyze_bmi function
def analyze_bmi(bmi_value):
  key_bmi_values = [18.5, 25, 30]
  change_in_bmi_upper = round(abs(bmi_value - key_bmi_values[1]), 2)
  change_in_bmi_lower = round(abs(bmi_value - key_bmi_values[0]), 2)
  
  if bmi_value > key_bmi_values[2]:
    print("Your BMI of " + str(bmi_value) + " is in the obese range. To lower your cost and improve your health, you should significantly lower your BMI by " + str(change_in_bmi_upper) + " to " + str(change_in_bmi_lower) + " points.\n")
    
  elif key_bmi_values[1] <= bmi_value <= key_bmi_values[2]:
    print("Your BMI of " + str(bmi_value) + " is in the overweight range. To lower your cost and improve your health, you should lower your BMI by " + str(change_in_bmi_upper) + " to " + str(change_in_bmi_lower) + " points.\n")

  elif 18.5 <= bmi_value < 25:
    print("Great work! Your BMI is in a healthy range.")
  else:
    print("Your BMI of " + str(bmi_value) + " is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health. You should try to increase your BMI by " + str(change_in_bmi_lower) + " to " + str(change_in_bmi_upper) + " points.\n")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = round((250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500), 2)
  print(name + ", your Estimated Insurance Cost is $" + str(estimated_cost) + ".")
# Call smoker and bmi functions inside insurance cost function
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 37.5, num_of_children = 3, smoker = 1)

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names = ["Keanu", "Maria", "Rohan", "Valentina"]
insurance_costs = [33000.0, 4150.0, 5320.0, 35210.0]
estimated_insurance_costs = [keanu_insurance_cost, maria_insurance_cost, rohan_insurance_cost, valentina_insurance_cost]

insurance_data = list(zip(names, insurance_costs))
print("\nHere is the actual insurance cost data: " + str(insurance_data) + "\n")

estimated_insurance_data = list(zip(names, estimated_insurance_costs))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data)+"\n")

def calculate_insurance_cost_difference(actual_costs, estimated_costs):
  cost_differences = []
  for i in range(len(actual_costs)):
    j, k = estimated_costs[i]
    l, m = actual_costs[i]
    if k > m:
      print(j + "'s estimated insurance cost is " + str(k-m) + " higher than the actual cost.\n")
    elif k < m:
      print(j + "'s estimated insurance cost is " + str(m-k) + " lower than the actual cost.\n")
    else:
      print(j + "'s estimated cost is equal to their actual cost!\n")
    cost_differences.append(k-m)
  return cost_differences

calculate_insurance_cost_difference(insurance_data, estimated_insurance_data)
