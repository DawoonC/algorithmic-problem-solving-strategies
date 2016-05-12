package com.codehack.dp;
import java.util.Arrays;
import java.util.Scanner;

/*
 * 3
1
5
100
 * Q: All case of filling 2x1 squares in a 2xn square
 * Sol: tiling(n) = tiling(n-1) + tiling(n-2)
 */
public class Tiling2 {
    private static Scanner sc;
    static final int MAX_NUM = 101;
	private static final int MOD = 1000000007;
    
    static int[] cache = new int[MAX_NUM];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cache.length; i++) {
            	Arrays.fill(cache, -1);
			}
        	
        	int n = sc.nextInt();
        	System.out.println( tiling(n) );
        }
	}

	private static int tiling(int n) {
		if( n <= 1 )	return 1;
		if( cache[n] != -1 )	return cache[n];
		
		return cache[n] = (tiling(n-1) + tiling(n-2)) % MOD;
	}
}
