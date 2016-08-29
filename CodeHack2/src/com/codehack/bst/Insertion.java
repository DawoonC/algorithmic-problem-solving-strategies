package com.codehack.bst;
import java.util.Scanner;

public class Insertion {
    private static Scanner sc;
	private static int[] shifted = new int[50000];
	private static int[] origianl = new int[50000];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	int nums = sc.nextInt();
        	for (int i = 0; i < nums; i++) {
				shifted [i] = sc.nextInt();
			}
        	
        	solve( nums );
        	
        	for (int i = 0; i < nums; i++) {
				System.out.print( origianl[i] + " " );
			}
        	System.out.println(" ");
        }
	}

	private static void solve( int nums ) {
		TreapNode candidates = null;
		for (int i = 0; i < nums; i++) {
			candidates = insert( candidates, new TreapNode(i+1) );
		}
		
		for (int i = nums-1; i >= 0; --i) {
			int larger = shifted[i];
			TreapNode k = kth( candidates, i+1 - larger );	//	all# - larger# = #th, 5-3=2th
			origianl[i] = k.key;
			candidates = delete( candidates, k.key );
		}
	}

	private static TreapNode kth(TreapNode root, int k) {
		int leftSize = 0;
		if( root.left != null )	leftSize = root.left.size;
		if( k <= leftSize )	return kth(root.left, k);
		if( k == leftSize+1 )	return root;
		
		return kth( root.right, k-leftSize-1 );
	}

	//	키값 비교 => 우선순위 비교
	private static TreapNode delete(TreapNode root, int key) {
		if( root == null )	return root;
		
		if( root.key == key )	{
			//	root 삭제 후 남은 sub-tree들을 병합
			TreapNode newRoot = merge( root.left, root.right );
			return newRoot;
		}
		
		//	삭제할 node를 찾으러 recursion
		if( key < root.key )	{
			root.setLeft( delete(root.left, key) );
		}
		else	{
			root.setRight( delete(root.right, key) );
		}
		
		return root;
	}

	//	
	private static TreapNode merge(TreapNode leftTreap, TreapNode rightTreap) {
		if( leftTreap == null )	return rightTreap;
		if( rightTreap == null )	return leftTreap;
		
		//	rightTreap이 root가 되어야 함 (leftTreap은 어디로? 그래서 merge가 필요)
		//	leftTreap과 rightTreap의 left가 merge 되어야 함
		if( leftTreap.priority < rightTreap.priority )	{
			rightTreap.setLeft( merge(leftTreap, rightTreap.left) );
			return rightTreap;
		}
		
		//	leftTreap이 root가 되어야 함
		leftTreap.setRight( merge(leftTreap.right, rightTreap) );
		return leftTreap;
	}

	//	우선순위 비교 => 키값 비교
	private static TreapNode insert(TreapNode root, TreapNode node) {
		if( root == null )	return node;	//	base condition
		
		if( root.priority < node.priority )	{	//	replace node by new node
			NodePair splitted = split( root, node.key );
			node.setLeft( splitted.smaller );
			node.setRight( splitted.bigger );
			return node;
		}
		else if( node.key < root.key )	{	//	node < root => insert sub-left w/ recursion 
			root.setLeft( insert(root.left, node) );
		}
		else	{	//	node > root => insert sub-right w/ recursion
			root.setRight( insert(root.right, node) );
		}
		
		return root;
	}

	private static NodePair split(TreapNode root, int key) {
		if( root == null )	return new NodePair( null, null );
		//	node가 없을때까지 recursion
		//	최종 결과: new 기준, 작은트립과 큰트립으로 나뉨(기존 root는 어딘가에 포함, 더이상 root가 아님)
		
		if( root.key < key )	{
			//	root보다 new가 크면, new보다 큰것을 찾기위해 right를 split
			//	split 후 큰것은 new에 주고, 작은것은 자신의 오른쪽에(right를 split했으므로)
			NodePair rs = split( root.right, key );
			root.setRight( rs.smaller );
			return new NodePair( root, rs.bigger );
		}

		//	root보다 new가 작으면, new보다 작은것을 찾기위해 left를 split
		//	split 후 작은것은 new에 주고, 큰것은 자신의 왼쪽에(left를 split했으므로)
		NodePair ls = split( root.left, key );
		root.setLeft( ls.bigger );
		return new NodePair( ls.smaller, root );
	}

}

//	first: treap nodes < new.key, second: treap nodes >= new.key
class NodePair	{
	public TreapNode smaller;
	public TreapNode bigger;

	public NodePair(TreapNode first, TreapNode second) {
		this.smaller = first;
		this.bigger = second;
	}
	
}

class TreapNode	{
	int key;
	double priority;
	int size;
	TreapNode left;
	TreapNode right;

	public TreapNode(int key) {
		this.key = key;
		this.size = 1;
		this.priority = Math.random();
		this.left = null;
		this.right = null;
	}

	public void setRight(TreapNode newRight) {
		right = newRight;
		calcSize();
	}

	public void setLeft(TreapNode newLeft) {
		left = newLeft;
		calcSize();
	}

	private void calcSize() {
		size = 1;
		if( left != null )	size += left.size;
		if( right != null )	size += right.size;
	}
}
