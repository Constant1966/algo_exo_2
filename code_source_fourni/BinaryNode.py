
class BinaryNode:
    # Le noeud contient la donnee, une reference vers le fils de gauche et une reference vers le fils de droite
    # #private T data;
    # #private BinaryNode<T> right;
    # #private BinaryNode<T> left;

    # TODO: initialisation (add the code in place of pass)
#   # O(1)
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # TODO: on retourne la donnee voulue
    # O(1)
    def getData(self):
        return self.data

    # TODO: on ajoute une nouvelle donnee au bon endroit
    # Vous pouvez utiliser la forme du livre 
    # O(log(n))
    def insert(self, newData):
        if newData < self.data:
            if self.left is None:
                self.left = BinaryNode(newData)
            else:
                self.left.insert(newData)
        else:
            if self.right is None:
                self.right = BinaryNode(newData)
            else:
                self.right.insert(newData)

    # TODO: est-ce que l'item fais partie du noeuds courant
    # O(log(n))
    def contains(self, item):
        if self.data == item:
            return True
        elif item < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(item)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(item)

    #TODO: on retourne la hauteur maximale de l'arbre
    def getHeight(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.getHeight()
        elif self.right is None:
            return 1 + self.left.getHeight()
        else:
            return 1 + max(self.left.getHeight(), self.right.getHeight())

    # TODO: l'ordre d'insertion dans la liste est l'ordre logique
    # de manière que le plus petit item sera le premier inseré
    # result is a list of nodes
    def fillListInOrder(self, result):
        if self.left is not None:
            self.left.fillListInOrder(result)
        result.append(self.data)
        if self.right is not None:
            self.right.fillListInOrder(result)














# # Création d'un arbre binaire
# root = BinaryNode(5)
# root.insert(3)
# root.insert(7)
# root.insert(2)
# root.insert(4)
# root.insert(6)
# root.insert(8)

# # Liste pour stocker les éléments dans l'ordre logique
# elements = []
# root.fillListInOrder(elements)

# # Affichage de la liste des éléments dans l'ordre logique
# print("Éléments dans l'ordre logique :", elements)
