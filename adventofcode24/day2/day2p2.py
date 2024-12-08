def read_file(f):
    line_count = 0
    safe_count = 0
    with open(f, "r") as file:
        for line in file:
            line_count += 1
            line_list = line.split()
            # testing
            safety_check = helper(line_list)
            if safety_check == 1:
                print("safe")
            else:
                print("unsafe")
            #testing
            safe_count += safety_check
    return safe_count


def helper(line_list):

    unsafe_toleration_count = 0

    print(line_list)
    left_pointer = 0
    right_pointer = 1
    
    while right_pointer <= 1:

        # difference_result = int(line_list[left_pointer]) - int(line_list[right_pointer])
        # difference of first and last element in list
        difference_result = int(line_list[left_pointer]) - int(line_list[len(line_list) - 1])

        # Edge cases
        # 1 2 5 9 7
        # 1 2 5 9 4 

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
                        # return 0
                        unsafe_toleration_count += 1

                        # check for out of bounds
                        if right_pointer == len(line_list) - 1:
                            break

                        dif = int(line_list[left_pointer]) - int(line_list[right_pointer + 1])
                        if dif > 0:
                            if dif <= 3 and dif >= 1:
                                # check for out of bounds
                                if right_pointer == len(line_list) - 2:
                                    break

                                right_pointer += 1
                                left_pointer += 2
                            else:
                                unsafe_toleration_count += 1   
                                right_pointer += 1
                                break     
                        else:
                            right_pointer += 1
                            unsafe_toleration_count += 1
                            break


                else:
                    # return 0
                    unsafe_toleration_count += 1
                    left_pointer += 1
                    right_pointer += 1

        # Edge cases
        # 1 2 5 9 7 8
        # 1 2 5 9 4 6
        # 1 2 5 9 10 6
        # 1 3 5 7 14
        # 1 3 5 9 10

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
                        # return 0
                        unsafe_toleration_count += 1

                        # check for out of bounds
                        if right_pointer == len(line_list) - 1:
                            break

                        dif = int(line_list[left_pointer]) - int(line_list[right_pointer + 1])
                        if dif < 0:
                            if dif >= -3 and dif <= -1:
                                # check for out of bounds
                                if right_pointer == len(line_list) - 2:
                                    break

                                right_pointer += 1
                                left_pointer += 2
                            else:
                                unsafe_toleration_count += 1    
                                right_pointer += 1
                                break
                        else:
                            unsafe_toleration_count += 1
                            right_pointer += 1
                            break

                else:
                    # return 0
                    unsafe_toleration_count += 1
                    left_pointer += 1
                    right_pointer += 1

        # no difference, bad level
        else:
            # return 0
            unsafe_toleration_count += 1
            left_pointer += 1
            right_pointer += 1

        
    # return 1
    # check to see toleration of a single bad level
    if unsafe_toleration_count <= 1:
        return 1
    else:
        return 0


print(read_file('data.txt'))

#378 too low