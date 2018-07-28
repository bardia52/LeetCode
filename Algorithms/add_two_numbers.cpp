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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyRoot = new ListNode(0);
        ListNode* lSum = dummyRoot;
        int flag = 0;
        while (l1 || l2) {
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;
            int midVal = val1 + val2 + flag;
            int digit = 0;
            if (midVal >= 10) {
                flag = 1;
                digit = midVal - 10;
            }
            else {
                flag = 0;
                digit = midVal;
            }
            lSum->next = new ListNode(digit);
            if (l1)
                l1 = l1->next;
            if (l2)
                l2 = l2->next;
            lSum = lSum->next;
        }
        if (flag)
            lSum->next = new ListNode(1);
        lSum = dummyRoot->next;
        delete dummyRoot;
        return lSum;
    }
};
