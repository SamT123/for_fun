rm(list = ls())
setwd('~/Desktop/learn/for_fun/AdventOfCode/day2/')

pws = readLines('input.txt')
pws_example = c('1-3 a: abcde',
                '1-3 b: cdefg',
                '2-9 c: ccccccccc')

parse_pw = function(pw_char){

  spl = strsplit(pw_char, '-')[[1]]
  min = spl[[1]]
  pw_char = spl[[2]]

  spl = strsplit(pw_char, ' ')[[1]]
  max = spl[[1]]
  pw_char = paste0(spl[-1], collapse = '')

  spl = strsplit(pw_char, ':')[[1]]
  let = spl[[1]]
  pw_char = spl[[2]]

  pw = strsplit(pw_char, ' ')[[1]][[1]]

  return(list(min = as.numeric(min), max = as.numeric(max), let = let, pw = pw))
}

check_pw_ex1 = function(pw_list){
  split_pw = strsplit(pw_list$pw, '')[[1]]
  cnt = sum(split_pw == pw_list$let)
  return(cnt >= pw_list$min & cnt <= pw_list$max)
}

check_pw_ex2 = function(pw_list){
  split_pw = strsplit(pw_list$pw, '')[[1]]
  pos1 = (split_pw[[pw_list$min]] == pw_list$let)
  pos2 = (split_pw[[pw_list$max]] == pw_list$let)

  return(sum(pos1, pos2) == 1)
}

count_passes  = function(pws_vec, check_fn) {
  parsed = lapply(pws_vec, parse_pw)
  passed = sapply(parsed, check_fn)
  passes = sum(passed)
  passes
}

count_passes(pws, check_pw_ex1)
count_passes(pws, check_pw_ex2)

check_pw(parse_pw(pws[[1]]))
strsplit(pws_example[[1]], '')
