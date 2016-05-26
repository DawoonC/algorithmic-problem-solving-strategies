package com.codehack.bst;
import java.util.Scanner;
import java.util.TreeMap;

public class Nerd2 {
    private static Scanner sc;
    private static TreeMap<Integer, Integer> coords = new TreeMap<Integer, Integer>();
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	int personSum = 0;
        	coords.clear();
        	int applicantNum = sc.nextInt();
        	for (int i = 0; i < applicantNum; i++) {
        		int quizNum = sc.nextInt();
        		int ramenNum = sc.nextInt();
        		
        		personSum += registered( quizNum, ramenNum );
			}
        	
        	System.out.println( personSum );
        }
	}

	private static int registered(int x, int y) {
		if( isDominated(x, y) )	return coords.size();
		
		removeDominated(x, y);
		coords.put(x, y);
		
		return coords.size();
	}

	private static boolean isDominated(int x, int y) {
		if( coords.isEmpty() )	return false;
		
		if( coords.ceilingKey(x) != null )	{
			int rightMinKey = coords.ceilingKey(x);
			
			return coords.get(rightMinKey) > y;
		}
		else	return false;
	}

	private static void removeDominated(int x, int y) {
		if( coords.isEmpty() )	return;
		
		if( coords.floorKey(x) != null )	{
			int leftMaxKey = coords.floorKey(x);

			int nextKey = leftMaxKey;
			while( true )	{
				if( coords.get(nextKey) > y )	break;
				
				if( nextKey == coords.firstKey() )	{
					coords.remove( nextKey );
					break;
				}
				else	{
					coords.remove( nextKey );
					nextKey = coords.lowerKey(nextKey);	//	previous node key
				}
			}
		}
	}
}
