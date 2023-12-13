# create a dictionary to store the price of sports items
# accept one new key value pair from user and add the new key value pair to the existing dictionay
# display the name of the higst priced sports items in the dictionary

items = {"cricket bat": 1000, "cricket ball": 100, "football": 500, "basketball": 300, "tennis racket": 200, "tennis ball": 50}
print(items)

# accept one new key value pair from user and add the new key value pair to the existing dictionay
new_item = input("Enter the name of the new item: ")
new_price = int(input("Enter the price of the new item: "))
items[new_item] = new_price
print(items)

# display the name of the higst priced sports items in the dictionary
max_price = max(items.values())
print(max_price)
for item, price in items.items():
    if price == max_price:
        print(item)
