package com.codehack.dp;
import java.util.Arrays;
import java.util.Scanner;

/*
모든 숫자가 같을 때 (예: 333, 5555) 난이도: 1
숫자가 1씩 단조 증가하거나 단조 감소할 때 (예: 23456, 3210) 난이도: 2
두 개의 숫자가 번갈아 가며 출현할 때 (예: 323, 54545) 난이도: 4
숫자가 등차 수열을 이룰 때 (예: 147, 8642) 난이도: 5
그 외의 경우 난이도: 10

원주율의 일부가 입력으로 주어질 때, 난이도의 합을 최소화하도록 숫자들을 3자리에서 5자리까지 끊어 읽고 싶습니다. 최소의 난이도를 계산하는 프로그램을 작성하세요.

sol) min( len(3)'s min + classify(n-3), len(4)'s min + classify(n-4), len(5)'s min + classify(n-5) )
 */
public class PI {
    static final int MAX_NUM = 10000;
	private static final int INF = 987654321;

    private static Scanner sc;
    static int[] cache = new int[MAX_NUM+2];
    private static String inputStr;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	Arrays.fill(cache, -1);
        	inputStr = sc.next();
        	
            System.out.println( memorize(0) );
        }
	}
	
	private static int memorize(int begin) {
		// base cond
		if( begin == inputStr.length() )	return 0;
		
		if( cache[begin] != -1 )	return cache[begin];

		int ret = INF;
		for (int len = 3; len <= 5; len++) {
			if( begin+len <= inputStr.length() )	{
				cache[begin+len] = Math.min( ret, memorize(begin+len)+classify(begin, begin+len) );
				ret = cache[begin+len];
			}
		}
		
		return ret;
	}
	
	//	return hardness of [a, b]
	private static int classify(int a, int b) {
		char[] m = inputStr.substring( a, b ).toCharArray();
		
		boolean sameChars = true;
		for (int i = 0; i < m.length; i++) {
			if( m[0] != m[i] )	{
				sameChars = false;
				break;
			}
		}
		if( sameChars )	return 1;
		
		boolean progressive = true;
		for (int i = 0; i < m.length-1; i++) {
			if( m[i+1]-m[i] != m[1]-m[0] )	progressive = false;
		}
		if( progressive && Math.abs(m[1]-m[0]) == 1 )	return 2;
		
		boolean alternating = true;
		for (int i = 0; i < m.length; i++) {
			if( m[i] != m[i%2] )	alternating = false;
		}
		
		if( alternating )	return 4;
		if( progressive )	return 5;
		
		return 10;
	}

}
