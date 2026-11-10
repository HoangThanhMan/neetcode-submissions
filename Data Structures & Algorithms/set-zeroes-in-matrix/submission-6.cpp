class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();

        vector<vector<long long>> temp(n, vector<long long>(m));

        // Copy matrix sang temp
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                temp[i][j] = matrix[i][j];
            }
        }

        long long MARK = 1LL << 33;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (temp[i][j] == 0 || temp[i][j] == MARK) {

                    // Mark row
                    for (int a = 0; a < m; a++) {
                        if (temp[i][a] < (1LL << 31)) {
                            temp[i][a] += MARK;
                        }
                    }

                    // Mark column
                    for (int b = 0; b < n; b++) {
                        if (temp[b][j] < (1LL << 31)) {
                            temp[b][j] += MARK;
                        }
                    }
                }
            }
        }

        // Convert marked elements to zero
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (temp[i][j] >= (1LL << 31)) {
                    temp[i][j] = 0;
                }
            }
        }

        // Copy kết quả trở lại matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                matrix[i][j] = static_cast<int>(temp[i][j]);
            }
        }
    }
};