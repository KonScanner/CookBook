package main

import "fmt"

type rectangle struct {
	width, height int
}

// References rectangle struct with "r"
func (r *rectangle) area() int {
	return r.width * r.height

}

func (r rectangle) perimeter() int {
	return 2*r.width + 2*r.height

}

func main() {
	r := rectangle{width: 25, height: 10}

	fmt.Println("Area: ", r.area())
	fmt.Println("Perimeter: ", r.perimeter())

	rp := &r
	rp.height = 50
	fmt.Println("Area: ", rp.area())
	fmt.Println("Perimeter: ", rp.perimeter())

}
