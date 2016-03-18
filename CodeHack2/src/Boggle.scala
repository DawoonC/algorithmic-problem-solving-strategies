/*
PRETTY YES
GIRL YES
REPEAT YES
KARA NO
PANDORA NO
GIAZAPX YES
 */
object Boggle {
//  val dx = Array( -1, -1, -1,  1, 1, 1,  0, 0 )
//  val dy = Array( -1,  0,  1, -1, 0, 1, -1, 1 )
//  val board = Array.ofDim[Char](5, 5)

  def main(args: Array[String]): Unit = {
//////////////////////////////////////////////////////    
//    val filename = "input.txt"
//    var cases = 0
//    for (line <- Source.fromFile(filename).getLines()) {
//      cases = Integer.parseInt(readLine())
//    }
//////////////////////////////////////////////////////
    val dx = Array( -1, -1, -1,  1, 1, 1,  0, 0 )
    val dy = Array( -1,  0,  1, -1, 0, 1, -1, 1 )
    val board = Array.ofDim[Char](5, 5)
    
    var cases = scala.io.StdIn.readInt()
    while (cases > 0) {
      for( lineCnt <- 0 to 4 ) {
        var idx = 0
        val line = scala.io.StdIn.readLine
        line.toCharArray.map { xChar =>
          board(lineCnt)(idx) = xChar
          idx += 1
        }
      }

      var wordCnt = scala.io.StdIn.readInt
      while( wordCnt > 0 )  {
        var isYes = false
        val word = scala.io.StdIn.readLine
        for( y <- 0 to 4 )  {
          for( x <- 0 to 4 )  {
            if( hasWord(y, x, word) )  {
              isYes = true
            }
          }
        }
        
        if( !isYes )  println( word + " NO" )
        else  println( word + " YES" )
        
        wordCnt -= 1
      }
      cases -= 1
    }

    def hasWord(x:Int, y:Int, word:String): Boolean = {
      if( !inRange(y, x) )  return false
      if( !board(y)(x).equals(word.charAt(0)) )  return false
      if( word.size == 1 )  return true
      
      for( direction <- 0 to 7 )  {
        var nextY = y + dy(direction)
        var nextX = x + dx(direction)
        if( hasWord(nextX, nextY, word.substring(1)) )  return true
      }
      return false
    }

    def inRange(y:Int, x:Int): Boolean = {
      return y >= 0 && y < 5 && x >= 0 && x < 5
    }
  }
}