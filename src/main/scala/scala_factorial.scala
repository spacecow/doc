object algorithms_factorial{
  def factorial(n:Int): Int = {
    def loop(acc:Int, n:Int): Int = 
      if (n==0) acc 
      else loop(acc*n, n-1)
    loop(1, n) 
  }
  def main(args:Array[String]){
    assert(factorial(4) == 24)
  } 
}
