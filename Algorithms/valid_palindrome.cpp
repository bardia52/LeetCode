class Solution {
public:
    bool isPalindrome(string s) {
        int inx1 = 0;
        int inx2 = s.length();
        bool checkPalindrome = true;
        if (s.length() <= 1)
            return checkPalindrome;
        while (inx1 < inx2) {
            // Skip over space
            while (!isalnum(s[inx1])) inx1++;
            while (!isalnum(s[inx2])) inx2--;
            if (inx1 > inx2) break;

            // Check symmetry
            if (toupper(s[inx1]) != toupper(s[inx2])) {
                checkPalindrome = false;
                break;
            }
            else {
                inx1++;
                inx2--;
            }
        }
        return checkPalindrome;
    }
};
