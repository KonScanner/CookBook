package main

import "fmt"

type person struct {
	name   string
	age    uint8 // earthling years
	height uint8 // cm
}

type dog struct {
	name string
	age  uint8 // earthling years
}

func addPerson(name string, age uint8, height uint8) *person {
	p := person{name: name, age: age, height: height}
	return &p

}

func main() {
	fmt.Println(person{"Bob", 20, 172})

	fmt.Println(person{name: "Alice", age: 26, height: 178})

	fmt.Println(person{name: "Baby Yoda", height: 95}) //  age is not fed, value assumed

	fmt.Println(&dog{name: "Ruby", age: 9})

	fmt.Println(addPerson("Bob Builder", 50, 150))

	a := person{name: "test_subject003", age: 22, height: 177}
	fmt.Println(a.name, a.height)

	ap := &a
	fmt.Println(ap.age)

	ap.age = 23 // updates the memory location of a (shared with ap)
	fmt.Println(a.age)
}
