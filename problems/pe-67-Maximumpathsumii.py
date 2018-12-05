# COMPLETE

from pe_18_maxpathsum import tri_max_path as data_max


with open('../assets/pe_67_triangle.txt', 'r') as f:
    data = f.read()

    examine = data.strip()
    print(data_max(examine))
