package com.codehack.dp;
import java.util.ArrayList; 
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class WildCard {
    private static Scanner sc;
    
    static int[][] cache = new int[100][100];

	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            String pattern = sc.next();
            
            int strCnt = sc.nextInt();
            String[] strList = new String[strCnt];
            ArrayList<String> retList = new ArrayList<String>();
            for (int i = 0; i < strCnt; i++) {
            	strList[i] = sc.next();
			}
            
            for (int i = 0; i < strCnt; i++) {
                for (int ii = 0; ii < 100; ii++) {
                	for (int jj = 0; jj < 100; jj++) {
                		cache[ii][jj] = -1;
    				}
    			}

//                if( matchMemo2(pattern, strList[i], 0, 0) == 1 )	{
                if( matchMemo(pattern, strList[i], 0, 0) == 1 )	{
                	retList.add( strList[i] );
                }
//                System.out.println( match(pattern, strList[i] ));
//                System.out.println( matchMemo(pattern, strList[i], 0, 0) );
//                System.out.println( matchMemo2(pattern, strList[i], 0, 0) );
			}
            
            Collections.sort( retList, new Comparator<String>(){
            	public int compare(String obj1, String obj2)	{
                      return obj1.compareToIgnoreCase(obj2);
                }
            });
            
            for (String string : retList) {
				System.out.println( string );
			}
        }
    }

	private static int matchMemo(String str1, String str2, int w, int s) {
		if( cache[w][s] != -1 )	return cache[w][s];
		
		char[] pattern = str1.toCharArray();
		char[] str = str2.toCharArray();
		
		while( s < str.length && w < pattern.length &&
				(pattern[w] == '?' || pattern[w] == str[s]) )	{
			++w;
			++s;
		}
		
		if( w == pattern.length )	{
			int ret = -1;
			if( s == str.length )	ret = 1;
			else	ret = 0;
			
			cache[w][s] = ret;
			
			return ret; 
		}
		
		if( pattern[w] == '*' )	{
			for (int skip = 0; skip < str.length; skip++) {
				if( matchMemo(str1, str2, w+1, s+skip) == 1 )	return cache[w][s] = 1;
			}
		}
		
		return cache[w][s] = 0;
	}

	
	private static int matchMemo2(String str1, String str2, int w, int s) {
		if( cache[w][s] != -1 )	return cache[w][s];
		
		char[] pattern = str1.toCharArray();
		char[] str = str2.toCharArray();
		
		if( s < str.length && w < pattern.length &&
				(pattern[w] == '?' || pattern[w] == str[s]) )	{
			return cache[w+1][s+1] = matchMemo2(str1, str2, w+1, s+1);
		}
		
		if( pattern[w] == '*' )	{
			if( (matchMemo2(str1, str2, w+1, s)==1) ||
					(s < str.length && (matchMemo2(str1, str2, w, s+1)==1)) )
				return cache[w][s] = 1;
		}
		
		return cache[w][s] = 0;
	}

	private static boolean match(String str1, String str2) {
		int pos = 0;
		char[] pattern = str1.toCharArray();
		char[] str = str2.toCharArray();
		
		while( pos < str.length && pos < pattern.length &&
				(pattern[pos] == '?' || pattern[pos] == str[pos]) )
			++pos;
		
		if( pos == pattern.length )	return pos == str.length;
		
		if( pattern[pos] == '*' )	{
			for (int skip = 0; pos+skip <= str.length; skip++) {
				if( match(str1.substring(pos+1), str2.substring(pos+skip)) )	return true;
			}
		}
		
		return false;
	}

}
