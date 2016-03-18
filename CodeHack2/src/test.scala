object Main {
  def main(args: Array[String]): Unit = {
//    var cases = Integer.parseInt(readLine())
    var cases = scala.io.StdIn.readInt()
    while (cases > 0) {
//      println("Hello, " + readLine() + "!")
      println("Hello, " + scala.io.StdIn.readLine + "!")
      cases -= 1
    }
  }
}