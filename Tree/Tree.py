class Tree:
    def __init__(self,data, values):
        self.data     = data
        self.value    = values
        self.children = []
        self.parent   = None
        
    def get_label(self):
        level = 0
        Parent = self.parent
        while Parent:
            level += 1
            Parent = Parent.parent
        
        return level
    
    def print_tree(self):
        spaces = ' '*self.get_label()*2
        prefix = spaces + "|__ " if self.parent else ' '
        print(prefix + self.data + '='+str(self.value))
        if self.children:
            for child in self.children:
                child.print_tree()
                
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
def build_product_tree(tree_data, Root):   
    if Root in tree_data.keys():
        # Pick the minimum value for the parent node from branches
        Parent = Tree(Root, min(tree_data[Root].values()))
        for child in tree_data[Root].keys():
            Child = Tree(child,tree_data[Root][child])
            if child in tree_data.keys():
                Child = build_product_tree(tree_data,child)
            Parent.add_child(Child)

    #Parent.print_tree()
    return Parent


if __name__ == '__main__':
    tree = {
        'A': {'B':0,'C':0,'D':0},
        'B': {'E':10,'F':20,'G':30},
        'C': {'H':40,'I':50,'J':60},
        'D': {'K':70,'L':80,'M':90}
    }
    T = build_product_tree(tree,'A')
    T.print_tree()