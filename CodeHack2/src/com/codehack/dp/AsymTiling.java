package com.codehack.dp;
import java.util.Arrays;
import java.util.Scanner;

public class AsymTiling {
    private static Scanner sc;
    static final int MAX_NUM = 100;
	private static final int MOD = 1000000007;
    static int triWidth = 0;
    
    static int[] cache = new int[MAX_NUM+1];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cache.length; i++) {
            	Arrays.fill(cache, -1);
			}
        	
        	triWidth = sc.nextInt();
        	
        	//	All(Sym+Asym) tiling: tiling(n) = tiling(n-1) + tiling(n-2)
        	//	Asym tiling: all_tiling(n) - sym_tiling(n)
        	//	Sym tiling(n is odd): all_tiling(n) - tiling(n/2)
        	//	Sym tiling(n is even): all_tiling(n) - tiling(n/2) - tiling(n/2-1)
            System.out.println( asymTiling(triWidth) );
        }
	}

	private static int asymTiling(int width) {
		if( width%2 == 1 )	return (tiling(width) - tiling(width/2) + MOD) % MOD;
		
		int ret = tiling( width );
		ret = (ret - tiling(width/2) + MOD) % MOD;
		ret = (ret - tiling(width/2-1) + MOD) % MOD;
		
		return ret;
	}

	private static int tiling(int width) {
		if( width <= 1 )	return 1;
		if( cache[width] != -1 )	return cache[width];
		
		return cache[width] = (tiling(width-1) + tiling(width-2)) % MOD;
	}
}
