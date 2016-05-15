package com.codehack.tree;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Fortress {
    private static Scanner sc;
    static int wallNum;
    static int[] x;
    static int[] y;
    static int[] r;
	private static int longest;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	longest = 0;
        	wallNum = sc.nextInt();
        	x = new int[wallNum];
        	y = new int[wallNum];
        	r = new int[wallNum];
        	
        	for (int i = 0; i < wallNum; i++) {
				x[i] = sc.nextInt();
				y[i] = sc.nextInt();
				r[i] = sc.nextInt();
			}
        	
        	TreeNode tree = getTree(0);
        	System.out.println( solve(tree) );
        }
	}

	private static int solve(TreeNode root) {
		longest = 0;
		int h = height( root );
		
		return Math.max(longest, h);
	}

	private static int height(TreeNode root) {
		ArrayList<Integer> heights = new ArrayList<Integer>();
		
		for (int i = 0; i < root.children.size(); i++) {
			heights.add( height(root.children.get(i)) );
		}
		
		if( heights.isEmpty() )	return 0;

		//	sort heights...
        Collections.sort( heights, new Comparator<Integer>(){
			@Override
			public int compare(Integer o1, Integer o2) {
				return o1 < o2 ? -1 : o1 > o2 ? 1 : 0;
			}
        });

		if( heights.size() >= 2 )
			longest = Math.max(longest, 
					2 + heights.get(heights.size()-2) + heights.get(heights.size()-1) );
		
		return heights.get( heights.size()-1 ) + 1;	//	get last
	}

	private static TreeNode getTree(int root) {
		TreeNode ret = new TreeNode();
		for (int i = 0; i < wallNum; i++) {
			if( isChild(root, i) )
				ret.children.add( getTree(i) );
		}
		
		return ret;
	}

	private static boolean isChild(int parent, int child) {
		if( !encloses(parent, child) )	return false;
		
		for (int i = 0; i < wallNum; i++) {
			if( i != parent && i != child &&
					encloses(parent, i) && encloses(i, child) )
				return false;
		}
		
		return true;
	}

	private static boolean encloses(int a, int b) {
		return r[a] > r[b] &&
				sqrtDist(a, b) < sqr(r[a] - r[b]);
	}

	private static int sqrtDist(int a, int b) {
		return sqr(y[a]-y[b]) + sqr(x[a]-x[b]);
	}

	private static int sqr(int x) {
		return x * x;
	}

}

class TreeNode	{
	ArrayList<TreeNode> children;
	
	public TreeNode()	{
		this.children = new ArrayList<TreeNode>();
	}
}
