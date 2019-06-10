package main

import (
    "fmt"
    "math"
)

type Point struct {
    x, y float64
}

func getDistance(p1, p2 Point) float64 {
    return math.Hypot(p2.x - p1.x, p2.y - p1.y)
}

//封装，函数
func (self *Point) getDistance2(p Point) float64 {
    return math.Hypot(p.x - self.x, p.y - self.y)
}

func main() {
    fmt.Println("distance with two points")
    p1 := Point{0.0, 0.0}
    p2 := Point{3.0, 4.0}
    fmt.Println(getDistance(p1,p2))
    fmt.Println(p1.getDistance2(p2))
}

// F:\GoProject\src\test2079>go run test02.go