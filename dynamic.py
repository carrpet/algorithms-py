def maximumToys(prices, k):
    table = [[0 for x in range(k + 1)]]
    for x in range(len(prices)):
        table.append([0 if y == 0 else None for y in range(k + 1)])
    print(table)
