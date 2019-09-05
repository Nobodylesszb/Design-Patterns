from enum import Enum
import random

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


class Tree:
    pool = dict()

    def __new__(cls, tree_type, *args, **kwargs):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({},{})'.format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    print('trees rendered {}'.format(tree_counter))
    print('trees actully created:{}'.format(len(Tree.pool)))

    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)

    print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
    print('{}=={}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))


if __name__ == '__main__':
    main()


"""
render a tree of type TreeType.apple_tree and age 24 at (45,26)
render a tree of type TreeType.apple_tree and age 19 at (26,71)
render a tree of type TreeType.apple_tree and age 8 at (93,54)
render a tree of type TreeType.apple_tree and age 8 at (69,52)
render a tree of type TreeType.apple_tree and age 5 at (21,23)
render a tree of type TreeType.apple_tree and age 26 at (27,11)
render a tree of type TreeType.apple_tree and age 14 at (38,58)
render a tree of type TreeType.apple_tree and age 20 at (79,51)
render a tree of type TreeType.apple_tree and age 5 at (10,80)
render a tree of type TreeType.apple_tree and age 6 at (67,58)
render a tree of type TreeType.cherry_tree and age 24 at (36,36)
render a tree of type TreeType.cherry_tree and age 13 at (9,83)
render a tree of type TreeType.cherry_tree and age 8 at (52,86)
render a tree of type TreeType.peach_tree and age 18 at (13,7)
render a tree of type TreeType.peach_tree and age 18 at (32,75)
render a tree of type TreeType.peach_tree and age 6 at (0,57)
render a tree of type TreeType.peach_tree and age 26 at (90,1)
render a tree of type TreeType.peach_tree and age 1 at (68,82)
trees rendered 18
trees actully created:3
2503257029712 == 2503257029712? True
2503257029712==2503256986904? False
"""
