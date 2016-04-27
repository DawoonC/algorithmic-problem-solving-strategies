import java.util.Arrays;
import java.util.Scanner;

/*
 * 4
1
1 1 
1 1 1 
1 1 1 1 
 * Q: 
 * Sol: 
 */
public class Tripathcnt {
    private static Scanner sc;
    static final int MAX_NUM = 100;
    static int[][] cntCache = new int[MAX_NUM][MAX_NUM];
    static int[][] triCache = new int[MAX_NUM][MAX_NUM];
    
	private static int triSize;
	private static int[][] triMatrix = new int[MAX_NUM][MAX_NUM];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cntCache.length; i++) {
            	Arrays.fill(cntCache[i], -1);
			}
        	
        	for (int i = 0; i < triCache.length; i++) {
            	Arrays.fill(triCache[i], -1);
			}
        	
        	triSize = sc.nextInt();
        	//	make triangle
            int height = triSize;
            for (int i = 0; i < triSize; i++) {
            	for (int j = 0; j < triSize; j++) {
            		if( j < triSize-height + 1 )	{
            			triMatrix[i][j] = sc.nextInt();
            		}
            		else	triMatrix[i][j] = 0;
				}
            	height -= 1;
			}
            
        	System.out.println( countPath(0, 0) );
        }
	}

	private static int countPath(int y, int x) {
		if( y == triSize-1 )	return 1;
		if( cntCache[y][x] != -1 )	return cntCache[y][x];
		
		cntCache[y][x] = 0;	//	init for sum counts
		if( path2(y+1, x+1) >= path2(y+1, x) )	cntCache[y][x] += countPath( y+1, x+1 );
		if( path2(y+1, x+1) <= path2(y+1, x) )	cntCache[y][x] += countPath( y+1, x );
		
		return cntCache[y][x];
	}

	private static int path2(int y, int x) {
		if( y == triSize-1 )	return triMatrix[y][x];
		if( triCache[y][x] != -1 )	return triCache[y][x];
		
		return triCache[y][x] = Math.max( path2(y+1, x+1), path2(y+1, x) ) + triMatrix[y][x];
	}

}
