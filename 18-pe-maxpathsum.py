# TODO!!!

data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# new = data.replace(" ", ",")
# what = data.split("\n")
# test = map(int, data.split())
# final = [int(x) for x in new.split('\n')]
# for n in data:
#     print(n)
#     if n == "\"":
#         new += data.replace('\"', '')


# # Split and create new list at \n as int
# new_data = list(map(int, data.split()))

# # Transform this data in a list of numbers
# clean = [x for x in data.split("\n")]

# tri = [[]]

# print(new_data)






# Get length of lists
# Start one from the last, e.g. if 5 lists, start at list 4
# Associate the current list to the list below it to add the 2 numbers below it. 
# Modify current list to highest value
# remove last list from the data once highest values are saved
desired_data = [
    [75], 
    [95, 64], 
    [17, 47, 82], 
    [18, 35, 87, 10]
]

for l in range(len(desired_data)):
    for num in range(len(desired_data[l])):

    center = desired_data[len(desired_data) - 1][l]
    left = desired_data[len(desired_data)][l]
    right = desired_data[len(desired_data)][l+1]

        if center + left >= center + right:
            center = center + left
        else:
            center = center + right