# Create initial list of inventory
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Explore inventory using functions like length, indexing, slicing, range, and sorting
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory.sort()
print(inventory)
print("\n")

# Create a list of unique items and the number of items in inventory
removed_items = []
inventory_counts = []
for i in inventory:
  if i not in removed_items:
    removed_items.append((i))
    inventory_counts.append((i, inventory.count(i)))
inventory_counts.sort(reverse=True)
print(inventory_counts)
