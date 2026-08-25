class Solution:
    def isValid(self, s: str) -> bool:
        st = list()
        
        for i in range(len(s)):
            if st:
                last = st[-1]
                cur = s[i]
                if self.is_pair(last, cur):
                    st.pop()
                    continue
            
            st.append(s[i])

        return not st

    def is_pair(self, last, cur):
        return last == '(' and cur == ')' or last == '{' and cur == '}' or last == '[' and cur == ']'

            