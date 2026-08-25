class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        unordered_map<int, int> count;
        vector<vector<int>> v(nums.size()+1);
        for(auto n : nums){
            count[n] += 1;
        }

        for(auto it : count){
            v[it.second].push_back(it.first);
        }

        for(int i = v.size() - 1; i>0; --i){
            for (int n : v[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }

        return res;
    }
};
