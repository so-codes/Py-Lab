# create a list to store the max and min temperature of city ( major 5 cities in india ) accept the input from user. display in ascending order

temp_min = []
for i in range(5):
    print("Enter the name of the city - min temperature of city: ")
    ans = input().split("-")
    temp_min.append(int(ans[1]))
print(temp_min)

temp_min.sort()
print("The sorted list is: ", temp_min)

temp_max = []
for i in range(5):
    print("Enter the name of the city - max temperature of city: ")
    ans = input().split("-")
    temp_max.append(int(ans[1]))
print(temp_max)

temp_max.sort()
print("The sorted list is: ", temp_max)

temp = []
for i in range(5):
    temp.append(temp_min[i])
    temp.append(temp_max[i])
print(temp)
temp.sort()
print("The sorted list is: ", temp)
