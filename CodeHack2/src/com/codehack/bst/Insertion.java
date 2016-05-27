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

	private static TreapNode delete(TreapNode root, int key) {
		if( root == null )	return root;
		
		if( root.key == key )	{
			TreapNode ret = merge( root.left, root.right );
			return ret;
		}
		
		if( key < root.key )	{
			root.setLeft( delete(root.left, key) );
		}
		else	{
			root.setRight( delete(root.right, key) );
		}
		
		return root;
	}

	private static TreapNode merge(TreapNode a, TreapNode b) {
		if( a == null )	return b;
		if( b == null )	return a;
		if( a.priority < b.priority )	{
			b.setLeft( merge(a, b.left) );
			return b;
		}
		
		a.setRight( merge(a.right, b) );
		return a;
	}

	private static TreapNode insert(TreapNode root, TreapNode node) {
		if( root == null )	return node;	//	base condition
		
		if( root.priority < node.priority )	{	//	replace node by new node
			NodePair splitted = split( root, node.key );
			node.setLeft( splitted.first );
			node.setRight( splitted.second );
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
		
		if( root.key < key )	{
			NodePair rs = split( root.right, key );
			root.setRight( rs.first );
			return new NodePair( root, rs.second );
		}
		
		NodePair ls = split( root.left, key );
		root.setLeft( ls.second );
		return new NodePair( ls.first, root );
	}

}

class NodePair	{
	public TreapNode first;
	public TreapNode second;

	public NodePair(TreapNode first, TreapNode second) {
		this.first = first;
		this.second = second;
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
