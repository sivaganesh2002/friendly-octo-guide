#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <climits>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// Recursive BST validator
bool isValidBST(TreeNode* root, long minVal, long maxVal) {
    if (!root) return true;
    if (root->val <= minVal || root->val >= maxVal) return false;
    return isValidBST(root->left, minVal, root->val) &&
           isValidBST(root->right, root->val, maxVal);
}

int main() {
    vector<string> tokens;
    string val;
    while (cin >> val) { // read entire line (space separated)
        tokens.push_back(val);
    }

    if (tokens.empty()) {
        cout << "true\n";
        return 0;
    }

    // Build tree from level order
    TreeNode* root = nullptr;
    if (tokens[0] != "null") {
        root = new TreeNode(stoi(tokens[0]));
    } else {
        cout << "true\n"; // empty tree is valid BST
        return 0;
    }

    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < tokens.size()) {
        TreeNode* node = q.front();
        q.pop();

        // Left child
        if (i < tokens.size() && tokens[i] != "null") {
            node->left = new TreeNode(stoi(tokens[i]));
            q.push(node->left);
        }
        i++;

        // Right child
        if (i < tokens.size() && tokens[i] != "null") {
            node->right = new TreeNode(stoi(tokens[i]));
            q.push(node->right);
        }
        i++;
    }

    cout << (isValidBST(root, LONG_MIN, LONG_MAX) ? "true" : "false") << "\n";
    return 0;
}