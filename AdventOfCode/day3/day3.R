setwd('~/Desktop/learn/for_fun/AdventOfCode/day3/')

input = readLines("input.txt")
M = do.call(rbind, lapply(input, function(x) {strsplit(x, '')[[1]]}))
M


get_trees = function(M, increment){
  pos = c(1,1)
  trees = 0
  while(pos[[1]] <= dim(M)[[1]]){

    if (M[ pos[[1]], pos[[2]] ] == '#') trees = trees + 1
    pos = pos + increment
    if (pos[[2]] > dim(M)[[2]]) pos[[2]] = pos[[2]] - dim(M)[[2]]
  }
  trees
}


get_trees(M, c(1,3))
get_trees(M, c(1,1)) * get_trees(M, c(1,3)) * get_trees(M, c(1,5)) * get_trees(M, c(1,7)) * get_trees(M, c(2,1))
