class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";

        int start = 0;
        int maxLength =1;
        
        for (int i = 0; i < s.length(); i++) {
            //odd-length
            int left = i, right = i;
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                left--;
                right++;
            }
            int len1 = right - left - 1;
            //even-length
            left = i;
            right = i+1;
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                left--;
                right++;
            }
            int len2 = right - left -1;
            int currentMax = max(len1, len2);

            if (currentMax > maxLength) {
                maxLength = currentMax;
                start = i - (currentMax - 1) / 2;
            }
        }
        return s.substr(start, maxLength);
    }
};