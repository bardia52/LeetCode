/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // Corner case check
        if (headA == NULL || headB == NULL)
            return NULL;

        // Temporary pointer assignments
        ListNode *pA = headA;
        ListNode *pB = headB;
        
        while (pA != pB) {
            if (pA == NULL) {
                pA = headB;
            }
            else {
                pA = pA->next;
            }
            if (pB == NULL) {
                pB = headA;
            }
            else {
                pB = pB->next;
            }
        }
        return pA;
    }
};
