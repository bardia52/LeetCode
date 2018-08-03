class Solution {
public:
    int firstUniqChar(string s) {
        int list[256] = {0};
        for(auto i: s) {
            list[i] ++;
            //cout << "i=" << i << "list[i]= " << list[i] << endl;
        }
        for(int i=0; i<s.length(); i++) {
            if (list[s[i]]==1)
                return i;
        }
        return -1;
    }
};
