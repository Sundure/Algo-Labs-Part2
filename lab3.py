class Lab3:
    class BinaryTree:
        def __init__(self, value, left=None, right=None, parent=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

    @staticmethod
    def find_successor(chosen_node: BinaryTree):
        successor_value = None
        target_value = chosen_node.value
        can_go_left = True

        while True:
            while chosen_node.left != None and can_go_left:
                chosen_node = chosen_node.left
            else:
                if successor_value == None and chosen_node.value > target_value:
                    successor_value = chosen_node.value
                elif successor_value != None and chosen_node.value > target_value and chosen_node.value < successor_value:
                    successor_value = chosen_node.value

            if chosen_node.right != None:
                can_go_left = True
                chosen_node = chosen_node.right
                continue
            else:
                can_go_left = False
                if chosen_node.parent == None:
                    break
                else:
                    while chosen_node.parent != None and chosen_node.parent.right == chosen_node:
                        chosen_node = chosen_node.parent
                    if chosen_node.parent == None:
                        break
                    else:
                        chosen_node = chosen_node.parent

        return successor_value

    @staticmethod
    def read_from_file(filepath: str):
        with open(filepath, 'r', encoding='utf-8') as f:
            values = list(map(int, f.readline().split()))
            target = int(f.readline().strip())

        root = None
        chosen_node = None

        for val in values:
            if not root:
                root = Lab3.BinaryTree(val)
                if val == target: chosen_node = root
                continue
            
            curr = root
            while True:
                if val < curr.value:
                    if not curr.left:
                        curr.left = Lab3.BinaryTree(val, parent=curr)
                        if val == target: chosen_node = curr.left
                        break
                    curr = curr.left
                else:
                    if not curr.right:
                        curr.right = Lab3.BinaryTree(val, parent=curr)
                        if val == target: chosen_node = curr.right
                        break
                    curr = curr.right

        return root, chosen_node

    @staticmethod
    def print_tree(root):
        if not root: return
        
        grid = {}
        
        def write_str(x, y, s):
            for i, char in enumerate(s):
                grid[(x + i, y)] = char

        def traverse(node, x, y, side):
            if not node: return
            
            s_val = str(node.value)
            write_str(x, y, s_val)
            
            H = 8
            V = 2
            
            if side == 0:  
                if node.left:
                    for i in range(x - H + len(str(node.left.value)) + 1, x - 1):
                        grid[(i, y)] = '-'
                    traverse(node.left, x - H, y, -1)
                if node.right:
                    for i in range(x + len(s_val) + 1, x + H - 1):
                        grid[(i, y)] = '-'
                    traverse(node.right, x + H, y, 1)
                    
            elif side == -1:  
                if node.right:
                    grid[(x - H//2, y - V//2)] = '\\'
                    traverse(node.right, x - H, y - V, -1)
                if node.left:
                    grid[(x - H//2, y + V//2)] = '/'
                    traverse(node.left, x - H, y + V, -1)
                    
            elif side == 1:  
                if node.right:
                    grid[(x + H//2, y - V//2)] = '/'
                    traverse(node.right, x + H, y - V, 1)
                if node.left:
                    grid[(x + H//2, y + V//2)] = '\\'
                    traverse(node.left, x + H, y + V, 1)

        traverse(root, 0, 0, 0)
        
        min_x = min(k[0] for k in grid.keys())
        max_x = max(k[0] for k in grid.keys())
        min_y = min(k[1] for k in grid.keys())
        max_y = max(k[1] for k in grid.keys())
        
        print("\n--- Tree Visualization ---")
        for y in range(min_y, max_y + 1):
            row = "".join(grid.get((x, y), ' ') for x in range(min_x, max_x + 1))
            print(row.rstrip())
        print("---------------------------\n")

if __name__ == "__main__":
    tree, target = Lab3.read_from_file("test.txt")
    
    if tree and target:
        Lab3.print_tree(tree)
        print(f"Looking for successor of node: {target.value}")
        successor = Lab3.find_successor(target)
        print(f"Found successor: {successor}")
