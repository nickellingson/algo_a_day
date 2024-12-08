def read_line(file):
    with open(file, "r") as f:
        answer = 0
        for line in f:
            line_list = list(line)
            answer += helper(line_list)
    return answer


def helper(line_list):
    correct_list = ['m', 'u', 'l', '(', '1',',', '1', ')']
    do_list = ['d', 'o', '(', ')']
    do_index = 0
    dont_list = ['d', 'o', 'n', '\'', 't', '(', ')']
    dont_index = 0
    index = 0
    total = 0
    do = True
    while index <= len(line_list) - 1:
        if line_list[index] == "m":
            multiplier1 = ""
            multiplier2 = ""
            correct_list_index = 0
            multiply_and_addem_up = True
            while correct_list_index <= len(correct_list) - 1:
                if correct_list_index != 4 and correct_list_index != 6:
                    if correct_list[correct_list_index] == do_list[do_index]:
                        do_index += 1
                    if correct_list[correct_list_index] == line_list[index]:
                        index += 1
                        correct_list_index += 1
                    else:
                        multiply_and_addem_up = False
                        break
                else:
                    count = 0
                    while count <= 3:
                        if line_list[index] != "," and line_list[index] != ")":
                            if line_list[index].isnumeric():
                                if correct_list_index == 4:
                                    multiplier1 += line_list[index]
                                    index += 1
                                    count += 1
                                else:
                                    multiplier2 += line_list[index]
                                    index += 1
                                    count += 1
                            else:
                                multiply_and_addem_up = False
                                break
                        else:
                            break
                    correct_list_index += 1

            if multiply_and_addem_up:
                total += (int(multiplier1) * int(multiplier2))
        else:
            index += 1

    return total



print(read_line("data.txt"))