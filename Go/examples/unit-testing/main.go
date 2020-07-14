package main

func main() {

}

func sum(x, y int) int {
	if x > 100 {
		return x + 20 // introducing a bug
	}
	return x + y
}
