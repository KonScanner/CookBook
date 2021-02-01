package main

import (
"fmt"
"runtime")


var version string; // for external compilation use (see pass-flags.sh)

func main(){
  fmt.Printf("OS: %s\nArchitecture: %s\n", runtime.GOOS, runtime.GOARCH)
  fmt.Printf("Version %s\n", version)
}

