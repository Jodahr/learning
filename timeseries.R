# show all built-in data
data()

# plot co2 data
plot(co2)

# summary about the data
help(co2)

# compute summary stats
summary(co2)

# extract time
time(co2)

# create lm
model <- lm(co2 ~ time(co2))

time(residuals(model))

plot(model$residuals, xlim = c(100, 200))

# plot residuals hist
co2_res <- resid(model)
hist(co2_res)
co2_res

# residual timeplot
plot(co2_res ~ time(co2))
# oscillator behaviour
plot(co2_res ~ time(co2), xlim=c(1960,1962))

# autocorr
acf(co2, lag.max = 100)

plot(model)
model

# qq plot by hand
# number of obs
n <- length(co2)
n
r <- order(order(co2))
r
p <- (r - 1/2) / n
p
y <- qnorm(p)
y
plot(y)
plot(co2,y)

# qnorm gives the quantile/percentile 
# e.g. qnorm of 0.5 is the position of the median in a normal distribution, so 0
qnorm(0.5)
qnorm(c(0.25,0.5,0.75,0.94))
data <- rnorm(2000)
plot(data)
hist(data)
quantile(data)
quantile(data, c(0.25,0.5,0.75,0.94))

# nice explantion: https://data.library.virginia.edu/understanding-q-q-plots/
model$residuals
