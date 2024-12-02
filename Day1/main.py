listA = []
listB = []

def read_input_file():
    #Funtion to extract the content of the input.txt file into two integer lists.
    try:
        with open('AdventOfCodeDay1/input.txt', mode = 'r') as my_file:
            line = my_file.readline()
            while line != "":
                split = line.split()
                listA.append(int(split[0]))
                listB.append(int(split[1]))
                line = my_file.readline()
    except FileNotFoundError as err:
        print('File does not exist')
        raise err

def compute_difference(list1, list2):
    difference_totalizer =0
    for num1, num2 in zip(list1, list2):
        difference_totalizer += abs(num1 - num2)
    return difference_totalizer

def element_occurance(list1, list2):
    occurance_counter_dict = {
        "elementListA": 0, 
        "occuranceListA": 0,
        "occuranceListB": 0
    }
    occurance_counter_list = []
    for num1 in list1:
        if occurance_counter_dict['elementListA'] != num1:
            occuranceListA = list1.count(num1)
            occuranceListB = list2.count(num1)
            occurance_counter_dict = dict(elementListA = num1, occuranceListA = occuranceListA, occuranceListB = occuranceListB)
            occurance_counter_list.append(occurance_counter_dict)
    return occurance_counter_list

read_input_file()
listA.sort()
listB.sort()

#######################################################
# Solution for Day 1, part 1
difference_totalizer = compute_difference(listA, listB)
print(f'The solution for Day 1 part 1 of the Advent calendar is: {difference_totalizer}')
#######################################################


#######################################################
# Solution for Day 1, part 2
#element_occurance is a list of dictionaries.
#It keeps tag of each individual element from listA and how many times it is found in listA and listB
element_occurance = element_occurance(listA, listB)
similarity_score = 0
for element in element_occurance:
    similarity_score += (element['elementListA'] * element['occuranceListA']) * element['occuranceListB']
print(f'The solution for Day 1 part 2 of the Advent calendar is: {similarity_score}')
#######################################################



