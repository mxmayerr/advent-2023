# Advent of Code 2023 day 9
# 12/13/2023
# Author: Max Mayer

# function to get the next line of history
def get_next_list(lst):
    # gets a list of the differences of the elements of the list
    return [lst[i+1] - lst[i] for i in range(len(lst)-1)]

# read the file
with open("day09.txt", "r") as f:
    data = f.read().splitlines()
    histories = []
    for lst in data:
        lst = [int(i) for i in lst.split(" ")]
        histories.append(lst)


# ----- PART 1 -----
# initialize count
count = 0

# for every line in histories
for line in histories:
    # get the list of sequences
    sequences = []
    sequences.append(line)
    next_list = get_next_list(line)
    # while the list isnt all zeros (ending case), get the next list
    while not all(val == 0 for val in next_list):
        sequences.append(next_list)
        next_list = get_next_list(next_list)

    # append the ending case
    sequences.append(next_list)

    # now that we have the sequences, we need to get the next number for each row
    for i in range(len(sequences)-1, 0, -1):
        # get the current and next value (based on the values next to it)
        val = sequences[i][-1]
        next_val = sequences[i-1][-1] + val
        sequences[i-1].append(next_val)

    # add the last 0 to the last sequence
    sequences[-1].append(0)

    # add the new "predicted" value to the count
    count += sequences[0][-1]

# show the answer
print("Part 1 answer: " + str(count))

# ----- PART 2 -----
# same thing, but the front instead of the back

count2 = 0

for line in histories:
    sequences = []
    sequences.append(line)
    next_list = get_next_list(line)
    while not all(val == 0 for val in next_list):
        sequences.append(next_list)
        next_list = get_next_list(next_list)

    sequences.append(next_list)

    for i in range(len(sequences)-1, 0, -1):
        val = sequences[i][0]
        next_val = sequences[i-1][0] - val
        sequences[i-1].insert(0, next_val)

    sequences[-1].insert(0, 0)

    count2 += sequences[0][0]

print("Part 2 answer: " + str(count2))


