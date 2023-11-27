from BinarySearchTree import BinarySearchTree

class CompanyNode:
    def __init__(self, money):
        self.money = money
        self.childs = BinarySearchTree()
        self.worstChild = None

    def buy(self, item):
        self.childs.insert(item)

    def getMoney(self):
        return self.money

    def fillStringBuilderInOrder(self, builder, prefix):
        builder.append(prefix).append(str(self.money)).append("\n")
        children = self.childs.getItemsInOrder()
        for child in reversed(children):
            child.fillStringBuilderInOrder(builder, prefix + " > ")

    def __lt__(self, other):
        return self.money < other.money

    def __gt__(self, other):
        return self.money > other.money

    def __eq__(self, other):
        return self.money == other.money


# Création des objets CompanyNode
companyA = CompanyNode(1000)
companyA.childs.insert(CompanyNode(800))
companyA.childs.insert(CompanyNode(1200))

companyA.childs.root.buy(CompanyNode(700))
companyA.childs.root.buy(CompanyNode(900))

companyA.childs.root.right.buy(CompanyNode(1100))
companyA.childs.root.right.buy(CompanyNode(1300))

# Affichage de la hiérarchie des entreprises
print(companyA.fillStringBuilderInOrder(""))
