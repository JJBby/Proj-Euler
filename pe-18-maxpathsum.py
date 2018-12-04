# COMPLETE!!!

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


def tri_max_path(the_data):
    tri_data = [[int(n) for n in line.split(" ")] for line in the_data.split("\n")]

    for l in range(len(tri_data)):
        test = len(tri_data)-1 - l
        for num in range(len(tri_data[test])):
        
            try:
                center = tri_data[test-1][num]
                left = tri_data[test][num]
                right = tri_data[test][num+1]
                x = center + left
                y = center + right

                if center + left >= center + right:
                    x1 = center + left
                    tri_data[test-1][num] += left
                    
                    # tri_data[center].update(x) = center + left
                else:
                    y1 = center + right
                    tri_data[test-1][num] += right

            except IndexError:
                pass

        # del data[test]
    return tri_data[0]

print(tri_max_path(data))







'''
TODO: STUDY THIS and refactor existing code!
SAMPLE CODE TO SAVE AND LOOK AT!
    Includes: 
        Lambda/anon function
        List comprehension x2


# for string in split_data:


# lines = data.split("\n")

# strings = map((lambda a_list: a_list.split()), lines)

# def map_int(a_list):return list(map(int, a_list))

# ints = list(map(map_int, strings))

# print(ints)



# lines = data.split("\n")

# def map_split_by_space(a_list): return a_list.split()

# def map_int(a_list):return list(map(int, a_list))

# strings = list(map(map_split_by_space, lines))
# ints = list(map(map_int, strings))

# print(ints)



triangle = """1
2 3
4 5 6
7 8 9 10"""

the_list = [[int(n) for n in line.split(" ")] for line in data.split("\n")]
print(the_list)

the_list = []
for line in triangle.split("\n"):
    inner_list = []
    for number in line.split(" "):
        inner_list.append(int(number))
    the_list.append(inner_list)
    

'''