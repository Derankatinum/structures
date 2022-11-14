class Tree:

    def __init__(root,data):#конструктор  __init__ використовуватиметься для вставки елементів в дерево
        root.right=None
        root.left=None
        root.value=data
        
    def search_node(root,data):#пошук елементу
        if data < root.value:
            if root.left is None:
                return str(data)+" not found"
            return root.left.search_node(data)
        elif data > root.value:
            if root.right is None:
                return str(data)+" not found"
            return root.right.search_node(data)
        else:
            print(str(root.value)+" is found!")
        
    def insert(root,data):#метод для вставки елементів
        if root.value:
            if root.value>data:
                if root.left is None:
                    root.left=Tree(data)
                else:
                    root.left.insert(data)
            elif root.value<data:
                if root.right is None:
                    root.right=Tree(data)
                else:
                    root.right.insert(data)
        else:
            root.value=data
        
    def create_root_bst(root,data):
        root.right=None
        root.left=None
        root.parent=None
        root.value=data







def inorder(root):
        if root:
            inorder(root.left)
            print(str(root.value)+'->',end='')
            inorder(root.right)
            
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.value)+"->",end='')

def preorder(root):
    if root:
        print(str(root.value)+"->",end='')
        postorder(root.left)
        postorder(root.right)

        
def tree_successor(root):
    pass

root=Tree(10)
root.insert(15)
root.insert(121)
root.insert(22)
root.insert(12)
root.insert(143)
print("inorder :\n")
inorder(root)
print("\n\npostorder :\n")
postorder(root)
print("\n\npreorder :\n")
preorder(root)
print("\n"+root.search_node(10))

