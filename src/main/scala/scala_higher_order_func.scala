object higher_order_func{
  def sum(f:Int=>Int, a:Int, b:Int): Int =
    if (a>b) 0 else f(a) + sum(f, a+1, b)
  
  def id(x:Int): Int = x
  def main(args:Array[String]){
    assert(sum(id, 1, 10) == 55)
  }
}
