#include "stdio.h"
#include "stdlib.h"
#define true  1
#define false 0

struct BST
{
	int data;
	struct BST *left;
	struct BST *right;
};

struct BST* GetNewNode(int data)
{
	struct BST* rootNode=(struct BST*)malloc(sizeof(struct BST));
	rootNode->data=data;
	rootNode->left=rootNode->right=NULL;
	return rootNode;
}

struct  BST* InsertNode(struct BST* root,int data)
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

int Search(struct BST* root,int data)
{
	if(root==NULL) return false;
	else if(data==root->data) return true;
	else if(data<=root->data) return Search(root->left,data); 
	else return Search(root->right,data);
}


int FindMin(struct BST* root)
{
	if(root==NULL) 
	{
		printf("tree is NULL\n");
		return -1;
	}
	else if(root->left==NULL)
	{
		return root->data;
	}
	return FindMin(root->left);  //  use recursive function
}

int FindMax(struct BST* root)
{
	if(root==NULL) 
	{
		printf("tree is empty\n");
		return -1;
	}
	else if(root->right==NULL)
	{
		return root->data;
	}
	return FindMax(root->right);  //  use recursive function
}
int main(int argc, char const *argv[])
{

	printf("hello manohar\n\n");
	struct BST *root=NULL;
	root=InsertNode(root,20);
	root=InsertNode(root,15);
	root=InsertNode(root,25);
	root=InsertNode(root,10);
	root=InsertNode(root,17);
	root=InsertNode(root,22);
	root=InsertNode(root,27);

	int ele;
	printf("%s\n","Enter the elements to Search" );
	scanf("%d",&ele);
	if(Search(root,ele)== true)	printf("%s%d\n","elements found " , ele);
	else
		printf("Not found\n" );

	int min=FindMin(root);
	printf("Min=%d\n",min);

	int max=FindMax(root);
	printf("Max=%d\n",max);
	return 0;
}