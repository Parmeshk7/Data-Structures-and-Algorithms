/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getMin(TreeNode *root){
        if(root == NULL)
            return -1;
        if(root->left == NULL)
            return root->val;
        return getMin(root->left);
    }
    
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(root == NULL)
            return root;
        if(key > root->val)
            root->right = deleteNode(root->right, key);
        else if(key < root->val)
            root->left = deleteNode(root->left, key);
        else{
            if(root->left != NULL && root->right != NULL){
                int minVal = getMin(root->right);
                root->val = minVal;
                root->right = deleteNode(root->right, minVal);
            }
            else if(root->left != NULL)
                return root->left;
            else
                return root->right;
        }
        return root;
    }
};


