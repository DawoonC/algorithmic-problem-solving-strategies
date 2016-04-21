import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class JLIS {
    private static Scanner sc;
    static final int MAX_NUM = 100;
    static int inputSize1 = 0;
    static int inputSize2 = 0;
    static int[][] cache = new int[MAX_NUM+1][MAX_NUM+1];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        ArrayList<Integer> numList1 = new ArrayList<Integer>();
        ArrayList<Integer> numList2 = new ArrayList<Integer>();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cache.length; i++) {
            	Arrays.fill(cache[i], -1);
			}
        	
        	numList1.clear();
        	numList2.clear();
        	
            inputSize1 = sc.nextInt();
            inputSize2 = sc.nextInt();
            for (int i = 0; i < inputSize1; i++) {
				numList1.add( sc.nextInt() );
			}
            
            for (int i = 0; i < inputSize2; i++) {
				numList2.add( sc.nextInt() );
			}

            System.out.println( jlis(numList1, numList2, -1, -1) - 2 );
        }
	}

	private static int jlis(ArrayList<Integer> numList1, ArrayList<Integer> numList2, int idx1, int idx2) {
		if( cache[idx1+1][idx2+1] != -1 )	return cache[idx1+1][idx2+1];
		
		int ret = 2;
		long a = (idx1 == -1 ? Long.MIN_VALUE : numList1.get(idx1) );
		long b = (idx2 == -1 ? Long.MIN_VALUE : numList2.get(idx2) );
		long maxElem = Math.max(a, b);
		
		for (int next1 = idx1+1; next1 < inputSize1; next1++) {
			if( maxElem < numList1.get(next1) )	{
				cache[idx1+1][idx2+1] = Math.max( ret, jlis(numList1, numList2, next1, idx2) + 1 );
				ret = cache[idx1+1][idx2+1];
			}
		}
		
		for (int next2 = idx2+1; next2 < inputSize2; next2++) {
			if( maxElem < numList2.get(next2) )	{
				cache[idx1+1][idx2+1] = Math.max( ret, jlis(numList1, numList2, idx1, next2) + 1 );
				ret = cache[idx1+1][idx2+1];
			}
		}
		
		return ret;
	}
}
