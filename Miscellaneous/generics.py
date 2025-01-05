from collections import namedtuple, deque, Counter, defaultdict, OrderedDict, ChainMap

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# DEQUE:  A double ended queue...
dq = deque(['a', 'b', 'c'])
dq.append('d') # Add to right..
print(dq)
dq.appendleft('z')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
data = [1,2,3,4,51,1,2,3,"a"]
z= "acbbdsn"

# find frequency of each..
counter = Counter(z)
print(counter)
dd = defaultdict(int)
dd['a'] +=1
print(dd)
print(dd['z'])

#  ordered list: sorting based on keys of input order..
od = OrderedDict()
od['a'] = 1
od['c'] = 2
od['b'] = 3
print(od)

# chainMap:
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'd': 4}
chain = ChainMap(d1, d2)
print(chain['b'])
chain['c'] = 5
print(chain)
print(d1)

del chain['c']

print(chain)

# del chain['d']

print(chain)
chain['b'] = 5
print(chain)