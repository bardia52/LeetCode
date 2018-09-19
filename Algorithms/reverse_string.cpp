#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string reverseString(string s) {
        int len = s.length();
        string result(len, '*');
        for (int i = 0; i <= len; i++) {
        	result[i] = s[len-i-1];
        }
        return result;
    }
};

int main() {
    string line = "Yellow";
	string ret = Solution().reverseString(line);

	string out = (ret);
	cout << out << endl;
    return 0;
}
