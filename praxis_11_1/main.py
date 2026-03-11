# def iterate(x0, m):
#     x = x0
#     while True:
#         yield x
#         x *= m
#
#
# # for n in iterate(1, 1.2):
# #     print(n)
# #     if n > 3:
# #         break
#
# if __name__ == '__main__':
#     # tests
#     i = iterate(1, 1.2)
#     assert(next(i)) == 1
#     assert(next(i)) == 1.2
#     assert(next(i)) == 1.44
#     assert(next(i)) == 1.728

def filter_orders_by_cost(file_iter, cost):
    row_head = next(file_iter)   #"client_id, order_id, order_cost"

    print(row_head)


if __name__ == '__main__':
    with open("orders.csv", "r") as f:
        result = filter_orders_by_cost(f, 20)

    print(result)

