class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
     //map
     //data = int
     //index =int
     //data->index
     //key        value
     //presence   occerenece
     //name our our container ->

      unordered_map<int,int> mp; // empty

      //insert data->index
      int length=nums.size();
      vector<int> result;

      //optimization

      //tranverse it once
      for(int i=0;i<length;i++){
        //key = data
        //value = index
        //++
        int b = target- nums[i];
        if(mp.find(b)!=mp.end()){ //we have found it
           result.push_back(i);
           result.push_back(mp[b]);
           return result;
        }
        mp[nums[i]]=i;   //changes


      }
      //check conditions
      //logic
      //nums[i]=a
      //nums[j]=b
      // a +b =target
      //b= target - a
    return result;

    }
};