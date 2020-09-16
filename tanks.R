setwd('Desktop/learn/for_fun/')

library(abc)
library(matrixStats)
sample_tanks = function(n_samp = 10, N_max = 500){
  return(sort(sample(1:N_max, n_samp)))
}

N_max_prior = function(n, min = 10){
  sample(min:100000,n, replace=T)
}

##
normal = function(mu, sig, n){
  return(sort(rnorm(n, mu, sig)))
}

mu_prior = function(n){
  return(rnorm(n,0,10))
}

sig_prior = function(n){
  return(runif(n, 0, 100))
}

## tanks problem
n_samp = 20
N_max = 50000
sim_size = 100000

obs = sample_tanks(n_samp, N_max)
sim = array(NA, dim = c(sim_size, n_samp))

sim_param = N_max_prior(sim_size, max(n_samp))
for (i in 1:sim_size) sim[i,] = sample_tanks(n_samp, sim_param[i])

o = abc(obs, sim_param, sim, tol = .01, method = 'rejection')
summary(o)
hist(o$unadj.values); abline(v = 50000)


## normal 

mu_true = 10
sig_true = 4
n_samp = 200
sim_size = 100000

obs = normal(mu_true, sig_true, n_samp)
sim = array(NA, dim = c(sim_size, n_samp))

sim_param = cbind(mu_prior(sim_size), sig_prior(sim_size))
for (i in 1:sim_size) sim[i,] = normal(sim_param[i,1], sim_param[i,2], n_samp)

sim2 = cbind(rowMeans(sim), rowVars(sim))
obs2 = c(mean(obs), var(obs))


o = abc(obs, sim_param, sim, tol = .01, method = 'rejection')
summary(o)
hist(o$unadj.values[,1]); abline(v = mu_true)
hist(o$unadj.values[,2]); abline(v = sig_true)


o = abc(obs2, sim_param, sim2, tol = .01, method = 'rejection')
summary(o)
hist(o$unadj.values[,1]); abline(v = mu_true)
hist(o$unadj.values[,2]); abline(v = sig_true)
