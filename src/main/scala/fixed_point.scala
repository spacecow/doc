import math.abs

object jmath{
  def fixedPoint(f:Double=>Double)(firstGuess:Double) = {
    val tolerance = 0.0001
    def isCloseEnough(x:Double, y:Double) =
      abs(x-y) < tolerance
    def iterate(guess:Double): Double = {
      println(guess)
      val next = f(guess) 
      if (isCloseEnough(guess,next)) next
      else iterate(next) 
    }
    iterate(firstGuess)
  }
  def averageDamp(f:Double=>Double)(x:Double) = (x + f(x))/2
  def sqrt(x:Double) = fixedPoint(averageDamp(y=>x/y))(1)
}
