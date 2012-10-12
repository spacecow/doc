object func_default_value{
  def balance(chars:List[Char], n:Int = 0){
    println("balancing...") //balancing...
  }

  def main(args:Array[String]){
    balance("test".toList)
  }
}
