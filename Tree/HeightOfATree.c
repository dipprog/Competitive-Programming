#include<stdio.h>

/*

				D
			   / \
			  /   \
			 /     \
			A       F
		   / \     / \
		  /   \   /   \
		 E     B R	   T
		/ \     /     / \
	   G   Q   V     J   L

*/

int complete_node = 15;

char tree[] = {'\0', 'D', 'A', 'F', 'E', 'B', 'R', 'T', 'G', 'Q', '\0', '\0', 'V', '\0', 'J', 'L' };

int get_left_child(int index)
{
	//node is not null
	// and the result must lie within the number of nodes for a complete binary tree
	if(tree[index] != '\0' && (2*index) <= complete_node )
		return (2*index);
	// left child doesn't exist
	return -1;
}


int get_right_child(int index)
{
	//node is not null
	// and the result must lie within the number of nodes for a complete binary tree
	if(tree[index] != '\0' && (2*index + 1) <= complete_node )
		return (2*index + 1);
	// right child doesn't exist
	return -1;
}

int is_leaf(int index){
	// to check the indices of the left and right children are valid or not
	if(!get_left_child(index) && !get_right_child(index))
		return 1;
	// to check if both the children of the node are null or not
	if(tree[get_left_child(index)]=='\0' && tree[get_right_child(index)]== '\0')
		return 1;
	return 0;// node is not a leaf	
}

int get_max(int a, int b){
	return (a > b) ? a : b;
}

int get_height(int index)
{
	// if the node is a leaf the height will be zero
	// the height will be 0 also for the invalid cases
	if(tree[index]=='\0' || index <=0 || is_leaf(index))
		return 0;
	// height of the node i is 1 + maximum among the height of left subtree and right subtree
	return(get_max(get_height(get_left_child(index)), get_height(get_right_child(index))) + 1);	
}

int main()
{
	printf("Height of the given tree: %d\n",get_height(1));
	return 0;
}
