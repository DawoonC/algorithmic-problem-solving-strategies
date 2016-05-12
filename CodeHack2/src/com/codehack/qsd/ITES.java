package com.codehack.qsd;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

//	8791 20
public class ITES {
    private static Scanner sc;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	int sumK = sc.nextInt();
        	int numSignal = sc.nextInt();

        	System.out.println( countRange(sumK, numSignal) );
        }
	}

	private static int countRange(int sumK, int numSignal) {
		// generate signals
		RNG rng = new RNG();
		
		Queue<Integer> queue = new LinkedList<Integer>();
		int rangeSum = 0;
		int count = 0;
		
		for (int i = 0; i < numSignal; i++) {
			int newSignal = rng.next();
			
			rangeSum += newSignal;
			queue.add( newSignal );
			
			while( rangeSum > sumK )	{
				rangeSum -= queue.remove();
			}
			
			if( rangeSum == sumK )	count++;
		}
		
		return count;
	}
}

//	1984, 8791, 4770, 7665, 3188
class RNG	{
	private long seed;
	
	public RNG()	{
		this.seed = 1983L;
	}

	public int next() {
		long ret = seed;
		seed = ( (seed * 214013L) + 2531011L ) % (long)Math.pow(2, 32);
		
		return (int) (ret % 10000 + 1);
	}
	
}
