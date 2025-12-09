class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans=-10000;
        int length=nums.size();
        int variable=0;
        for(int i=0;i<length;i++){
            variable=variable+nums[i];
            if(variable>ans){
                ans=variable;
            }
           if (variable<0){
            variable=0;
           }
        }
        return ans;
    }
};