99. Recover Binary Search Tree
Hard

969

55

Favorite

Share
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?


"""
 Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 Use Morris Traversal; Time O(n), Space O(1)
"""

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Morris Traversal
        parent, pre, cur = None, None, root
        first, second = None, None
        while cur:
            if not cur.left:
                if parent and parent.val > cur.val:
                    if not first:           # if never assigned first, assign first (and then keep unchanged)
                        first = parent
                    second = cur            # update second
                parent = cur                # update parent as cur moves forward
                cur = cur.right             # continue to traverse right sub-tree of cur
            else:
                pre = cur.left              
                while pre.right and pre.right != cur:
                    pre = pre.right         # pre = the rightmost node under cur.left unless pre.right == cur(previouly assigned)
                if not pre.right:
                    pre.right = cur         # build the path to next inorder Node
                    cur = cur.left          # cur = next inorder Node which is cur.left since cur.left is True
                else:
                    pre.right = None        # break the path to next inorder Node to recover to original tree when pre.right = cur(previouly assigned)
                    if parent and parent.val > cur.val:
                        if not first:       # if never assigned first, assign first (and then keep unchanged)
                            first = parent
                        second = cur        # update second
                    parent = cur
                    cur = cur.right         # cur = next inorder Node(a parent Node)
                    
        first.val, second.val = second.val, first.val   # simplest way to swap
        # Use XOR to swap integers: x ^= y y ^= x x ^= y
