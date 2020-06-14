from heapq import heapify, heappop, heappush, _heapify_max, _heappop_max

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
data_copy = data.copy()
heapify(data)                      # derrearrange the list into heap or
heappush(data, -5)                 # add a new entry
print([heappop(data) for i in range(3)])
# fetch the three smallest entries
_heapify_max(data_copy)
heappush(data_copy, 200)

print([_heappop_max(data_copy) for i in range(3)])





