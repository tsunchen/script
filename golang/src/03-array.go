package main

import (
    "fmt"
)

func main() {
    var a1 [] float64 = [] float64 {3.14, 2.20, 3.10}

    b1 := [] int {0, 1, 2, 3, 4, 5, 6}

    points := [5][2]int{
        {0, 0},
        {1, 1},
        {2, 2},
        {3, 3}}

    fmt.Println(a1)
    fmt.Println(b1)
    fmt.Println(points)
    s1 := b1[:]
    s1 = append(s1, 101)
    s2 := append(s1, 202)
    fmt.Println(s2)
    fmt.Println(s1)
}

// F:\GoProject\src\test2079>go run test02.go