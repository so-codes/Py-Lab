# create a list to store the max and min temperature of city ( major 5 cities in india ) accept the input from user. display in ascending order

temp = []
for i in range(5):
    print("Enter the name of the city - temperature of city: ")
    ans = input().split("-")
    temp.append(int(ans[1]))
print(temp)

temp.sort()
print("The sorted list is: ", temp)