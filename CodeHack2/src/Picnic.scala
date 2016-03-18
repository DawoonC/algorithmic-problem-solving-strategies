import scala.util.control.Breaks._

object Picnic {
  val areFriends = Array.ofDim[Boolean](10, 10)
//  val taken = new Array[Boolean](10)

  var stdNum = 0
  
  def main(args: Array[String]): Unit = {
    var cases = scala.io.StdIn.readInt()
    while (cases > 0) {
      stdNum = scala.io.StdIn.readLine.split(" ")(0).toInt  //  #std, #pair
      val pairs = scala.io.StdIn.readLine.split(" ")
      var idx = 0
      var x = 0
      pairs.map  { num =>
        if( idx % 2 == 1 )  {
          areFriends(x)(num.toInt) = true 
        }
        else  {
          x = num.toInt
        }
        idx += 1
      }
      
//      for( i <- 0 to 9 )  {
//        for ( j <- 0 to 9 )  {
//          println( i+","+j+": " + areFriends(i)(j) )
//        }
//      }

      val taken = new Array[Boolean](10)
      for( i <- 0 to 9 )  {
        taken(i) = true
      }
      for( i <- 0 to stdNum-1 )  {
        taken(i) = false
      }
      println( countPairs(taken) )
      
      cases -= 1
    }

    
    def countPairs(taken:Array[Boolean]): Int = {
      var firstFree = -1
      
      breakable  {
        for( i <- 0 to stdNum-1 )  {
          if( !taken(i) )  {
            firstFree = i
//            println( "break: " + firstFree )
            break
          }
        }
      }

      //  base condition
      if( firstFree == -1 )  {
//        println( "base con!!!" )
        return 1
      }
      
      var count = 0
//      for( pairWith <- firstFree to stdNum-1 )  {
      for( pairWith <- firstFree+1 to stdNum-1 )  {
        if( !taken(pairWith) && areFriends(firstFree)(pairWith) )  {
//        if( !taken(pairWith) && areFriends(pairWith)(firstFree) )  {
          taken(firstFree) = true
          taken(pairWith) = true
          count += countPairs( taken )
          
          taken(firstFree) = false
          taken(pairWith) = false
        }
      }
      return count
    }
  }
}