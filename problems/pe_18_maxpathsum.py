# COMPLETE!!!


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

# new_data = """59
# 73 41
# 52 40 09
# 26 53 06 34
# 10 51 87 86 81
# 61 95 66 57 25 68
# 90 81 80 38 92 67 73
# 30 28 51 76 81 18 75 44
# 84 14 95 87 62 81 17 78 58
# 21 46 71 58 02 79 62 39 31 09
# 56 34 35 53 78 31 81 18 90 93 15"""

# print(tri_max_path(new_data))

# with open('../assets/pe_67_triangle.txt', 'r') as txt_data:
#     data = txt_data.read()
#     new = data.strip()
#     print(tri_max_path(data)) 



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