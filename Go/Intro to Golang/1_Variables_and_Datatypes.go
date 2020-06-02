package main

import (
	"fmt"
	"reflect"
)

func main() {
	var a complex64 // Explicit variable declaration
	var b = 20000.2 // Implicit variable declaration (let the compiler decide)
	a = 5 + 2i
	var testAssign uint32
	var boolTest bool
	c1 := complex(10, 2) // Expression assignment operator (Fastest, easiest)
	c2 := 12 + 4i

	var result = c1 + c2

	fmt.Println(result)
	fmt.Println("Its real part is:", real(result))
	fmt.Println("Its imaginary part is:", imag(result))

	fmt.Println("type:", reflect.TypeOf(result))
	fmt.Println("type of var a", reflect.TypeOf(a))
	fmt.Println(testAssign, boolTest) // Defaults are 0 and false
	fmt.Printf("The value of %v is type %T", b, b)

}
