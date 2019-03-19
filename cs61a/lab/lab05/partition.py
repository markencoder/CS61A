def partition_options(total, biggest_num):
    if total == 0:
        return [[]]
    elif total < 0 or biggest_num == 0:
        return []
    else:
        with_biggest=partition_options(total- biggest_num, biggest_num)
        without_biggest=partition_options(total, biggest_num - 1)
        return sum([[biggest_num,[with_biggest, without_biggest]]],[])
