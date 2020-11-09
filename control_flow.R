# if statements
condition = T
if (condition) print("true_action") else print("false_action")

# if also returns a value so you can use for assignment:

x1 <- if (T) 1 else 2
x2 <- if (F) 1 else 2
x1; x2

# if you use an if statement without an else, NULL is returned if condition = FALSE. In turn, null is dropped by print, c(), etc:
greet <- function(name, birthday = FALSE) {
  paste0(
    "Hi ", name,
    if (birthday) " and HAPPY BIRTHDAY"
  )
}
greet("Maria", FALSE)
#> [1] "Hi Maria"
greet("Jaime", TRUE)
#> [1] "Hi Jaime and HAPPY BIRTHDAY"

# invalid inputs: input must evaluate to a single true/false, except for logical vector of length > 1

# vectorized if:
## use ifelse():
x = 1:20
ifelse(x %% 2 == 0, "even", "odd") # useful to have yes and no vecotrs of same type, otherwise output type hard to predict

## case_when is another good option:

library(dplyr)
y <- 1:50
dplyr::case_when(
  x %% 35 == 0 ~ "fizz buzz",
  x %% 5 == 0 ~ "fizz",
  x %% 7 == 0 ~ "buzz",
  is.na(x) ~ "???",
  TRUE ~ as.character(x) # 'else'
)

# switch()
## alternative to many if ... else if ... else if

x_option <- function(x) {
  if (x == "a") {
    "option 1"
  } else if (x == "b") {
    "option 2" 
  } else if (x == "c") {
    "option 3"
  } else {
    stop("Invalid `x` value")
  }
}

x_option_sw <- function(x) {
  switch(x,
         a = "option 1",
         b = "option 2",
         c = "option 3",
         stop("Invalid `x` value") # last option must return error, otherwise invisibile NULL is returned
  )
}

x_option('a')
x_option_sw('a')


# there is 'fall through' behaviour:
legs <- function(x) {
  switch(x,
         cow = ,
         horse = ,
         dog = 4,
         human = ,
         chicken = 2,
         plant = 0,
         stop("Unknown input")
  )
}
legs("cow")

legs("dog")

# what type do the following return?
typeof(ifelse(TRUE, 1, "no"))
typeof(ifelse(FALSE, 1, "no"))
typeof(ifelse(NA, 1, "no"))

# looping
vector = 1:5
for (item in vector) perform_action
# can be exited with next or break

# tips:
## make sure to preallocate 
## seq_along(x), not 1:length(x)
## loops strip attributes:

xs <- as.Date(c("2020-01-01", "2010-01-01"))
for (x in xs) {
  print(x)
}

## remmeber: map and apply are often better than for


