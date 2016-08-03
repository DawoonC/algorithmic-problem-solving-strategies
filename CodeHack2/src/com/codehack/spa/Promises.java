package com.codehack.spa;

import java.util.Arrays;
import java.util.Scanner;

public class Promises {
	private static Scanner sc;
	private static int cityNum;
	private static int roadNum;
	private static int willNum;
	private static int[][] adj;
	
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	cityNum = sc.nextInt();
        	roadNum = sc.nextInt();
        	willNum = sc.nextInt();
        	
        	adj = new int[cityNum][cityNum];
        	for (int i = 0; i < cityNum; i++) {
				Arrays.fill(adj[i], 9999999);
			}

        	for (int i = 0; i < roadNum; i++) {
        		int u = sc.nextInt();
        		int v = sc.nextInt();
        		int w = sc.nextInt();
				adj[u][v] = w;
				adj[v][u] = w;
			}

//        	printFloyd();
        	floyd();
//        	printFloyd();
        	
        	int ret = 0;
        	for (int i = 0; i < willNum; i++) {
        		int u = sc.nextInt();
        		int v = sc.nextInt();
        		int w = sc.nextInt();

        		if( !update(u, v, w) )	ret += 1;
			}
        	
        	System.out.println( ret );
        }
	}

	private static void floyd() {
		for (int i = 0; i < cityNum; i++) {
			adj[i][i] = 0;
		}

		for (int k = 0; k < cityNum; k++) {
			for (int i = 0; i < cityNum; i++) {
				for (int j = 0; j < cityNum; j++) {
					adj[i][j] = Math.min(adj[i][j], adj[i][k]+adj[k][j]);
				}
			}
		}
	}

	private static boolean update(int u, int v, int w) {
		if( adj[u][v] <= w )	return false;
		
		for (int i = 0; i < cityNum; i++) {
			for (int j = 0; j < cityNum; j++) {
				adj[i][j] = Math.min( adj[i][j], 
						Math.min(adj[i][u]+w+adj[v][j], adj[i][v]+w+adj[u][j]) );
			}
		}
		return true;
	}

	private static void printFloyd() {
		System.out.println( "===============" );
    	for (int i = 0; i < cityNum; i++) {
			for (int j = 0; j < cityNum; j++) {
				System.out.print(adj[i][j] + " ");
			}
			System.out.println("");
		}
	}
}
