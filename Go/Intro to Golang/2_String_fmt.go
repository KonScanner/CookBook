package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {

	p := point{3, 4} // main.point

	fmt.Printf("%v\n", p) // x: 3 y: 4

	fmt.Printf("%+v\n", p)

	fmt.Printf("%#v\n", p)

	fmt.Printf("%T\n", p)

	fmt.Printf("%t\n", true)

	fmt.Printf("%d\n", 456)

	fmt.Printf("%b\n", 13)

	fmt.Printf("%c\n", 333)

	fmt.Printf("%x\n", 654)

	fmt.Printf("%f\n", 69.96)

	fmt.Printf("%e\n", 456100000.0)
	fmt.Printf("%E\n", 456100000.0)

	fmt.Printf("%s\n", "\"string\"")

	fmt.Printf("%q\n", "\"string\"")

	fmt.Printf("%x\n", "hex this")

	fmt.Printf("%p\n", &p)

	fmt.Printf("|%6d|%6d|\n", 12, 345)

	fmt.Printf("|%6.2f|%6.2f|\n", 1.2, 3.45)

	fmt.Printf("|%-6.2f|%-6.2f|\n", 1.2, 3.45)

	fmt.Printf("|%6s|%6s|\n", "foo", "b")

	fmt.Printf("|%-6s|%-6s|\n", "foo", "b")

	s := fmt.Sprintf("a %s", "string")
	fmt.Println(s)

	fmt.Fprintf(os.Stderr, "an %s\n", "error")
}
