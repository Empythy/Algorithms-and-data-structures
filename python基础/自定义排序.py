import functools
import pprint
from operator import itemgetter
from operator import attrgetter

def cmp(a, b):
    if b < a:
        return -1
    if a < b:
        return 1
    return 0
a = [1, 2, 5, 4]
# print(sorted(a, key=functools.cmp_to_key(cmp)))
# [5, 4, 2, 1]
"""

"""

def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        __slots__ = ['obj']

        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        __hash__ = None

    return K
def test2():
    """方法2"""
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    def by_name(t):
        return t[0].lower()
    print(sorted([('Bob', 99), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=by_name))
    # [('Adam', 92), ('Bart', 66), ('Bob', 99), ('Lisa', 88)]

def test3():
    # 希望一个二维数组，先按第二列排序，再按第一列排序
    a = [[5, 3, 4], [6, 4, 5], [5, 3, 7], [5, 3, 6]]
    ret = sorted(a, key=lambda x: (x[1], x[0]))
    print(ret)
    # [[5, 3, 4], [5, 3, 7], [5, 3, 6], [6, 4, 5]]

# import random
# item1 = [random.randint(0,9) for _ in range(5)]
# # item2 = [random.randint(0,9) for _ in range(5)]
# # items = [[item1[i], item2[i]] for i in range(len(item1))]
a = [[5, 3, 4], [6, 4, 5], [5, 4, 7], [5, 3, 6]]
print(a)
# 先按第一列升序  第二列降序
ret = sorted(a, key=lambda x: (x[0], -x[1]))
print(ret)
#
# 对字典进行排序
phonebook = {'Linda':'7750',
             'Bob': '9345',
             'Carrol': '5834'}
ret = sorted(phonebook.items(), key=itemgetter(0))
print(ret)
mydict = {'Li':['M', 7],
          'Zhang': ['E', 2],
        'Wang':['P', 3],
          'Du':['C', 2],
          'Ma':['C', 9],
          'Zhe': ['H', 7]}
ret = sorted(mydict.items(), key=itemgetter(1))
print(ret)
# """List中混合字典排序
#
#
# """
# from operator import attrgetter
# 如果类表中每个元素为字典形式，需要针对字典多个key进行排序
gameresult = [
    {"name":"liuliang", "wins":10,"losses:":3,  "rating":75},
    {"name": "lilei", "wins": 3, "losses:": 5, "rating": 57},
    {"name": "yuwei", "wins": 9, "losses:": 2, "rating": 71},
    {"name": "limeimei", "wins": 9, "losses:": 2, "rating": 71}
]
ret = sorted(gameresult, key=itemgetter('rating', 'name'))
pprint.pprint(ret)

ret = sorted(gameresult, key=lambda x:(-x['rating'], x['name']))
pprint.pprint(ret)
# [{'losses:': 3, 'name': 'liuliang', 'rating': 75, 'wins': 10},
#  {'losses:': 2, 'name': 'limeimei', 'rating': 71, 'wins': 9},
#  {'losses:': 2, 'name': 'yuwei', 'rating': 71, 'wins': 9},
#  {'losses:': 5, 'name': 'lilei', 'rating': 57, 'wins': 3}]
"""operator.itemgetter  Class
    Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2].
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
"""

""" operator.attrgetter
 Return a callable object that fetches the given attribute(s) from its operand.
    After f = attrgetter('name'), the call f(r) returns r.name.
    After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
    After h = attrgetter('name.first', 'name.last'), the call h(r) returns
    (r.name.first, r.name.last).
"""

