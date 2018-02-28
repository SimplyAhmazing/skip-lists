import random
import collections


class NilNode(object):
    def __init__(self):
        self.key = float('inf')
        self.val = float('inf')


NIL = NilNode()


class Node(object):
    def __init__(self, key, val, levels = 0):
        self.key = key
        self.val = val
        # self.forward = [None] * levels
        self.forward = collections.defaultdict(lambda: NIL)
        [self.forward[i] for i in range(levels + 1)]

    def __str__(self):
        return '<Node ({}, {})'.format(self.key, self.val)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.forward)


class SkipList(object):
    def __init__(self):
        self.header = Node(None, None)

    def insert(self, key, val):
        # search_key = hash(key)
        search_key = key
        # local_update = [None] * len(self.header)
        update = collections.defaultdict(lambda: NIL)

        x = self.header
        for i in range(len(self.header), -1):
            print('i is ', i)
            while self.header.forward[i].key < search_key:
                x = self.header.forward[i]
            update[i] = x
        print(x, 'update', update)

        if x.key == search_key:
            x.val = val
        else:
            lvl = self.random_level()
            print('Random lvl generated is', lvl)
            if lvl > len(self.header):
                for i in range(len(self.header), lvl - 1):
                    update[i] = self.header  # Hmm..??
            x = Node(search_key, val, levels=lvl)
            for i in range(0, lvl + 1):
                if not isinstance(x.forward[i], NilNode):
                    x.forward[i] = update[i].forward[i]
                    update[i].forward[i] = x
        pass

    def delete(self, key, val):
        pass

    def search(self, key):
        pass

    def random_level(self):
        lvl = 0
        p = 0.5
        max_level = len(self.header)
        while random.random() < p and lvl < max_level:
            lvl += 1
        return lvl

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, val):
        return self.insert(key, val)


skl = SkipList()


skl['a'] = 1
# skl['b'] = 2
# skl['c'] = 3

# assert skl['a'] == 1
# assert skl['b'] == 2
# assert skl['c'] == 3
#
# del skl['c']
#
# assert skl['c'] == None
