/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Find the lengths of lists
        ListNode* lp1 = l1;
        int len1 = 0;
        while (lp1) {
            lp1 = lp1->next;
            len1++;
        }

        ListNode* lp2 = l2;
        int len2 = 0;
        while (lp2) {
            lp2 = lp2->next;
            len2++;
        }

        // Reverse them
        lp1 = reverseList(l1);
        lp2 = reverseList(l2);



        return num1+num2;
    }

    ListNode* reverseList(ListNode* head) {
        ListNode *current = head;
        ListNode *prev = NULL;
        ListNode *next = NULL;
        while (current != NULL) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }
};

