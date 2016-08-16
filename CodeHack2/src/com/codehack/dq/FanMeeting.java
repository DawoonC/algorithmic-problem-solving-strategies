package com.codehack.dq;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class FanMeeting {
    private static final int[] EMPTY = {};
	private static Scanner sc;
//	private static int callCnt;

	public static void main(String[] args) throws Exception {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            char[] members = sc.next().toCharArray();
            char[] fans = sc.next().toCharArray();
            
            System.out.println( hug(members, fans) );
        }
    }

	private static int hug(char[] members, char[] fans) throws Exception {
		int[] number1 = new int[members.length];
		int[] number2 = new int[fans.length];
		
		for (int i = 0; i < members.length; i++) {
			if( members[i] == 'M' )	number1[i] = 1;
			else	number1[i] = 0;
		}
		
		for (int i = 0; i < fans.length; i++) {
			if( fans[i] == 'M' )	number2[fans.length-i-1] = 1;
			else	number2[fans.length-i-1] = 0;
		}
		
//		for (int i = 0; i < number1.length; i++) {
//			System.out.print(number1[i]);
//		}
//		System.out.println( " " );
//		
//		for (int i = 0; i < number2.length; i++) {
//			System.out.print(number2[i]);
//		}
//		System.out.println( " " );
		
//		subFrom( number1, number2 );
//		for (int i = 0; i < number1.length; i++) {
//			System.out.print(number1[i]);
//		}
//		System.out.println( " " );

//		int[] ret = addTo( number1, number2, 1 );
//		for (int i = 0; i < ret.length; i++) {
//			System.out.print(ret[i]);
//		}
//		System.out.println( " " );

		
		int[] result = karatsuba( number1, number2 );
		
		int allHugs = 0;
		for (int i = members.length-1; i < fans.length; i++) {
			if( result[i] == 0 )	++allHugs;
		}
		
		return allHugs;
		
//		return 0;
	}

	private static int[] karatsuba(int[] number1, int[] number2) throws Exception {
//		if( callCnt > 10 )	throw new Exception();
//		callCnt++;
		int n1Len = number1.length;
		int n2Len = number2.length;
		
		if( n1Len < n2Len )	return karatsuba( number2, number1 );
		
		//	base conditions
		if( n1Len == 0 || n1Len == 0 )	return EMPTY;
		if( n1Len <= 50 )	return multiply( number1, number2 );	//	to normal process
		
		int half = n1Len / 2;
		
		//	z2 = a1 * b1;
		//	z0 = a0 * b0
		//	z1 = (a0 + a1) * (b0 + b1) - z0 - z2
		int[] a0 = Arrays.copyOf( number1, half );	//	params is cnt
		int[] a1 = Arrays.copyOfRange( number1, half, number1.length );	//	params are idx
		int[] b0 = Arrays.copyOf( number2, Math.min(half, number2.length) );	//	params is cnt
		int[] b1 = Arrays.copyOfRange( number2, Math.min(half, number2.length), number2.length );	//	params are idx
/*
		System.out.print("number1: ");
		for (int i = 0; i < number1.length; i++) {
			System.out.print( number1[i] );
		}
		System.out.println( " " );
		
		System.out.print("a0: ");
		for (int i = 0; i < a0.length; i++) {
			System.out.print( a0[i] );
		}
		System.out.println( " " );

		System.out.print("a1: ");
		for (int i = 0; i < a1.length; i++) {
			System.out.print( a1[i] );
		}
		System.out.println( " " );
*/
		
		//	z2 = a1 * b1;
		int[] z2 = karatsuba( a1, b1 );		
		
		//	z0 = a0 * b0
		int[] z0 = karatsuba( a0, b0 );
		
		//	z1 = (a0 + a1) * (b0 + b1) - z0 - z2
		a0 = addTo( a0, a1, 0 );	//	(a0+a1)
		b0 = addTo( b0, b1, 0 );	//	(b0+b1)
		int[] z1 = karatsuba( a0, b0 );
		
		subFrom( z1, z0 );
		subFrom( z1, z2 );
		
		int[] retVal = new int[number1.length+number2.length];
		retVal = addTo( retVal, z0, 0 );
		retVal = addTo( retVal, z1, half );
		retVal = addTo( retVal, z2, half+half );

/*		
		System.out.print("retVal: ");
		for (int i = 0; i < retVal.length; i++) {
			System.out.print( retVal[i] );
		}
		System.out.println( " " );
*/		
		return retVal;
	}

	//	a += b*(10^k)
	private static int[] addTo(int[] a, int[] b, int k) {
		int[] retVal;
		int[] newb = new int[b.length+k];
		for (int i = 0; i < newb.length; i++) {
			if( i > k )	newb[i] = b[i-k];
			else	newb[i] = 0;
		}
		
//		for (int i = 0; i < newb.length; i++) {
//			System.out.print(newb[i]);
//		}
//		System.out.println( " " );
		
		if( a.length > newb.length )	{
			retVal = new int[a.length];
			for (int i = 0; i < a.length; i++) {
				int sum = 0;
				if( i < newb.length )	sum = a[i] + newb[i];
				else	sum = a[i];

				if( sum >= 10 )	{
					int next = i+1;
					while( a[next] == 9 )	{
						a[next] = 0;
						next++;
					}
					a[next] = a[next] + 1;
				}
				retVal[i] = sum;
			}
		}
		else	{
			retVal = new int[newb.length];
			for (int i = 0; i < newb.length; i++) {
				int sum = 0;
				if( i < a.length )	sum = a[i] + newb[i];
				else	sum = newb[i];
				
				if( sum >= 10 )	{
					int next = i+1;
					while( newb[next] == 9 )	{
						newb[next] = 0;
						next++;
					}
					newb[next] = newb[next] + 1;
				}
				retVal[i] = sum;
			}
		}
		
		return retVal;
	}

	//	a -= b, assume a >= b, if not arrayidx exception!!!
	private static void subFrom(int[] a, int[] b) {
		for (int i = 0; i < b.length; i++) {
			if( a[i] < b[i] )	{
				a[i] = 10 - b[0];
				int next = i+1;
				while( a[next] == 0 )	{
					a[next] = 9;
					next++;
				}
				a[next] = a[next] - 1;
			}
			else	{
				a[i] = a[i] - b[i];
			}
		}
	}
	
	private static int[] multiply(int[] number1, int[] number2) {
		int[] result = new int[number1.length+number2.length+1];
		Arrays.fill( result, 0 );
		
		for (int i = 0; i < number1.length; i++) {
			for (int j = 0; j < number2.length; j++) {
				result[i+j] += number1[i] * number2[j];
			}
		}
		
//		ArrayList<Integer> ret = normalize( result );
//		int[] nRet = new int[ret.size()];
//		for (int i = 0; i < ret.size(); i++) {
//			nRet[i] = ret.get(i);
//		}
//		
//		return nRet;
		
		return result;
	}

	private static ArrayList<Integer> normalize(int[] numArray) {
		ArrayList<Integer> number = new ArrayList<Integer>(numArray.length);
		for (int i = 0; i < numArray.length; i++) {
			number.add( numArray[i] );			
		}
		number.add( 0 );

		for (int i = 0; i < number.size(); i++) {
			int n1 = number.get(i).intValue();
			int n2 = number.get(i+1).intValue();

			if( n1 < 0 )	{
				int borrow = (Math.abs(n1)+9) / 10;
				number.set( i+1, n2-borrow );
				number.set( i, n1+(borrow*10) );
//				number[i+1] = number[i+1] - borrow;
//				number[i] = number[i] + (borrow * 10);
			}
			else	{
				number.set( i+1, n2+(n1/10) );
				number.set( i, n1%10 );
//				number[i+1] = number[i+1] + (number[i] / 10);
//				number[i] = number[i] % 10;
			}
		}

		while( number.size() > 1 && number.get(number.size()-1) == 0 )	{
			number.remove( number.size()-1 );
		}
		
		return number;
/*		
		for (int i = 0; i < number.length; i++) {
			if( number[i] < 0 )	{
				int borrow = (Math.abs(number[i])+9) / 10;
				number[i+1] -= borrow;
				number[i] += (borrow * 10);
			}
			else	{
				number[i+1] += (number[i] / 10);
				number[i] %= 10;
			}
		}
*/		
	}

}
