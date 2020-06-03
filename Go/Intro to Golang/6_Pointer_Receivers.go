package main

import "fmt"

type car struct {
	gasPedal      uint16  //min: 0,      max: 65535    16bit
	brakePedal    uint16  //min: 0,      max: 65535
	steeringWheel int16   //min: -32768  max: 32768
	topSpeedKmh   float64 //what's our top speed?
}

const usixteenbitmax float64 = 65535
const kmhMultiple float64 = 1.60934

// Value receiver
func (c car) kmh() float64 {
	return float64(c.gasPedal) * (c.topSpeedKmh / usixteenbitmax)
}

func (c car) mph() float64 {
	return float64(c.gasPedal) * (c.topSpeedKmh / kmhMultiple / usixteenbitmax)
}

// Pointer Receiver (if struct is large, this is better, more efficient, no copy)
func (c *car) newTopSpeed(newSpeed float64) {
	c.topSpeedKmh = newSpeed
}

// Not more efficient
func modifyTopSpeed(c car, speed float64) car {
	c.newTopSpeed(speed)
	return c
}

func main() {

	aCar := car{64900, 0, 12562, 225.0}

	fmt.Println("gasPedal:", aCar.gasPedal, "brakePedal:", aCar.brakePedal, "steeringWheel:", aCar.steeringWheel)
	fmt.Println("km/h", aCar.kmh())
	fmt.Println("m/h", aCar.mph())

	aCar = modifyTopSpeed(aCar, 500)
	fmt.Println("gasPedal:", aCar.gasPedal, "brakePedal:", aCar.brakePedal, "steeringWheel:", aCar.steeringWheel)
	fmt.Println("km/h", aCar.kmh())
	fmt.Println("m/h", aCar.mph())
}
