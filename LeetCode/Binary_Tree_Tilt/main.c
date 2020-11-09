/* main.c */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int tilt(struct TreeNode* node){
    int sum = 0, left = 0, right = 0;
    if (node->left != NULL){
        left = tilt(node->left);
    }
    if (node->right != NULL){
        right = tilt(node->right);
    }
    sum = node->val + left + right;
    node->val = abs(left - right);
    return sum;
}

int sum(struct TreeNode* node){
    if (node != NULL){
        return node->val + sum(node->left) + sum(node->right);
    }
    return 0;
}

int findTilt(struct TreeNode* root){
    if (!root){
        return 0;
    } else {
        tilt(root);
        return sum(root);
    }
}
