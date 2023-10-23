class Bubble_Sort:

    def sort(self, list):
        count = 0
        while(count < len(list)):
            i = 0
            for j in range (1,len(list)):
                if list[i] > list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
                i += 1
            count += 1
        return list
    
b = Bubble_Sort()
list = [6,5,43,2,1]
# [5,6,2,1,43]
# [5,2,1,6,43]
# [2,1,5,6,43]
# [1,2,5,6,43]
print(b.sort(list))