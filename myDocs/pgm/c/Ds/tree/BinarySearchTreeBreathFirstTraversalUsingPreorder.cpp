#include "stdio.h"
#include "stdlib.h"
#include "iostream"
// #define true  1
// #define false 0
using namespace std;

struct BST
{
	char data;
	struct BST *left;
	struct BST *right;
};

struct BST* GetNewNode(char data)
{
	// struct BST* rootNode=(struct BST*)malloc(sizeof(struct BST));
	BST *rootNode=new BST();
	rootNode->data=data;
	rootNode->left=rootNode->right=NULL;
	return rootNode;
}

struct  BST* InsertNode(struct BST* root,char data)
{
	if(root==NULL)
	{
		root=GetNewNode(data);
	}
	else if(data<=root->data)
	{
		root->left=InsertNode(root->left,data);
	}
	else
	{
		root->right=InsertNode(root->right,data);
	}
	return root;
}

bool Search(struct BST* root,char data)
{
	if(root==NULL) return false;
	else if(data==root->data) return true;
	else if(data<=root->data) return Search(root->left,data); 
	else return Search(root->right,data);
}

void PreOrder(BST* root)
{
	if(root==NULL) return;
	printf("%c\t",root->data);
	PreOrder(root->left);
	PreOrder(root->right);	
}

int main(int argc, char const *argv[])
{

	printf("hello manohar\n");
	struct BST *root=NULL;


	root=InsertNode(root,'F');
	root=InsertNode(root,'D');
	root=InsertNode(root,'J');
	root=InsertNode(root,'B');
	root=InsertNode(root,'E');                         
	root=InsertNode(root,'G');
	root=InsertNode(root,'K');
	root=InsertNode(root,'A');
	root=InsertNode(root,'C');
	root=InsertNode(root,'I');
	root=InsertNode(root,'H');


	PreOrder(root);
	
	char ele;

	printf("\n%s\n","Enter the elements to Search" );
	cin>>ele;
	// scanf("%d",&ele);

/*	if(Search(root,ele)== true)	printf("%s%d\n","elements found " , ele);
	else
		printf("Not found\n" );*/

	if(Search(root,ele)== true)	cout <<"Elements found ",ele,"\n";
	else
		cout << "elements not found.." <<endl;
	printf("\n" );
	return 0;
}