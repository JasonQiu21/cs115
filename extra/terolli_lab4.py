def knapsack(cap, items: list):
    def helper1(l):
        '''
        sum up value
        '''
        if l == []:
            return 0
        return l[0][1] + helper1(l[1:])
    def helper2(l):
        '''
        sum up weight
        '''
        if l == []:
            return 0
        return l[0][0] + helper2(l[1:])
    def knapsack_(cap, items: list):
        '''
        See pdf for functionality.
        '''
        if items == []:
            return []
        use_it = [items[0]] + knapsack_(cap, items[1:])
        lose_it = knapsack_(cap, items[1:])

        # print(helper2(use_it))
        if helper1(use_it) > helper1(lose_it) and helper2(use_it)<cap:
            # print(use_it)
            return use_it
        else:
            # print(lose_it)
            return lose_it
        # return use_it if helper1(use_it) > helper1(lose_it) else lose_it
    return [helper1(knapsack_(cap, items)), knapsack_(cap, items)]

print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
print(knapsack(24, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
print(knapsack(20, []) )
print(knapsack(0, [[1, 1000], [2, 3000], [4, 55000]]))