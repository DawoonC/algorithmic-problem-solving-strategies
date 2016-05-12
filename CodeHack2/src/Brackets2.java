import java.util.Scanner;
import java.util.Stack;

public class Brackets2 {
    private static Scanner sc;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	char[] formula = sc.next().toCharArray();
        	if( wellMatched(formula) )	System.out.println("YES");
        	else	System.out.println("NO");
        }
	}

	private static boolean wellMatched(char[] formula) {
		Stack<Character> openStack = new Stack<Character>();
		
		for (int i = 0; i < formula.length; i++) {
			if( formula[i] == '(' || formula[i] == '{' || formula[i] == '[' )	{	//	open brackets
				openStack.push( formula[i] );
			}
			else	{	//	close brackets
				if( openStack.isEmpty() )	return false;
				char pop = openStack.pop();
				switch (pop) {
				case '(':
					if( formula[i] != ')' )	return false;
					break;
				case '{':
					if( formula[i] != '}' )	return false;
					break;
				case '[':
					if( formula[i] != ']' )	return false;
					break;
				}
			}
		}
		
		return openStack.isEmpty();
	}

}
