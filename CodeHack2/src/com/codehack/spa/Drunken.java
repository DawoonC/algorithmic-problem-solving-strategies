package com.codehack.spa;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Drunken {
	static class Pair {
		private int cost;
		private int here;

		public Pair(int cost, int here) {
			this.cost = cost;
			this.here = here;
		}
	}
	
	static class ComparatorPair implements Comparator<Pair> {
	    @Override
	    public int compare(Pair o1, Pair o2) {
	        if(o1.cost > o2.cost){
	            return 1;
//	            return -1;
	        } else if (o1.cost == o2.cost){
	            return 0;
	        } else {
	            return -1;
//	            return 1;
	        }
	    }
	}
	
    private static Scanner sc;
	private static int[] delay;
	private static int[][] distance;
	private static int[][] adj;
	private static int vNum;
	private static int eNum;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
    	vNum = sc.nextInt();
    	eNum = sc.nextInt();
    	
    	delay = new int[vNum];
    	distance = new int[vNum][vNum];
    	adj = new int[vNum][vNum];
    	
    	Arrays.fill( delay, 9999999 );
    	for (int i = 0; i < vNum; i++) {
    		Arrays.fill( distance[i], 9999999 );
    		Arrays.fill( adj[i], 9999999 );
		}
    	
    	for (int i = 0; i < vNum; i++) {
			delay[i] = sc.nextInt();
		}
    	
    	for (int i = 0; i < eNum; i++) {
    		int u = sc.nextInt()-1;
    		int v = sc.nextInt()-1;
    		int w = sc.nextInt();
			adj[u][v] = w;
			adj[v][u] = w;
		}

    	solve();
    	
        int cases = sc.nextInt();
        while(cases-- > 0) {
        	System.out.println( distance[sc.nextInt()-1][sc.nextInt()-1] );        	
        }
	}

	private static void solve() {
		Pair[] order = new Pair[vNum];
		
		for (int i = 0; i < vNum; i++) {
			order[i] = new Pair(delay[i], i);
		}
	
		Arrays.sort( order, new ComparatorPair() );
//		for (int i = 0; i < order.length; i++) {
//			System.out.print( order[i].cost );
//		}
//		System.out.println( " " );
		
		
		for (int i = 0; i < vNum; i++) {
			for (int j = 0; j < vNum; j++) {
				if( i == j )	distance[i][j] = 0;
				else	distance[i][j] = adj[i][j];
			}
		}
		
		for (int k = 0; k < vNum; k++) {
			int w = order[k].here;
			for (int i = 0; i < vNum; i++) {
				for (int j = 0; j < vNum; j++) {
					adj[i][j] = Math.min( adj[i][j], adj[i][w]+adj[w][j] );
					distance[i][j] = Math.min( adj[i][w]+delay[w]+adj[w][j], distance[i][j] );
				}
			}
		}
	}
}
