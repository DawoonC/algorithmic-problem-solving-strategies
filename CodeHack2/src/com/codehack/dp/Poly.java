package com.codehack.dp;
import java.util.Arrays;
import java.util.Scanner;

public class Poly {
    private static Scanner sc;
    static final int MAX_NUM = 100;
	private static final int MOD = 10000000;
    
    static int[][] cache = new int[MAX_NUM+1][MAX_NUM+1];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cache.length; i++) {
            	Arrays.fill(cache[i], -1);
			}
        	
        	int size = sc.nextInt();
        	long total = 0;
        	for (int i = 1; i <= size; i++) {
				total += poly(size, i);
			}
        	System.out.println( total % MOD );
        }
	}

	private static int poly(int n, int first) {
		if( n == first )	return 1;
		if( cache[n][first] != -1 )	return cache[n][first];
		
		cache[n][first] = 0;
		for (int second = 1; second <= n-first; second++) {
			int addCase = second + first - 1;
			addCase = addCase * poly( n-first, second );
			addCase = addCase % MOD;
			cache[n][first] = cache[n][first] + addCase;
			cache[n][first] = cache[n][first] % MOD;
		}
		
		return cache[n][first];
	}

}
