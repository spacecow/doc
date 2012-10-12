object func_overloading{
  def balance(chars:List[Char]){
    println("balancing...") //balancing...
  }
  def balance(s:String): Unit = balance(s.toList)

  def main(args:Array[String]){
    balance("test")
  }
}
