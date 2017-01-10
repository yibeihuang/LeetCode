__author__ = 'yibeihuang'
def verticalOrder(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # hashmap, BFS
        if root==None: return []
        q = [root]
        col,rst = [0],[]
        hashmap = {}
        mi, mx = 0,0
        while q:
            curr_node = q.pop(0)
            curr_col = col.pop(0)
            if curr_col not in hashmap:
                hashmap[curr_col]=[]
            hashmap[curr_col].append(curr_node.val)
            if curr_node.left:
                q.append(curr_node.left)
                col.append(curr_col-1)
                mi = min(mi, curr_col-1)
            if curr_node.right:
                q.append(curr_node.right)
                col.append(curr_col+1)
                mx = max(mx, curr_col+1)
        for i in range(mi, mx+1):
            rst.append(hashmap[i])
        return rst