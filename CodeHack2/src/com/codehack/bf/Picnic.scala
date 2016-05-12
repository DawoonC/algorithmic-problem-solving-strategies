package com.codehack.bf

import scala.util.control.Breaks._

object Picnic {
  val areFriends = Array.ofDim[Boolean](10, 10)
  var stdNum = 0
  
  def main(args: Array[String]): Unit = {
    var cases = scala.io.StdIn.readInt()
    while (cases > 0) {
      
      for( i <- 0 to 9 )  {
        for ( j <- 0 to 9 )  {
          areFriends(i)(j) = false
        }
      }
      
      stdNum = scala.io.StdIn.readLine.split(" ")(0).toInt  //  #std, #pair
      val pairs = scala.io.StdIn.readLine.split(" ")
      var idx = 0
      var x = 0
      pairs.map  { num =>
        if( idx % 2 == 1 )  {
          areFriends(x)(num.toInt) = true
          areFriends(num.toInt)(x) = true
        }
        else  {
          x = num.toInt
        }
        idx += 1
      }
      
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
            break
          }
        }
      }

      //  base condition
      if( firstFree == -1 )  {
        return 1
      }
      
      var count = 0
      for( pairWith <- firstFree+1 to stdNum-1 )  {
        if( !taken(pairWith) && areFriends(firstFree)(pairWith) )  {
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