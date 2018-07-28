class Solution {
public:
    int romanToInt(string s) {
        // Creating a hashtable for Roman and Integers
        map<char, int> indexMap = {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000},
        };

        // Converting from left to right
        int n = s.size() - 1;
        int res = 0;
        for (int i = 0; i < n; i++) {
            // Check for subtraction cases
            if (indexMap[s[i]] < indexMap[s[i + 1]])
                res -= indexMap[s[i]];
            else
                res += indexMap[s[i]];
        }
        res += indexMap[s[n]];
        return res;
    }
};
