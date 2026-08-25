class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size();
        int m = t.size();

        map<char, int> mp;

        for(int i = 0 ; i < n ; i++){
            mp[s[i]]+=1;
        }

        for(int i = 0 ; i < m ; i++){
            if(mp.find(t[i]) != mp.end()){
                mp[t[i]]-=1;
            }else{
                return 0;
            }
        }

        for(auto it : mp){
            if (it.second != 0) return 0;
        }

        return 1;
    }
};
