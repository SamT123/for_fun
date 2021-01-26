
setwd('~/Desktop/learn/for_fun/AdventOfCode/day5/')

library(compositions)

getpos <- function(s){
  s %>% str_sub(start = 1, end = 7) %>% str_replace_all('F', '0') %>% str_replace_all('B', '1') %>% unbinary() -> row
  s %>% str_sub(start =8, end = 10) %>% str_replace_all('L', '0') %>% str_replace_all('R', '1') %>% unbinary() -> col
  return(c(row, col))
}

getid <- function(pos){
  return(pos[[1]]*8 + pos[[2]])
}

getpos('BFFFBBFRRR') %>% getid()

input = readLines('input.txt')

input %>% lapply(getpos) %>% sapply(getid) %>% max()

input %>% lapply(getpos) %>% sapply(getid) -> ids

(49:806)[which.min( 49:806 %in% sort(ids) )]

input[[757]] %>% getpos()
str_sub(input[[757]], start =7, end = 10)
