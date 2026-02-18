###################################################################################################
# Create a simple triangle function: given an arbitrary string, loop thru chars,
# printing line of successive substrings from left to right, increasing in length, creating a
# triangle pattern.  if final line is not long enough, pad with &#39;*&#39;
#  Example:
# triangle(&#39;abcd&#39;) outputs:
# a
# bc
# d**
##################################################################################################
def build_triangle_using_function(input_str):
    if len(input_str) == 0:
        return
    
    output = []

    total_row_count = 1
    cur_row_count = 1
    cur_row = ''

    # Compute each row by keeping track of row count
    for char in input_str:
        if cur_row_count == 0:
            output.append(cur_row)
            cur_row = ''
            total_row_count += 1
            cur_row_count = total_row_count

        cur_row += char
        cur_row_count -= 1

    # Compute and add last row
    if len(cur_row) < total_row_count:
        cur_row = cur_row + '*'*(total_row_count-len(cur_row))
    output.append(cur_row)

    # Print all rows
    for row in output:
        print(row)

build_triangle_using_function('')
print('--------')
build_triangle_using_function('a')
print('--------')
build_triangle_using_function('ab')
print('--------')
build_triangle_using_function('abc')
print('--------')
build_triangle_using_function('abcd')
print('--------')
build_triangle_using_function('abcde')
print('--------')
build_triangle_using_function('abcdef')
print('--------')
build_triangle_using_function('abcdefh')
print('--------')
build_triangle_using_function('abcdessdsfsdfadsafsdfadfasdfasdfasdfasfasdfasdfadsfasdfasfdasfdasdfasdfafh')