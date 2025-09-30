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

# removing an item from our list 
my_list2.remove("Unix")
print("List after removing an item:", my_list2)
del my_list2[2]
print("List after deleting an item by index:", my_list2)


my_numerical_list = [ 1, 2, 4, 1, 2, 5, 6]
print(my_numerical_list.append(3))


print("List after appending an item:", my_numerical_list)

## sort a lit 

my_numerical_list.sort()
print("Sorted List:", my_numerical_list)

my_numerical_list.reverse()
print("Reversed List:", my_numerical_list)


# [6, 5, 4, 3, 2, 2, 1, 1]
for item in my_numerical_list:
    print(item)
    
    
## how to show the length of a list
print("Length of the list:", len(my_numerical_list))


# Concatenating Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

my_combined_list = list1 + list2
print("Combined List:", my_combined_list)

#Copying Lists
original_list = ["A", "B", "C"]
copied_list = original_list.copy()
print("Copied List:", copied_list)


another_copied_list = []
another_copied_list = another_copied_list + original_list
print("Another Copied List:", another_copied_list)



# A sample of power of lists in calculating the average of a list of numbers
sample_numbers = [10, 20, 30, 40, 50]
total = sum(sample_numbers) #150 
count = len(sample_numbers) #5
average = total / count
print("Average of the sample numbers:", average)


# list can contain different data types and can even include other lists (nested lists)   
mixed_list = [1, "Hello", 3.14, True, None, [1, 2, 3], [4,5], [6,7,8]]
print("Mixed List:", mixed_list)

print(type(mixed_list[5])) 
