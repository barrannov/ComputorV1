import time

def count_root(value):
    precision = 0.000001
    res_root = 0.0
    while res_root * res_root < value:
        res_root += precision

    res_root -= precision

    return round(res_root, 12)

def op_count_root(value):
    dot = 0.000000000001

    precision = 1.0
    res_root = 0.0

    while precision > dot:
        while res_root * res_root < value:
            res_root += precision
        res_root -= precision
        precision /= 10

    return round(res_root, 12)



# def split_root(value=0.0):
#     div = 1.0
#     pos_root = value / div
#     while pos_root * pos_root > value:
#         pos_root = value / div
#         div += 1
#
#     return pos_root


# start_time = time.time()
# print(split_root(value=164.8))
# print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(op_count_root(value=1654354.8))
print("--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# print(count_root(value=164.8))
# print("--- %s seconds ---" % (time.time() - start_time))
