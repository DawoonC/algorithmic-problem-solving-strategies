package com.codehack.dq;
import java.util.Scanner;

public class Fence {
    private static Scanner sc;

	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            int panjaNum = sc.nextInt();
            int[] panjaHeight = new int[panjaNum];
            for (int i = 0; i < panjaHeight.length; i++) {
            	panjaHeight[i] = sc.nextInt();
			}
            
            System.out.println( solve(panjaHeight, 0, panjaNum-1) );
        }
    }

	private static int solve(int[] panjaHeight, int left, int right) {
		if( left == right )	return panjaHeight[left];
		int mid = (left + right) / 2;
		
		//	normal case
		int retVal = Math.max( solve(panjaHeight, left, mid), solve(panjaHeight, mid+1, right) );
		
		//	cross case
		int low = mid;
		int hi = mid+1;
		int height = Math.min( panjaHeight[low], panjaHeight[hi] );
		retVal = Math.max( retVal, height*2 );
		
		while( left < low || hi < right )	{
			if( hi < right && (low == left || panjaHeight[low-1] < panjaHeight[hi+1]) )	{
				++hi;
				height = Math.min(height, panjaHeight[hi] );
			}
			else	{
				--low;
				height = Math.min(height, panjaHeight[low] );
			}
			retVal = Math.max( retVal, height*(hi-low+1) );
		}
		
		return retVal;
	}

}
