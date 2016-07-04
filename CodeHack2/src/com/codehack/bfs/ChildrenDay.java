package com.codehack.bfs;
import java.util.ArrayList; 
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class ChildrenDay {
    private static Scanner sc;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	String digits = sc.next();
        	int n = sc.nextInt();
        	int m = sc.nextInt();
        	
        	System.out.println( gifts(digits.toCharArray(), n, m) );
        }
	}

	private static String gifts(char[] digits, int n, int m) {
		Arrays.sort(digits);
		
		ArrayList<Integer> parent = new ArrayList<Integer>();
		ArrayList<Integer> choiceDigits = new ArrayList<Integer>();
		Queue<Integer> vertexs = new LinkedList<Integer>();

		for (int i = 0; i < 2*n; i++) {
			parent.add(-1);
			choiceDigits.add(-1);
		}
		
		parent.set( 0, 0 );
		vertexs.add( 0 );

		//	BFS
		while( !vertexs.isEmpty() )	{
			int here = vertexs.poll();

			for (int i = 0; i < digits.length; i++) {
				int there = append( here, (int)digits[i]-'0', n );
				
				if( parent.get(there) == -1 )	{
					parent.set(there, here);
					choiceDigits.set(there, (int)digits[i]-'0');

					vertexs.add(there);
				}
			}
		}

		if( parent.get(n+m) == -1 )	return "IMPOSSIBLE";	//	not reach m by append(based on %n)
		
		String ret = "";
		int here = n + m;	//	should start child's first vertex, 9 + 8 = 17 * 2 = 34
		while( parent.get(here) != here )	{	//	1 cycle
			ret += choiceDigits.get(here);
			here = (int)parent.get(here);
		}
		
		return (new StringBuffer(ret)).reverse().toString();
	}

	private static int append(int here, int edge, int mod) {
		int there = here * 10 + edge;
		if( there >= mod )	return mod + there % mod;
		
		return there % mod;
	}
}
