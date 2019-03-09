# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        numLists = len(lists)
        if numLists == 0:
            return []
        # print numLists, lists
        while True:
            # Initialize minInx
            for minInx in range(numLists):
                if lists[minInx]!= None:
                    minVal = lists[minInx].val
                    break
            # if all(v is None for v in lists):
            if lists[minInx] == None:
                break
            # find minInx
            for l in range(numLists):
                if lists[l]!=None and lists[l].val < minVal:
                    minVal = lists[l].val
                    minInx = l
            # print minInx, lists[minInx].val
            if 'cur' in locals():
                cur.next = lists[minInx]
                # print "cur1=",cur, cur.next, lists[minInx]
                cur = cur.next
            else:
                ans = cur = lists[minInx]
            # cur = cur.next
            lists[minInx] = lists[minInx].next
            # print "cur2=",cur, cur.next, lists[minInx]
            # print lists
        if 'ans' not in locals():
            return []
        return ans