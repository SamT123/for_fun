n = 1
muls = c(3,5)
alts = c('Fizz', 'Buzz')
while (n <= 100){
  output = ""
  for (i in 1:length(muls)){
    if (n%%muls[i] == 0){
      output = paste0(output, alts[i])
    }
  }
  if (output == ""){print(n)}
  else {print(output)}
  n = n+1
}
