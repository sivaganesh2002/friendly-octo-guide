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

// Helper function to check if the tree is a valid BST
bool isValidBST(TreeNode* root, long minVal, long maxVal) {
    if (!root) return true;
    if (root->val <= minVal || root->val >= maxVal) return false;
    return isValidBST(root->left, minVal, root->val) &&
           isValidBST(root->right, root->val, maxVal);
}

int main() {
    vector<string> input;
    string val;
    while (cin >> val) {
        input.push_back(val);
    }

    if (input.empty()) {
        cout << "true\n";
        return 0;
    }

    // Build tree from level-order input
    TreeNode* root = nullptr;
    if (input[0] != "null") {
        root = new TreeNode(stoi(input[0]));
    } else {
        cout << "true\n";
        return 0;
    }

    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < input.size()) {
        TreeNode* node = q.front();
        q.pop();

        // Left child
        if (i < input.size() && input[i] != "null") {
            node->left = new TreeNode(stoi(input[i]));
            q.push(node->left);
        }
        i++;

        // Right child
        if (i < input.size() && input[i] != "null") {
            node->right = new TreeNode(stoi(input[i]));
            q.push(node->right);
        }
        i++;
    }

    cout << (isValidBST(root, LONG_MIN, LONG_MAX) ? "true" : "false") << "\n";
    return 0;
}