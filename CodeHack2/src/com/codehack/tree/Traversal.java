package com.codehack.tree;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//7
//27 16 9 12 54 36 72	pre-order
//9 12 16 27 36 54 72	in-order
//12 9 16 36 72 54 27	<post-order>
public class Traversal {
    private static Scanner sc;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        int nodeNum = 0;

		ArrayList<Integer> preOrder;
		ArrayList<Integer> inOrder;
        
        while(cases-- > 0) {
        	nodeNum = sc.nextInt();

    		preOrder = new ArrayList<Integer>(nodeNum);
    		inOrder = new ArrayList<Integer>(nodeNum);
        	
        	for (int i = 0; i < nodeNum; i++) {
				preOrder.add( sc.nextInt() );
			}
        	
        	for (int i = 0; i < nodeNum; i++) {
				inOrder.add( sc.nextInt() );
			}
        	
        	printPostOrder( preOrder, inOrder );
        }
	}

	private static void printPostOrder(List<Integer> preOrder, List<Integer> inOrder) {
		int size = preOrder.size();
		if( preOrder.isEmpty() )	{
//			System.out.print( "e " );
			return;
		}

		int root = preOrder.get(0);	//	get root
		int leftSubSize = inOrder.indexOf(new Integer(root));
		
		printPostOrder( preOrder.subList(1, leftSubSize+1), inOrder.subList(0, leftSubSize) );			//	left(sub) print
		printPostOrder( preOrder.subList(leftSubSize+1, size), inOrder.subList(leftSubSize+1, size) );	//	right(sub) print
		System.out.print( root + " " );																	//	root print
	}

}
