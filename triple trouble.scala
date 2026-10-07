def tripleDouble(num1: Long, num2: Long): Int = {
  val s1 = num1.toString
  val s2 = num2.toString
  for (n <- 0 to 9) {
    if (s1.contains(s"$n$n$n")) && (s2.contains(s"$n$n")) then
    { 
      return 1
      }
}
       return 0
  
  
}
