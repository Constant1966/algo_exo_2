from CompanyNode import CompanyNode


class CompanyTree:
    def __init__(self):
        self.root = None

    def __init__(self, item):
        self.root = item

    def buy(self, item):
        # Ajout de la logique pour que la compagnie mère achète une autre compagnie
        pass

    def getMoney(self):
        # Retourne le montant en banque de la compagnie mère
        return self.root.getMoney() if self.root else float('-inf')

    def getWorstChildMoney(self):
        # Retourne le montant le plus bas parmi tous les enfants et sous-enfants de la compagnie mère
        return self.root.getWorstChildMoney() if self.root else float('-inf')

    def getTreeInOrder(self):
        # Retourne une présentation en chaîne de caractères en ordre inverse de la compagnie mère et de ses enfants
        return self.root.fillStringBuilderInOrder("") if self.root else ""



# Création des objets CompanyNode
companyMere = CompanyNode(1000)
companyMere.childs.insert(CompanyNode(800))
companyMere.childs.insert(CompanyNode(1200))

companyMere.childs.root.buy(CompanyNode(700))
companyMere.childs.root.buy(CompanyNode(900))

companyMere.childs.root.right.buy(CompanyNode(1100))
companyMere.childs.root.right.buy(CompanyNode(1300))

# Création de l'arbre d'entreprises
tree = CompanyTree(companyMere)

# Test des méthodes de l'arbre d'entreprises
print("Montant en banque de la compagnie mère :", tree.getMoney())
print("Pire montant parmi tous les enfants et sous-enfants :", tree.getWorstChildMoney())
print("Présentation en ordre inverse de la compagnie mère et de ses enfants :\n", tree.getTreeInOrder())
