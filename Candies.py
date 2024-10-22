def kidswithcandies(candies,extraCandies):
    x= []
    for i in candies:
        if i+extraCandies >= max(candies):
            x.append(True)
        else:
            x.append(False)
    return x




candies = [2,3,5,1,3]
extraCandies = 3

print(kidswithcandies(candies,extraCandies))