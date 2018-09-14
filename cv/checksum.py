def checksum(data):
    if type(data) == str and len(data) == 13:
        odd = data[0::2]
        even = data[1::2]
        oddsum =  0
        evensum = 0
        for i in odd:
            oddsum += int(i)

        for i in even:
            evensum += int(i)

        check = (10 - ((3 * evensum + oddsum) % 10 )) % 10
        print_check(check)


    else:
        raise ValueError('Wrong type of value or size')



def print_check(q):
    print(q)


if __name__ == '__main__':
    checksum('1234567890123')
