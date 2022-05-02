def queue_time(customers, n):
    count = 0

    while len(customers) != 0:
        for i in range(min(n, len(customers))):
            customers[i] -= 1

        customers = list(filter(lambda cus: cus != 0, customers))
        count += 1

    return count


def queue_time_best(customers, n):
    l = [0] * n
    for i in customers:
        l[l.index(min(l))] += i
        print(l)
    return max(l)


# print(queue_time([5, 2], 1))
print(queue_time([2, 3, 2, 10], 2))
# print(queue_time([2, 10, 3, 2], 3))
# print(queue_time([5, 0, 2, 0, 4], 1))
