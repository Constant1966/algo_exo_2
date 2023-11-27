from BinaryNode import BinaryNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __init__(self, item=None):
        self.root = BinaryNode(item)

    #  TODO: on insere un nouvel item a partir de la racine
    # O(log(n))
    def insert(self, item):
        if self.root is None:
            self.root = BinaryNode(item)
        else:
            self._insert_recursive(self.root, item)


    def _insert_recursive(self, current_node, item):
        if item < current_node.data:
            if current_node.left is None:
                current_node.left = BinaryNode(item)
            else:
                self._insert_recursive(current_node.left, item)
        else:
            if current_node.right is None:
                current_node.right = BinaryNode(item)
            else:
                self._insert_recursive(current_node.right, item)


    def contains(self, item):
        return self._contains_recursive(self.root, item) if self.root else False

    def _contains_recursive(self, current_node, item):
        if current_node is None:
            return False
        if current_node.data == item:
            return True
        elif item < current_node.data:
            return self._contains_recursive(current_node.left, item)
        else:
            return self._contains_recursive(current_node.right, item)

    def getHeight(self):
        return self._getHeight_recursive(self.root) if self.root else -1

    def _getHeight_recursive(self, current_node):
        if current_node is None:
            return 0
        left_height = self._getHeight_recursive(current_node.left)
        right_height = self._getHeight_recursive(current_node.right)
        return 1 + max(left_height, right_height)

    def getItemsInOrder(self):
        items = []
        self._fillListInOrder(self.root, items)
        return items

    def _fillListInOrder(self, current_node, result):
        if current_node is not None:
            self._fillListInOrder(current_node.left, result)
            result.append(current_node)
            self._fillListInOrder(current_node.right, result)

    def toStringInOrder(self):
        items = self.getItemsInOrder()
        return "[" + ", ".join(str(node.data) for node in items) + "]"
    


# # Création de l'arbre binaire de recherche
# tree = BinarySearchTree(5)
# tree.insert(3)
# tree.insert(7)
# tree.insert(2)
# tree.insert(4)
# tree.insert(6)
# tree.insert(8)

# # Test de la méthode contains pour vérifier la présence d'un élément
# print("L'arbre contient-il l'élément 4 ?", tree.contains(4))  # Devrait afficher True
# print("L'arbre contient-il l'élément 9 ?", tree.contains(9))  # Devrait afficher False

# # Test de la méthode getHeight pour obtenir la hauteur de l'arbre
# print("Hauteur de l'arbre :", tree.getHeight())  # Devrait afficher la hauteur de l'arbre

# # Test de la méthode getItemsInOrder pour obtenir les éléments dans l'ordre
# elements_in_order = tree.getItemsInOrder()
# print("Éléments dans l'ordre :", [node.data for node in elements_in_order])

# # Test de la méthode toStringInOrder pour obtenir une représentation en chaîne des éléments dans l'ordre
# print("Représentation en chaîne des éléments dans l'ordre :", tree.toStringInOrder())

