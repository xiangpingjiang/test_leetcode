from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree_from_list(nums):
    root = TreeNode(nums[0])
    len_nums = len(nums)
    c = 1
    i = 1
    pre_level = [root]
    while c + 2 ** i <= len_nums:
        current_level_list = nums[c: c + 2 ** i]
        current_level_Node = []
        j = 0
        for pr_l in pre_level:
            if current_level_list[j] != None:
                l = TreeNode(current_level_list[j])
            else:
                l = None
            if current_level_list[j+1] != None:
                r = TreeNode(current_level_list[j+1])
            pr_l.left = l
            pr_l.right = r
            current_level_Node.append(l)
            current_level_Node.append(r)
            j += 2
        c = c + 2 ** i
        i += 1
        pre_level = current_level_Node
    return root
    # last_level = nums[c:]
    # for i in range(len(last_level)):
    #     n = int(i/2)
    #     if i % 2 == 0:
    #         pre_level[n].left = 


    # j = 0
    # for pr_l in pre_level:
    #     l = TreeNode(current_level_list[j])
    #     r = TreeNode(current_level_list[j+1])
    #     pr_l.left = l
    #     pr_l.right = r
    #     current_level_Node.append(l)
    #     current_level_Node.append(r)
    #     j += 2



from collections import deque


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(ro, le, ri):
            if ro == None:
                return True
            if le and ro.val <= le:
                return False
            if ri and ro.val >= ri:
                return False
            
            return check(ro.left,le,ro.val) and check(ro.right,ro.val,ri)
        
        return check(root,None,None)
    
node1 = TreeNode(7)
node2 = TreeNode(4)
# node3 = TreeNode(3)

# node1.right = node3
# node1.left = node2

r = create_tree_from_list([0,None,-1])

s = Solution()

n = s.isValidBST(r)

print("c")