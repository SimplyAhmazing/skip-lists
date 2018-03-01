import random
from icecream import ic


class Node(object):
    def __init__(self, key, val, levels=0):
        self.key = key
        self.val = val
        self.forward = [None] * levels

    def __str__(self):
        return '<Node ({}, {})'.format(self.key, self.val)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.forward)


class SkipList(object):
    def __init__(self):
        self.header = Node(None, None, 1)
        self.level = 0
        self.max_level = 1

    def insert(self, key, val):
        node = Node(key, val, levels=self.random_level())
        self.max_level = max(self.max_level, len(node.forward))

        while len(self.header.forward) < len(node.forward):
            self.header.forward.append(None)

        update = [None] * self.max_level

        cur = self.header
        for i in reversed(range(len(self.header))):
            while cur.forward[i] and cur.forward[i].key < key:
                cur = cur.forward[i]
            update[i] = cur

        # Update key/val if exists and exist, else splice in node
        if cur.key == key:
            cur.val = val
            return

        if len(node.forward) > self.level:
            for i in range(self.level, len(node.forward)):
                update[i] = self.header
            self.level = len(node.forward)

        for i in range(len(node.forward)):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node

    def delete(self, key):
        node = self.search(key)
        if not node: return

        update = [None] * self.max_level
        cur = self.header
        for i in reversed(range(len(self.header))):
            while cur.forward[i] and cur.forward[i].key < key:
                cur = cur.forward[i]
            update[i] = cur

        for i in reversed(range(len(node.forward))):
            update[i].forward[i] = node.forward[i]
            if self.header.forward[i] == None:
                self.max_level -= 1
        self.level -= 1

    def search(self, key):
        cur = self.header
        for i in reversed(range(len(self.header))):
            while cur.forward[i] is not None and key > cur.forward[i].key:
                cur = cur.forward[i]

        if key == cur.key:
            return cur
        elif cur.forward[i] and key == cur.forward[i].key:
            return cur.forward[i]

    def random_level(self):
        lvl = 1
        while random.uniform(0, 1) < 0.5:  # and lvl < self.max_level:
            lvl += 1
        return lvl

    def __contains__(self, key):
        return self.search(key) is not None

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, val):
        return self.insert(key, val)

    def print(self):
        for level in reversed(range(len(self.header.forward))):
            cur = self.header.forward[level]
            print('level', level)
            while cur is not None:
                # print('({}, {})'.format(cur.key, cur.val), end=' ')
                print('{}'.format(cur.val), end=' ')
                cur = cur.forward[level]
            print('')



# skl = SkipList()
#
# [skl.insert(chr(65+i), i) for i in range(26)]
# skl.print()
#
# assert 'D' in skl
# assert 'd' not in skl
#


# skl['a'] = 1
# skl['b'] = 2
# skl['c'] = 3

# assert skl['a'] == 1
# assert skl['b'] == 2
# assert skl['c'] == 3
#
# del skl['c']
#
# assert skl['c'] == None
