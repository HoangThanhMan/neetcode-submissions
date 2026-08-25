class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size());
        int mul = 1;
        int cnt_zero = 0;
        for(int i = 0; i < nums.size() ; i++){
            if(nums[i] != 0){
                mul*= nums[i];
            }else{
                cnt_zero += 1;
            }
        }

        for(int i = 0; i < nums.size() ; i++){
            if(nums[i]!=0){
                ans[i] = (mul / nums[i]) * (cnt_zero == 0);
            }else{
                ans[i] = mul * (cnt_zero - 1 == 0);
            }
        }
        return ans;
    }
};
