import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class LIS {
    private static Scanner sc;
    static final int MAX_NUM = 500;
    static int inputSize = 0;
    static int[] cache = new int[MAX_NUM];
    static int[] cache2 = new int[MAX_NUM+1];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        ArrayList<Integer> numList = new ArrayList<Integer>();
        
        while(cases-- > 0) {
        	Arrays.fill(cache, -1);
        	Arrays.fill(cache2, -1);
        	
        	numList.clear();
        	
            inputSize = sc.nextInt();
            for (int i = 0; i < inputSize; i++) {
				numList.add( sc.nextInt() );
			}

            System.out.println( lis3(numList, -1) - 1 );
            
//            int maxLen = 0;
//            for (int begin = 0; begin < inputSize; begin++) {
//				maxLen = Math.max( maxLen, lis2(numList, begin) );
//			}
//            System.out.println( maxLen );
            
//            System.out.println( lis2(numList, 0) );
//            System.out.println( lis(numList) );
        }
	}

	private static int lis3(ArrayList<Integer> numList, int start) {
		if( cache2[start+1] != -1 )	return cache2[start+1];
		int ret = 1;
		for (int next = start+1; next < inputSize; next++) {
			if( start == -1 || numList.get(start) < numList.get(next) )	{
				cache2[start+1] = Math.max( ret, lis3(numList, next) + 1 );
				ret = cache2[start+1];
			}
		}
		
		return ret;
	}

	private static int lis2(ArrayList<Integer> numList, int start) {
		if( cache[start] != -1 )	return cache[start];
		int ret = 1;
		for (int next = start+1; next < inputSize; next++) {
			if( numList.get(start) < numList.get(next) )
				cache[start] = Math.max( ret, lis2(numList, next) + 1 );
				ret = cache[start];
		}
		
		return ret;
	}

	private static int lis(ArrayList<Integer> numList) {
		if( numList.isEmpty() )	return 0;

		ArrayList<Integer> numList2 = new ArrayList<Integer>();
		int ret = 0;
		for (int i = 0; i < numList.size(); i++) {
			for (int j = i+1; j < numList.size(); j++) {
				if( numList.get(i) < numList.get(j) )	numList2.add( numList.get(j) );
				ret = Math.max( ret, 1 + lis(numList2) );
			}
		}
		
		return ret;
	}
}
