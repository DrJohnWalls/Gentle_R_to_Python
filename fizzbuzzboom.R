fizzbuzzboom <- function(x){
  if(x == 524){
    delay <- 0.5
    print("You have entered the self destruct code...")
    Sys.sleep(delay)
    print("All your files will be erased...")
    Sys.sleep(delay)
    print("You have 5 seconds to abort...")
    t <- 5+1
    Sys.sleep(delay)
    while(t > 1) {t <- t-1; 
    print(t)
    Sys.sleep(delay);
    }
    print("BOOM")
  } else if (x %% 5==0 & x %% 3==0){
    return("fizzbuzz")
  } else if(x %% 5==0){
    return("buzz")
  } else if(x %% 3==0){
    return("fizz")
  } else {
    return(x)
  }
}

fizzbuzzboom(524)