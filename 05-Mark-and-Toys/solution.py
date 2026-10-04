def maximumToys(prices,k):
    prices.sort()

    total=0
    count=0

    for price in prices:
        if total+price>k:
            break
        total+=price
        count+=1

    return count
