import random
import argparse
import time


class Node:
    def __init__(self, maximizing):
        self.maximizing = maximizing
        self.children = []
        self.leaf_value = None

    def set_leaf_value(self, v):
        assert len(self.children) == 0, 'Only leaf nodes can have a leaf value'
        self.leaf_value = v
        return self

    def add_child(self, c):
        assert self.leaf_value is None, 'Leaf nodes cannot have children'
        assert c.maximizing != self.maximizing, 'Incompatible maximizing value'
        self.children.append(c)
        return self

    def add_children(self, children):
        for child in children:
            self.add_child(child)
        return self

    def check(self):
        for child in self.children:
            child.check()
            assert child.maximizing != self.maximizing
        assert (self.leaf_value is None) != (len(self.children) == 0)

    def display(self, indentation_level=0):
        indentation = '  ' * indentation_level
        if len(self.children) > 0:
            string = ('T' if self.maximizing else 'F') + '[' + str(id(self)) + ']'
            for child in self.children:
                string += ('\n' + indentation + '|-' + child.display(indentation_level + 1))
        else:
            string = '('+str(self.leaf_value)+')'
        return string
        
    def tostring(self, indentation_level=0):
        indentation = '  ' * indentation_level
        if len(self.children) > 0:
            string = ('T' if self.maximizing else 'F')
            for child in self.children:
                string += ('\n' + indentation + '|-' + child.tostring(indentation_level + 1))
        else:
            string = '('+str(self.leaf_value)+')'
        return string

    def __str__(self):
        return self.tostring()


def get_random_tree(maximize, max_depth=5):
    ''' Construit un arbre dont le resultat de minimax est connu (selon si la
        racine est un noeud maximisant ou pas).
        Retourne le noeud racine de l'arbre et le score correspondant '''

    def make_children(parent, parent_score, max_depth, children_min=0, children_max=4):
        ''' instancie recursivement des noeuds enfants, de telle manière que le
        parent ait le score indiqué. On tire au sort le nombre d'enfants qu'aura parent,
        sauf si max_dpth est a 0 auquel cas on ne creera aucun enfant'''
        n = random.randrange(
            children_min, children_max) if max_depth > 0 else 0
        if n > 0:
            # on choisit quel sera l'enfant qui transmettra son score a son parent
            index_of_child_with_parent_score = random.randrange(n)
            for k in range(n):
                # on crée n enfants
                child = Node(maximizing=not parent.maximizing)
                if k == index_of_child_with_parent_score:
                    child_score = parent_score
                elif parent.maximizing:
                    child_score = random.randint(-10, parent_score)
                else:
                    child_score = random.randint(parent_score, 10)
                parent.add_child(child)
                # auxquels on crée des noeuds enfants recursivement
                make_children(child, child_score, max_depth - 1)
        else:
            # si parent ne doit avoir aucun enfant, alors c'est une feuille de l'arbre et il faut
            # lui attribuer une valeur
            parent.leaf_value = parent_score

    root = Node(maximize)  # création de la racine on fixe le score qu'aura le noeud racine
    root_score = random.randint(-10, 10)  # on impose à la racine d'avoir un minimum d'enfants
    make_children(root, root_score, max_depth, 3, 5)

    return root, root_score


# ---------------------------------
def get_test_tree1():
    '''Arbre dont le score est 10 lorsquue la racine est maximisant
    Issu de la vidéo https://www.youtube.com/watch?v=J1GoI5WHBto&t=13m11s'''
    n1 = Node(maximizing=True).set_leaf_value(10)
    n2 = Node(maximizing=True).set_leaf_value(11)
    n3 = Node(maximizing=True).set_leaf_value(9)
    n4 = Node(maximizing=True).set_leaf_value(12)
    n5 = Node(maximizing=True).set_leaf_value(14)
    n6 = Node(maximizing=True).set_leaf_value(15)
    n7 = Node(maximizing=True).set_leaf_value(13)
    n8 = Node(maximizing=True).set_leaf_value(14)
    n9 = Node(maximizing=True).set_leaf_value(5)
    n10 = Node(maximizing=True).set_leaf_value(2)
    n11 = Node(maximizing=True).set_leaf_value(4)
    n12 = Node(maximizing=True).set_leaf_value(1)
    n13 = Node(maximizing=True).set_leaf_value(3)
    n14 = Node(maximizing=True).set_leaf_value(22)
    n15 = Node(maximizing=True).set_leaf_value(20)
    n16 = Node(maximizing=True).set_leaf_value(21)

    n21 = Node(maximizing=False).add_children([n1, n2])
    n22 = Node(maximizing=False).add_children([n3, n4])
    n23 = Node(maximizing=False).add_children([n5, n6])
    n24 = Node(maximizing=False).add_children([n7, n8])
    n25 = Node(maximizing=False).add_children([n9, n10])
    n26 = Node(maximizing=False).add_children([n11, n12])
    n27 = Node(maximizing=False).add_children([n13, n14])
    n28 = Node(maximizing=False).add_children([n15, n16])

    n31 = Node(maximizing=True).add_children([n21, n22])
    n32 = Node(maximizing=True).add_children([n23, n24])
    n33 = Node(maximizing=True).add_children([n25, n26])
    n34 = Node(maximizing=True).add_children([n27, n28])

    n41 = Node(maximizing=False).add_children([n31, n32])
    n42 = Node(maximizing=False).add_children([n33, n34])

    root = Node(maximizing=True).add_children([n41, n42])
    return root, 10


def evaluate(node):
    assert node.leaf_value is not None, 'This node has no leaf_value'
    return node.leaf_value


def get_children(node):
    return node.children


def test(root, solution):
    ''' Test si minimax appliqué à root renvoie bien la solution '''
    result = minimax(root, root.maximizing, get_children, evaluate, float('inf'))
    if not result == solution:
        print(str.format("Error lors du test (maximize = {:b}) sur l'arbre : ", root.maximizing))
        print(root.display())
        print('minimax returned : ', result)
        print('but the solution is : ', solution)
        raise Exception()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('version', nargs='?', default='limited_depth')
    parser.add_argument('-n', '--ntests', type=int, default=100,
                        help='nombre de tests effectués sur des arbres aléatoirement générés')
    args = parser.parse_args()    
    
    # importation de minimax
    cmd = f'from ..minimax.{args.version} import minimax'
    print(cmd)
    exec(cmd)

    # début des tests
    t0 = time.time()
    test(*get_test_tree1())
    for k in range(args.ntests):
        test(*get_random_tree(maximize=k % 2 == 0, max_depth=random.randint(4, 6)))
    duration = time.time() - t0
    print("{} tests passés avec succès en {:.3f}ms".format(args.ntests + 1, duration*1000))
