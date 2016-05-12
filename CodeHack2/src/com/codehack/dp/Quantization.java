package com.codehack.dp;
import java.util.Arrays;
import java.util.Scanner;

/*
 * Q: a progression(a1, a2, a3, a4, a5) -> if 2type nums, (A, A, B, B, B)
 * given, min( sigma((input-output)^2) )
 * Sol: 
 */
public class Quantization {
    private static Scanner sc;
    static final int MAX_NUM = 100;
	private static final int INF = 987654321;
    static int inputSize = 0;
    
    static int types = 0;
    static String inputStr = "";
    static int[][] cache = new int[MAX_NUM+1][11];
	static int[] inputNums;
	private static int[] pSum;
	private static int[] pSqSum;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cache.length; i++) {
            	Arrays.fill(cache[i], -1);
			}
        	
        	inputSize = sc.nextInt();
        	types = sc.nextInt();
        	inputNums = new int[inputSize];
        	pSum = new int[inputSize];
        	pSqSum = new int[inputSize];
        	for (int i = 0; i < inputSize; i++) {
				inputNums[i] = sc.nextInt();
			}
        	precalc();
        	
            System.out.println( quantize(0, types) );
        }
	}

	//	pre-cal sub-part sums
	private static void precalc() {
		Arrays.sort( inputNums );
//		for (int i = 0; i < inputNums.length; i++) {
//			System.out.println( inputNums[i] );
//		}
		
		pSum[0] = inputNums[0];
		pSqSum[0] = inputNums[0] * inputNums[0];
		for (int i = 1; i < inputSize; i++) {
			pSum[i] = pSum[i-1] + inputNums[i];
			pSqSum[i] = pSqSum[i-1] + inputNums[i] * inputNums[i];
		}
	}

	private static int quantize(int from, int types) {
		if( from == inputSize )	return 0;	//	end of series.
		if( types == 0 )	return INF;		//	can't grouping
		
		if( cache[from][types] != -1 )	return cache[from][types];
		cache[from][types] = INF;
		
		for (int partSize = 1; from+partSize <= inputSize; partSize++) {
			cache[from][types] = Math.min( cache[from][types], minError(from, from+partSize-1) +
					quantize(from+partSize, types-1) );
		}
		
		return cache[from][types];
	}

	private static int minError(int lo, int hi) {
		int sum = pSum[hi] - (lo == 0 ? 0 : pSum[lo-1]);
		int sqSum = pSqSum[hi] - (lo == 0 ? 0 : pSqSum[lo-1]);
		
		int m = (int)(0.5 + (double)sum / (hi-lo+1));
		int ret = sqSum - (2 * m * sum) + (m * m * (hi-lo+1));	//	Cal errors: sigma( num[i] - avg ) ^ 2 => A^2 -2AB _ B^2
		
		return ret;
	}

}
