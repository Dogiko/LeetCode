# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_tree_in(input_list):
    for t in input_list:
        if type(t) != int:
            return True
    
    return False

def tree_decompose(input_tree):
    ans = []
    if input_tree.left != None:
        ans.append(input_tree.left)
    
    ans.append(input_tree.val)
    
    if input_tree.right != None:
        ans.append(input_tree.right)
    
    return ans

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
        
        
        ans = [root]
        conti_bool = True
        while conti_bool:
            for i in range(len(ans)):
                if type(ans[i]) != int:
                    if i == 0:
                        ans = tree_decompose(ans[i]) + ans[i + 1:]
                    elif i == len(ans) - 1:
                        ans = ans[:len(ans) - 1] + tree_decompose(ans[i])
                    else:
                        ans = ans[:i] + tree_decompose(ans[i]) + ans[i + 1:]
                    break
                elif i == len(ans) - 1:
                    conti_bool = False
        
        return ans