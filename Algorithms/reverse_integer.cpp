class Solution {
public:
    int reverse(int x) {
        // Getting digits one by one
        int x_tmp = x;
        vector<int> digits(10);
        int digit_inx = 0;
        while (x_tmp) {
            digits[digit_inx] = x_tmp % 10;
            x_tmp /= 10;
            digit_inx++;
        }

        // Constructing reverse number one digit at a time
        int rev_int = 0;
        for (int i = digit_inx; i > 0 ; i--) {
            int temp = rev_int * 10;
            // Overflow Check
            if (temp / 10 != rev_int)
                return 0; // Overflow
            else
                rev_int = temp;
            temp = rev_int + digits[digit_inx-i];
            // Overflow Check
            if (temp - digits[digit_inx-i] != rev_int)
                return 0; // Overflow
            else
                rev_int = temp;
        }
        return rev_int;
    }
};
