setwd('~/Desktop/learn/for_fun/AdventOfCode/day1/')
library(dplyr)
library(matrixStats)
### pt 1

nums = scan('nums.txt')

# dplyr
expand.grid(nums, nums) %>% mutate(sum = Var1 + Var2) %>% filter(sum == 2020) %>% mutate(prod = Var1*Var2)
outer(nums, nums, FUN = `+`) # alternative


# without dups
combos = t(combn(nums,3))
i = which(rowSums(combos) == 2020)
combos[i,]


### pt 2

# dplyr
expand.grid(nums, nums, nums) %>% mutate(sum = Var1 + Var2 + Var3) %>% filter(sum == 2020) %>% mutate(prod = Var1*Var2*Var3)
outer(nums, nums, FUN = `+`) # alternative


# without dups
combos = t(combn(nums,3))
i = which(rowSums(combos) == 2020)
prod(combos[i,])
