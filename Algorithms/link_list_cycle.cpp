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
    bool hasCycle(ListNode *head) {
        if (head == NULL) return false;
        ListNode *p1 = head;
        ListNode *p2 = head;
        while (1) {
            if (p1->next == NULL)
                break;
            else
                p1 = p1->next;
            if  ((p2->next == NULL) || (p2->next->next == NULL))
                break;
            else
                p2 = p2->next->next;
            if (p1 == p2)
                return true;
        }
        return false;
    }
};
