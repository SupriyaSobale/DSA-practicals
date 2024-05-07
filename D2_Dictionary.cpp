#include <iostream>
using namespace std;

struct Entry {
    string keyword;
    string meaning;
    Entry* left;
    Entry* right;
    int height;
};

int getHeight(Entry* node) {
    if (node == NULL)
        return 0;
    return node->height;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

Entry* createEntry(string keyword, string meaning) {
    Entry* entry = new Entry;
    entry->keyword = keyword;
    entry->meaning = meaning;
    entry->left = NULL;
    entry->right = NULL;
    entry->height = 1;
    return entry;
}

Entry* rightRotate(Entry* y) {
    Entry* x = y->left;
    Entry* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;
    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;

    return x;
}

Entry* leftRotate(Entry* x) {
    Entry* y = x->right;
    Entry* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;

    return y;
}

int getBalance(Entry* node) {
    if (node == NULL)
        return 0;
    return getHeight(node->left) - getHeight(node->right);
}

Entry* insertEntry(Entry* root, string keyword, string meaning) {
    if (root == NULL)
        return createEntry(keyword, meaning);

    if (keyword < root->keyword)
        root->left = insertEntry(root->left, keyword, meaning);
    else if (keyword > root->keyword)
        root->right = insertEntry(root->right, keyword, meaning);
    else {
        cout << "Keyword already exists in the dictionary." << endl;
        return root;
    }

    root->height = 1 + max(getHeight(root->left), getHeight(root->right));

    int balance = getBalance(root);

    if (balance > 1 && keyword < root->left->keyword)
        return rightRotate(root);

    if (balance < -1 && keyword > root->right->keyword)
        return leftRotate(root);

    if (balance > 1 && keyword > root->left->keyword) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    if (balance < -1 && keyword < root->right->keyword) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

Entry* findMin(Entry* node) {
    Entry* current = node;
    while (current->left != NULL)
        current = current->left;
    return current;
}

void printEntries(Entry* root) {
    if (root != NULL) {
        printEntries(root->left);
        cout << "Keyword: " << root->keyword << ", Meaning: " << root->meaning << endl;
        printEntries(root->right);
    }
}

int main() {
    Entry* root = NULL;

    // Inserting entries into the dictionary
    root = insertEntry(root, "apple", "A fruit that grows on trees.");
    root = insertEntry(root, "banana", "A long curved fruit that grows in clusters.");
    root = insertEntry(root, "orange", "A citrus fruit with a tough orange skin and segments inside.");
    root = insertEntry(root, "pear", "A sweet fruit with a slightly gritty texture.");

    // Printing the dictionary entries
    cout << "Dictionary Entries:" << endl;
    printEntries(root);

    return 0;
}

