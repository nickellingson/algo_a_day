def read_file(f):
    line_count = 0
    safe_count = 0
    with open(f, "r") as file:
        for line in file:
            line_count += 1
            line_list = line.split()
            safe_count += helper(line_list)
    return safe_count


def helper(line_list):
    print(line_list)
    left_pointer = 0
    right_pointer = 1
    
    while right_pointer <= len(line_list) - 1:

        difference_result = int(line_list[left_pointer]) - int(line_list[right_pointer])

        # 5 3 2 1
        # decreasing
        if difference_result > 0:
            while right_pointer <= len(line_list) - 1:
                difference_result = int(line_list[left_pointer]) - int(line_list[right_pointer])
                if difference_result > 0:
                    if difference_result <= 3 and difference_result >= 1:
                        left_pointer += 1
                        right_pointer += 1
                    else:
                        return 0
                else:
                    return 0

        # 1 3 5 6
        # increasing
        elif difference_result < 0:
            while right_pointer <= len(line_list) - 1:
                difference_result = int(line_list[left_pointer]) - int(line_list[right_pointer])
                if difference_result < 0:
                    if difference_result >= -3 and difference_result <= -1:
                        left_pointer += 1
                        right_pointer += 1
                    else:
                        return 0
                else:
                    return 0

        else:
            return 0
        
    return 1

            

print(read_file("data.txt"))