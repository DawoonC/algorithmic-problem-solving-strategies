package com.codehack.dp;
import java.util.Arrays;
import java.util.Scanner;

public class TrianglePath2 {
    private static Scanner sc;
	private static int triSize;
	private static int[][] tri;
	private static int[][] cache;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	triSize = sc.nextInt();

        	cache = new int[triSize][triSize];
        	for (int i = 0; i < triSize; i++) {
        		Arrays.fill( cache[i], -1 );
			}
        	
        	tri = new int[triSize][triSize];
        	for (int i = 0; i < triSize; i++) {
				for (int j = 0; j <= i; j++) {
					tri[i][j] = sc.nextInt();
				}
			}
        	
        	System.out.println( triPath(0, 0) );
        }
	}

	private static int triPath(int y, int x) {
		if( y == triSize )	return 0;
		
		if( cache[y][x] != -1 )	return cache[y][x];
		cache[y][x] = Math.max( triPath(y+1, x), triPath(y+1, x+1) ) + tri[y][x];
		
		return cache[y][x];
	}

}
