import java.util.Arrays;
import java.util.Scanner;

public class TrianglePath {
    private static Scanner sc;
    static int triSize = 0;
    static final int MAX_NUM = 257;
    static int[][] triMatrix = new int[100][100];
//    static int[][][] cache = new int[100][100][MAX_NUM*100+1];
    static int[][] cache2 = new int[100][100];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            triSize = sc.nextInt();
            
//            for (int i = 0; i < 100; i++) {
//				for (int j = 0; j < 100; j++) {
//		            Arrays.fill(cache[i][j], -1);
//				}
//			}
            
            for (int i = 0; i < 100; i++) {
	            Arrays.fill(cache2[i], -1);
			}
            
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
            
//            for (int i = 0; i < triSize; i++) {
//            	for (int j = 0; j < triSize; j++) {
//            		System.out.print( triMatrix[i][j] );
//				}
//            	System.out.println("");
//			}
            
            System.out.println( path2(0, 0) );
//            System.out.println( path1(0, 0, 0) );
        }
	}

	private static int path2(int y, int x) {
		if( y == triSize-1 )	return triMatrix[y][x];
		if( cache2[y][x] != -1 )	return cache2[y][x];
		
		return cache2[y][x] = Math.max(path2(y+1, x), path2(y+1, x+1)) + triMatrix[y][x];
	}

//	private static int path1(int y, int x, int sum) {
//		if( y == triSize-1 )	return sum + triMatrix[y][x];
//		
//		if( cache[y][x][sum] != -1 )	return cache[y][x][sum];
//		sum += triMatrix[y][x];
//		return cache[y][x][sum] = Math.max(path1(y+1, x+1, sum), path1(y+1, x, sum));
//	}
}
