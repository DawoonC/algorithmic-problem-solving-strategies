package com.codehack.dp;
import java.util.Arrays;
import java.util.Scanner;

public class JumpGame {
    private static Scanner sc;
	private static int[][] cache;
	private static int[][] matrix;
	private static int size;

	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            size = sc.nextInt();

            cache = new int[size][size];
            for (int i = 0; i < cache.length; i++) {
            	Arrays.fill( cache[i], -1 );
			}
            
            matrix = new int[size][size];
            for (int i = 0; i < matrix.length; i++) {
            	for (int j = 0; j < matrix[0].length; j++) {
            		matrix[i][j] = sc.nextInt();
				}
			}

            if( jump(0, 0) > 0 )	System.out.println("YES");
            else	System.out.println("NO");
        }
    }

	//	base: x == y == matrix.size return true, x > matrix.size || y > matrix.size return false
	//	induction: jump(x+matrix[x][y], y) || jump(x, y+matrix[x][y]
	private static int jump(int y, int x) {
		if( x >= size || y >= size )	return 0;
		if( x == size-1 && y == size-1 )	return 1;
		
		if( cache[y][x] != -1 )	return cache[y][x];
		int jumpSize = matrix[y][x];
		
		int retVal = jump(y+jumpSize, x) + jump(y, x+jumpSize);
		cache[y][x] = retVal;
		
		if( retVal > 1 )	cache[y][x] = 1;
		
		return cache[y][x];
	}
}

