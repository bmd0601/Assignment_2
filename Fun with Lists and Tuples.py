#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Take input from the user

lst = []
n = int(input("Enter the number of tuples: "))
print("Enter the tuples in the format (x, y): ")
for i in range(n):
    tuple_input = input()
    tuple_values = tuple(map(int, tuple_input.strip('()').split(',')))
    lst.append(tuple_values)

# Sort the list 
sorted_list = sorted(lst, key=lambda x: x[-1])

# Print the sorted list
print("Sorted List in increasing order:", sorted_list)
#---------------------------------------------------------------------------------
#Output:
#[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#---------------------------------------------------------------------------------