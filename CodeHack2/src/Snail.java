import java.util.Arrays;
import java.util.Scanner;

public class Snail {
    private static Scanner sc;
    static final int MAX_NUM = 1000;
    static int depth = 0;
    static int rainDays = 0;
    
    static double[][] cache = new double[MAX_NUM][MAX_NUM*2+1];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cache.length; i++) {
            	Arrays.fill(cache[i], -1);
			}
        	
        	depth = sc.nextInt();
        	rainDays = sc.nextInt();
        	
        	//	climb(days, climbed) = climb(days+1, climbed+2)*0.75 + climb(days+1, climbed+1)*0.25
            System.out.println( String.format("%.10f", climb(0, 0)) );
        }
	}

	private static double climb(int days, int climbed) {
		if( days == rainDays )	return (climbed >= depth ? 1 : 0);
		if( cache[days][climbed] != -1 )	return cache[days][climbed];
		
		return cache[days][climbed] = (climb(days+1, climbed+2)*0.75) + (climb(days+1, climbed+1)*0.25);
	}
}
