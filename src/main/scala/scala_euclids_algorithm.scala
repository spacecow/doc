object algorithms{
  def euclids(a:Int, b:Int): Int = {
    if (b==0) a else euclids(b, a%b)
  }

  def main(args:Array[String]){
    assert(euclids(14,0) == 14)
    assert(euclids(14,21) == 7)
    assert(euclids(14,23) == 1)
  }
}
