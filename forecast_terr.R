options(warn=-1)
isNamespaceLoaded <- function(name) is.element(name, loadedNamespaces())
library(forecast)
options(warn=0)

conf <- 0.75
h <- 12
freq <- 365


df <- read.csv(text = csv,header=FALSE)
N <- nrow(df)
df$V1 <- as.Date(df$V1)
input <- ts(df$V2,freq=freq,1)
#input <- ts(df$V2,freq=12,start=df$V1[1])


extra_dates <- seq(from = df$V1[N],  length.out = h+1, by = "month")[-1]


conf_str <- paste0(as.character(conf*100),"% ")


hw_forecast <- hw(input,level=conf,h=h)
hw_fitted <- hw_forecast$fitted

arima_str = paste0("ARIMA ", c("Lower ","Upper "), conf_str)
hw_str = paste0("ARIMA ", c("Lower ","Upper "), conf_str)

output <- data.frame("date" = as.Date(c(df$V1,extra_dates)), "value" = c(df$V2,rep(NA,h)), "HW Fitted" = c(hw_fitted,rep(NA,h)),
                     "HW Upper" = c(rep(NA,N),hw_forecast$upper), "HW Mean Forecast" = c(rep(NA,N),hw_forecast$mean), "HW Lower" = c(rep(NA,N),hw_forecast$lower)
                     )


