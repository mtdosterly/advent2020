with open("5_input") as file:
    info = file.read().strip().split('\n')

def seatid(array):

    myseat = 0

    def merge_sort(array):

        import sys

        if len(array) > 1:
            middle = len(array)//2
            left = array[:middle]
            right = array[middle:]

            merge_sort(left)
            merge_sort(right)

            left.append(sys.maxsize)
            right.append(sys.maxsize)

            x = y = 0

            for z in range(0,len(array)):
                if left[x] <= right[y]:
                    array[z] = left[x]
                    x += 1
                else:
                    array[z] = right[y]
                    y += 1

        return array

    seats = []

    for x in array:
        row = ''
        column = ''

        for y in x[:7]:
            if y == 'F':
                row += '0'
            else:
                row += '1'
        for z in x[7:10]:
            if z == 'L':
                column += '0'
            else:
                column += '1'

        seatid = (8 * int(row,2)) + int(column,2)

        seats.append(seatid)

    merge_sort(seats)

    for x in range(1,len(seats)-1):
        if seats[x+1] != seats[x]+1:
            myseat = seats[x]+1

    return myseat

seatid(info)
