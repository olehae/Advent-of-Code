import collections as c
import itertools
import functools
import re

r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

V, F, D = set(), dict(), c.defaultdict(lambda: 1000)

for v, f, us in re.findall(r, open('input16.txt').read()):
    V.add(v)                         # store Valves
    if f != '0':
        F[v] = int(f)                # store flow per valve (if not zero)
    for u in us.split(', '):
        print(u)
        D[u, v] = 1                  # store distances (it is =1 for all valves in same line)


for k, i, j in itertools.product(V, V, V):     # floyd-warshall
    D[i, j] = min(D[i, j], D[i, k] + D[k, j])  # calculates minimum distances between two valves and stores them in dict

print(sorted(D.items()))


@functools.cache  # stores previous iteration results, making things more efficient
def search(time, u='AA', vs=frozenset(F), e=False):
    return max([F[v] * (time - D[u, v] - 1) + search(time - D[u, v] - 1, v, vs - {v}, e)
                for v in vs if D[u, v] < time] + [search(26, vs=vs) if e else 0])

# F[v] * (time - D[u, v] - 1) ->
# Flowrate * time left (time left = old time left - time it took to get to valve - time it took to open valve (1))

# search(time - D[u, v] - 1, v, vs - {v}, e) ->
# Recursive search with new time, current position (v) and valves that haven´t been visited yet (vs - {v})

# for v in vs if D[u, v] < time ->
# for every valve with value > 0 you can get to in the time left


print(f"Part 1: {search(30)}")
# print(f"Part 2: {search(26, e=True)}")
