#include <iostream>
#include <queue>
using namespace std;

class Node{
    int data;
    Node *left, *right;

public: 
    Node(int d){
        data = d;
        left = NULL;
        right = NULL;
    }

    friend class Tree;
};

class Tree{
Node* head;

public:
    Tree(){
        head = NULL;
    }

    void insert(int, Node*);
    void bfs(Node*);
    void dfs(Node*);
    void inorder(Node*);
    Node* get_head(){
        return head;
    }
    
};

void Tree::insert(int d, Node* temp){
    
    if(temp==NULL){
        head = new Node(d);
        return;
    }

    if(temp->left != NULL && d < temp->data){

        insert(d, temp->left);
    }

    else if(temp->right != NULL && d > temp->data){

        insert(d, temp->right);
    }

    else if(temp->left == NULL && d < temp->data)
        temp->left = new Node(d);
    
    else if(temp->right == NULL && d > temp->data)
        temp->right = new Node(d);
    
}


void Tree::dfs(Node* temp){
    // Same as Post-Order Traversal
    if(temp != NULL){
        dfs(temp->left);
        dfs(temp->right);
        cout<<temp->data<<" ";
    }
        
}

void Tree::bfs(Node *temp){
    if(temp != NULL){
        queue<Node*> q;
        q.push(temp);

        while(q.empty() == false){
            Node* n = q.front();
            cout<<n->data<<" ";
            q.pop();

            if(n->left != NULL){
                q.push(n->left);
            }
            
            if(n->right != NULL){
                q.push(n->right);
            }
        }
    }
}


void Tree::inorder(Node* temp){
    if(temp!=NULL){
        inorder(temp->left);
        cout<<temp->data<<" ";
        inorder(temp->right);
        
    }

}


int main(){

Tree t;

t.insert(8, t.get_head());
t.insert(4, t.get_head());
t.insert(6, t.get_head());
t.insert(1, t.get_head());
t.insert(15, t.get_head());
t.insert(2, t.get_head());

t.dfs(t.get_head());

    return 0;
}
















