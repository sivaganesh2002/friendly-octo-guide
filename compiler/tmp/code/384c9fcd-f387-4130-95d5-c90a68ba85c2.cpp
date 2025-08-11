#include <bits/stdc++.h>
using namespace std;

bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
    int n = s.size();
    vector<bool> dp(n + 1, false);
    dp[0] = true; // base case: empty string

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (dp[j] && wordSet.count(s.substr(j, i - j))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}

int main() {
    string s;
    getline(cin, s); // read the string
    string dictLine;
    getline(cin, dictLine); // read dictionary line

    stringstream ss(dictLine);
    vector<string> wordDict;
    string word;
    while (ss >> word) {
        wordDict.push_back(word);
    }

    cout << (wordBreak(s, wordDict) ? "True" : "False") << endl;
    return 0;
}