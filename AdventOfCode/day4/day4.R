library(stringr)

setwd('~/Desktop/learn/for_fun/AdventOfCode/day4/')

input = readLines("input.txt")
input

entries = list()
entries_idx = 1
for (l in input){
  if (is.null(entries[entries_idx][[1]])){
    entries[entries_idx] = l
    print(entries)
  } else{
    entries[entries_idx] = paste(entries[entries_idx], l)
  }
  if (l == "") entries_idx = entries_idx + 1
}


entries %>% lapply(trimws) %>% str_split(' ') %>% lapply(str_split, ':') -> entries_split


# get fields
entries_split %>% lapply(function(s){sapply(s, function(ss) return(ss[[1]]))}) -> fields
reqd_fields = c("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt")


sum(sapply(fields, function(entry){all(reqd_fields %in% entry)}))


entries_split %>% lapply(function(entry){
  l = list()
  for (e in entry){
    l[[e[[1]]]] = e[[2]]
  }
  return(l)
}) -> pplist


pp.isvalid = function(pp){
  fields = names(pp)
  if (!all(reqd_fields %in% fields)) return(F)

  byr_bool = as.numeric(pp$byr) >= 1920 & as.numeric(pp$byr) <= 2002
  iyr_bool = as.numeric(pp$iyr) >= 2010 & as.numeric(pp$iyr) <= 2020
  eyr_bool = as.numeric(pp$eyr) >= 2020 & as.numeric(pp$eyr) <= 2030

  hgt_unit = str_sub(pp$hgt,-2,-1)
  hgt_num = str_sub(pp$hgt, 1, -3)
  hgt_unit_bool = hgt_unit %in% c('in', 'cm')
  if (!hgt_unit_bool) return(F)
  if (hgt_unit == 'cm') hgt_num_bool = as.numeric(hgt_num) >= 150 & as.numeric(hgt_num) <= 193
  if (hgt_unit == 'in') hgt_num_bool = as.numeric(hgt_num) >= 59 & as.numeric(hgt_num) <= 76

  hcl_bool = (str_sub(pp$hcl, 1, 1) == '#') & all(str_split(pp$hcl,'')[-1] %in% c(letters, 1:9))
  eyc_bool = pp$ecl %in% c('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
  pid_bool = str_length(pp$pid) == 9 & as.numeric(pp$pid)
  c(iyr_bool, byr_bool, eyr_bool, hgt_unit_bool, hgt_num_bool, hcl_bool, eyc_bool, pid_bool) %>% sapply(isTRUE) %>% all() -> pass
  return(pass)
}

pplist %>% sapply(pp.isvalid) %>% sum

entries_split[[4]][[1]][1]



reqd_fields %in% fields[[3]]
reqd_fields


entries %>% str_split(' ')
