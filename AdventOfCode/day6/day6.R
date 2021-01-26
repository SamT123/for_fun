setwd('~/Desktop/learn/for_fun/AdventOfCode/day6/')
input = readLines('input.txt')
input_grouped = list(array(0, dim = c(26,0)));     rownames(input_grouped[[1]]) = letters

idx = 1
for (e in input){
  if (!(e == '')){
    add = as.logical(1:26 %in% which(letters %in% str_split(e, '')[[1]]))
    input_grouped[[idx]] = cbind(input_grouped[[idx]], add)
  } else{
    idx = idx + 1
    input_grouped[[idx]] = array(0, dim = c(26,0))
    rownames(input_grouped[[idx]]) = letters

  }
}



input_grouped %>% sapply(function(M) sum(apply(M,1, any))) %>% sum()

input_grouped %>% sapply(function(M) sum(apply(M,1, all))) %>% sum()


for (group_idx %in% seq_along(input_grouped)){
  M <- array(0, dim = c(26, length(group_sizes[[group_idx]])))

}
group_sizes

M = array(0, dim = c(26, ))

input_grouped %>% sapply(str_split, '') %>%

%>% lapply(unique)%>% sapply(length) %>% sum()
