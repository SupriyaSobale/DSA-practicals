class Set:
    def __init__(self, data=None):
        self.data = {}
        if data != None: 
            if len(data) != len(set(data)):
                data = set(data)
            for d in data:
                self.data[d] = d
    def insert(self, i):
        if i in self.data.keys():
            return 'Already in set'
        self.data[i] = i
    def remove(self, i):
        if i not in self.data.keys():
            return 'Not in set'
        self.data.pop(i)
    def size(self):
        return len(self.data.keys())
    def contains(self, i):
        if i in self.data.keys():
            return True
        return False
    def union(self, otherSet):
        setData = list(set(self.data.keys()) | set(otherSet.data.keys()))
        unionSet = Set(setData)
        return unionSet
    def intersection(self, otherSet):
        setData = list(set(self.data.keys()) & set(otherSet.data.keys()))
        intersectionSet = Set(setData)
        return intersectionSet
    def difference(self, otherSet):
        setData = list(set(self.data.keys()) ^ set(otherSet.data.keys()))
        differenceSet = Set(setData)
        return differenceSet
    def subset(self, otherSet):
        if set(self.data.keys()) < set(otherSet.data.keys()):
            return True
        return False
    def disp(self):
      return '{'+', '.join(str(x) for x in self.data.keys())+'}'
s = Set([1, 2, 3, 4, 1, 4])
s1=Set([2,3])
print(s.size())
s.insert(7)
print(s.disp())
print(s.contains(4))
print(s1.subset(s))
d=s.union(s1)
print(d.disp())
e=s.intersection(s1)
print(e.disp())
s.remove(7)
print(s.disp())

#OUTPUT
4
{1, 2, 3, 4, 7}
True
True
{1, 2, 3, 4, 7}
{2, 3}
{1, 2, 3, 4}

