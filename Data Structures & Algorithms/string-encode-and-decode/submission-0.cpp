class Solution {
public:

    /*
        neet code love you
        -> 4#neet4#code4#love3#you (encode)
    */
    string encode(vector<string>& strs) {
        string res = "";
        for(string s : strs){
            res += to_string(s.size()) + "#" + s;
        }
        return res;
    }

    /*
        4#neet4#code4#love3#you
        -> neet code love you (decode)
    */
    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while(i < s.size()){
            int j = i;
            while(s[j] != '#'){
                j++;
            }
            int sz = stoi(s.substr(i, j - i));
            res.push_back(s.substr(j + 1, sz));
            i = j + sz + 1;
        }   
        return res;
    }
};
