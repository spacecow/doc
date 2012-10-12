object map_reduce{
  def map_reduce(f:Int=>Int, combine:(Int, Int)=>Int, zero:Int)(a:Int, b:Int): Int =
    if (a>b) zero
    else combine(f(a), map_reduce(f, combine, zero)(a+1, b))

  def product(f:Int=>Int)(a:Int, b:Int): Int = map_reduce(f, (x, y)=>x*y, 1)(a, b)
  def factorial(n:Int) = product(x=>x)(1,n)

  def sum(f:Int=>Int)(a:Int, b:Int): Int = map_reduce(f, (x, y)=>x+y, 0)(a, b)

  def main(args:Array[String]){
    assert(product(x=>x)(1,5) == 120)
    assert(factorial(5) == 120)
    assert(sum(x=>x)(1,5) == 15)
  }
}
