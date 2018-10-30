/*
 * Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
 * that the number could represent. A mapping of digit to letters (just like on the telephone 
 * buttons) is given below. Note that 1 does not map to any letters.
 *
 * Example:
 *
 * Input: "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 *
 */

#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // Iterative solution
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        // Corner case check
        if(digits.empty()) return vector<string>();

        // Define table of phone digits to letters
        static const vector<string> v = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        result.push_back("");   // add a seed for the initial case

        // Loop over the digits one-by-one
        for (unsigned int i = 0; i < digits.size(); i++) {
            // Translate each digit from char to int
            int num = digits[i] - '0';

            // Error check
            if ((num < 0) || (num > 9))
                break;

            string candidate = v[num];
            if(candidate.empty()) continue;

            // All the strings that have num at their i'th place
            vector<string> tmp;
            for (unsigned int j = 0; j < candidate.size(); j++) {
                for (unsigned int k = 0; k < result.size(); k++) {
                    // Concatenate new candidates to the existing strings
                    tmp.push_back(result[k]+candidate[j]);
                }
            }
            // Put the recently generated set into results
            result.swap(tmp);
        }
        return result;
    }
};

int main() {
    string test_vector = "123";

    cout << "before: " << test_vector << endl;

    vector<string> letter_combo = Solution().letterCombinations(test_vector);
    int len = letter_combo.size();

    cout << endl << "after: ";
    for (int i = 0; i < len; i++) {
        string letter_case = letter_combo[i];
        cout << letter_case << " ";

    }

    return 0;
}
