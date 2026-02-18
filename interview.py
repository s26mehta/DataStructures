# Rectangular map
# Elements can be 1 or 0
# 1 is land and 0 is water
# connected 1s are basically continents
# Question: Find the total number of such continents
# parameter is map


map = [[ 0, 0, 0, 0 ],
       [ 0, 0, 0, 0 ],
       [ 0, 0, 0, 0 ]]


def find_total_number_of_continents(map):
    number_of_continents = 0

    for row_idx, row in enumerate(map):
        for column_idx, column in enumerate(row):
            if map[row_idx][column_idx] == 1:
                dfs(column_idx, row_idx, map)
                number_of_continents += 1
    return number_of_continents

def dfs(x_value, y_value, map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    map[y_value][x_value] = 0
    for dir in directions:
        if x_value + dir[0] < 0 or x_value + dir[0] > len(map[0])-1 :
            continue
        if y_value + dir[1] < 0 or y_value + dir[1] > len(map)-1:
            continue
        row = y_value + dir[1]
        col = x_value + dir[0]
        if map[row][col] == 1:
            dfs(col, row, map)

print("Total number of continents is: " + str(find_total_number_of_continents(map)))