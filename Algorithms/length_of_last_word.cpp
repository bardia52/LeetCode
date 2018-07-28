class Solution {
public:
    int lengthOfLastWord(string s) {
        int lastLen = 0;
        int wordLen = 0;
        int index = 0;
        char ch = s[index];
        while (ch != NULL) {
            if (ch == ' ') {
                if (lastLen != 0)
                    wordLen = lastLen;
                lastLen = 0;
            }
            else {
                lastLen++;
            }
            ch = s[++index];
        }
        if (lastLen != 0)
            wordLen = lastLen;
        return wordLen;
    }
};
