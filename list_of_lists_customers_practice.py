# Define initial customer information
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
expedited_shipping = [True, False, True, False]
preferred_size.append("Medium")


# Write a function to create a list of lists of all customer data
def create_customer_data(names, sizes, shipping):
  i = 0
  customer_data = []
  while i in range(len(names)):  
    customer = [names[i]]
    customer.append(sizes[i])
    customer.append(shipping[i])
    customer_data.append(customer)
    i+=1
  return customer_data

# Create initial customer data using the function above  
customer_data = create_customer_data(first_names, preferred_size, expedited_shipping)

# Make adjustments to the original dataset using 2-dimensional indexing
customer_data[2][2] = False
customer_data[1].remove(customer_data[1][2])

# Add 2 new customers to the dataset
new_customers = [["Amit", "Large", True], ["Karim", "X-Large", False]]

customer_data_final = customer_data + new_customers

# Examine the final dataset
print(customer_data_final)
