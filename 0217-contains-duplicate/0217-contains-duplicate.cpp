class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map <int, int>mp;
        int length = nums.size();
        for (int i = 0; i < length; i++) {
            mp[nums[i]]++;
            
        }   // 2->1 3->1 1->2
        for (auto i: mp) {
            int a = i.second; // for value
            // int b = i.first; for key
            if (a >= 2) {
                return true;
            }
        }
        return false;
    }
};