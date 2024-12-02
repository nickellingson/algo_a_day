def read_txt_file(f, l1, l2):
    with open(f, "r") as file:
        for line in file:
            p1, p2 = line.split()
            l1.append(p1)
            l2.append(p2)

    return [l1, l2]

def get_count(l2, l2_dict):
    for i in range(len(l2)):
        if l2[i] in l2_dict:
            l2_dict[l2[i]] += 1
        else:
            l2_dict[l2[i]] = 1

    return l2_dict

def calculate_simularity(l1, l2_dict, similarity_sum):
    for i in range(len(l1)):
        if l1[i] in l2_dict:
            similarity_sum += (int(l1[i]) * int(l2_dict[l1[i]]))
    return similarity_sum
            
list1 = []
list2 = []
similarity_sum = 0
l2_dict = {}

lists = read_txt_file("data.txt", list1, list2)

l1, l2 = lists

d = get_count(l2, l2_dict)
print(calculate_simularity(l1, d, similarity_sum))