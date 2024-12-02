def read_txt_file(f, l1, l2):
    with open(f, "r") as file:
        for line in file:
            p1, p2 = line.split()
            l1.append(p1)
            l2.append(p2)

    return [l1, l2]
            
def get_sum_dif(l1, l2, sum):
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        sum += abs(int(l1[i]) - int(l2[i]))
    return sum



list1 = []
list2 = []
sum = 0

lists = read_txt_file("data.txt", list1, list2)

l1, l2 = lists

print(get_sum_dif(l1, l2, sum))

