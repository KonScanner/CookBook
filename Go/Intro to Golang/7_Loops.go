package main

import "fmt"

func exampleLoop1() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

}

func exampleLoop2() {
	i := 0
	for i < 10 {
		fmt.Println(i)
		i++
	}

}

func exampleLoop3() {
	x := 5
	for {
		fmt.Println("print", x)
		x += 3
		if x > 25 {
			break
		}
	}

}

func exampleLoop4() {
	for x := 5; x < 25; x += 3 {
		fmt.Println("print", x)

	}
}

func exampleLoop5() {
	c := 3
	for x := 5; c < 25; x += 3 {
		fmt.Println("print", x)
		c += 4
	}
}

func main() {
	exampleLoop5()
}
