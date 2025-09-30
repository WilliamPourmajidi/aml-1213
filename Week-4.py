my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

print("Original List:", my_list)

## accessing elements using index of the items in the list
print("1st element: ", my_list[0])
print("2nd element: ", my_list[1])
print("3rd element: ", my_list[2])
print("4th element: ", my_list[3])
print("5th element: ", my_list[4])

## Slicing the list using index
print("Elements from index 1 to 3: ", my_list[1:3])

# first index is inclusive and the last index is exclusive
# say we are interested to list all the values from Cherry to Fig
print("Elements from index 2 to 5: ", my_list[2:6])


my_list2 = ["Windows 10", "Unix", "Ubuntu", "Kali Linux", "MacOS", "Fedora", "Red Hat"]

print("Original List:", my_list2)

my_list2[0] = "Windows 11"

print("Updated List:", my_list2)


