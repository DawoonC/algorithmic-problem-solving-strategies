package com.codehack.lds;
import java.util.LinkedList;
import java.util.Scanner;

//	6 3
//	123456 -> (1)23456 -> (1)23(4)56 -> (1)(2)3(4)56 -> (1)(2)3(4)5(6)
public class Josephus {
    private static Scanner sc;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	josephus( sc.nextInt(), sc.nextInt() );
        }
	}

	private static void josephus(int numMans, int interval) {
		LinkedList<Integer> survivors = new LinkedList<Integer>();
		for (int i = 1; i <= numMans; i++) {
			survivors.add(i);
		}
		int killIdx = 0;
		
		while( survivors.size() > 2 )	{
			int idx = killIdx %= survivors.size();
			survivors.remove( idx );
			killIdx += (interval-1);
		}
		
		System.out.println( survivors.getFirst() + " " + survivors.getLast() );
	}

}
