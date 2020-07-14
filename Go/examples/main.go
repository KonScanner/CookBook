package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	var printUser bool

	flag.BoolVar(&printUser, "print-user", true, "Print a name if set to true")

	flag.Parse()

	user := os.Getenv("USER")
	if printUser {
		fmt.Printf("Hello %s!\n", user)
	}

}
