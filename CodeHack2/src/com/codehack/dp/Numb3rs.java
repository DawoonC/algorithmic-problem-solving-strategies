package com.codehack.dp;
import java.util.Arrays;
import java.util.Scanner;

public class Numb3rs {
    private static Scanner sc;
    
    static double[][] cache = new double[51][101];
	private static int[][] connected = new int[51][51];
	private static int prison;
	private static int numCity;

	private static int[] deg = new int[51];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cache.length; i++) {
            	Arrays.fill(cache[i], -1);
			}
        	
        	numCity = sc.nextInt();
        	int days = sc.nextInt();
        	prison = sc.nextInt();
        	
        	//	make map
        	for (int i = 0; i < numCity; i++) {
        		for (int j = 0; j < numCity; j++) {
					connected[i][j] = sc.nextInt();
				}
			}

        	for (int i = 0; i < numCity; i++) {
            	int sum = 0;
				for (int j = 0; j < numCity; j++) {
					sum += connected[i][j];
				}
				deg[i] = sum;
			}
        	
        	int qSize = sc.nextInt();
        	for (int i = 0; i < qSize; i++) {
        		int qCity = sc.nextInt();
            	System.out.print( String.format("%.8f", search(qCity, days)) + " " );
			}
        	System.out.println("");
        }
	}

	private static double search(int here, int days) {
		if( days == 0 )	return (here == prison ? 1.0 : 0.0);
		if( cache[here][days] > -0.5 )	return cache[here][days];
		
		cache[here][days] = 0;
		for (int there = 0; there < numCity; there++) {
			if( connected[here][there] > 0 )	
				cache[here][days] += (search( there, days-1 ) / deg [there]);
		}
		
		return cache[here][days];
	}

}
