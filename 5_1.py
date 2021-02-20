with open("5_input") as file:
    info = file.read().strip().split('\n')

    def seatid_high(array):

        highid = 0

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

            if seatid > highid:
                highid = seatid

        return highid

seatid_high(info)
