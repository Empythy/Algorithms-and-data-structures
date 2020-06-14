from operator import attrgetter

# attrgetter 实际上内部调用了 getattr
"""
Return a callable object that fetches the given attribute(s) from its operand.
After f = attrgetter('name'), the call f(r) returns r.name.
After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
After h = attrgetter('name.first', 'name.last'), the call h(r) returns
(r.name.first, r.name.last)."""
f = attrgetter("name")
class Person():
    def __init__(self):
        self.name = "liuliang"
obj = Person()
print(f(obj))
