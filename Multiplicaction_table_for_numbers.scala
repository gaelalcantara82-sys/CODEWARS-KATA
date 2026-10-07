def multiTable(n: Int): String = {
    var i = 1
    var resultado = ""
  for
    i <- 1 to 10
  do
      if i == 10 then
    resultado += s"$i * $n = " + i * n
      else
      resultado += s"$i * $n = " + i * n + "\n"
    i += 1
  return resultado
  
    
  
  
  
  
  
  
  
  
  
  
  
  
  
}
