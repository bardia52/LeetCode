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
        //cout << "l1=" << listNodeToString(l1) << " l2=" << listNodeToString(l2) << endl;
        int num1 = list2int(l1);
        int num2 = list2int(l2);
        cout << "num1=" << num1 << " num2=" << num2 << endl;
        int sum = num1 + num2;
        ListNode* sumNode = int2list(sum);
        return sumNode;
    }
private:
    int list2int(ListNode* node) {
        int result = 0;
        if (node == nullptr) {
        }
        else {
            int order = 1;
            while (node) {
                result += (node->val * order);
                order *= 10;
                cout << "result=" << result << endl;
                node = node->next;
            }
        }
        return result;
    }

    ListNode* int2list(int num) {
        int numTemp = num;
        ListNode* dummyRoot = new ListNode(0);
        ListNode* ptr = dummyRoot;
        do {
            int rightDigit = numTemp % 10;
            numTemp /= 10;
            ptr->next = new ListNode(rightDigit);
            ptr = ptr->next;
        } while(numTemp);
        ptr = dummyRoot->next;
        delete dummyRoot;
        return ptr;
    }
};
