package main

import "fmt"

func main() {
	x := 35
	a := &x // memory adress
	fmt.Println(a)
	fmt.Println(*a)
	*a = 5
	fmt.Println(x)
	*a = *a * *a
	fmt.Println(x)
}
