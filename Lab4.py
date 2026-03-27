user_data = {}
all_items = []

num_users = int(input("Enter number of users: "))

for i in range(num_users):
    username = input("Enter username: ")
    num_items = int(input("How many items? "))
    items = []
    for j in range(num_items):
        item = input(f"Item {j+1}: ")
        items.append(item)
    user_data[username] = items
    all_items.extend(items)

unique_items_pool = set(all_items)
item_counts = {}
for item in unique_items_pool:
    count = 0
    for items_list in user_data.values():
        if item in items_list:
            count += 1
    item_counts[item] = count

print("\nUSER DATA:")
for user, items in user_data.items():
    print(f"{user} -> {items}")

print("\nCOMMON ITEMS:")
for item, count in item_counts.items():
    if count > 1:
        print(item)

print("\nUNIQUE ITEMS:")
for item, count in item_counts.items():
    if count == 1:
        print(item)

print("\nMOST POPULAR ITEM:")
if item_counts:
    max_val = max(item_counts.values())
    for item, count in item_counts.items():
        if count == max_val:
            print(item)
