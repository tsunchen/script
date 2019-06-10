package main

import (
    "fmt"
)

func main() {
    // 定义的map为nil
    var capital map[string]string

    if capital == nil {
        fmt.Println("capital is nil")
    }

    capital = make(map[string]string)
    if capital == nil {
        fmt.Println("capital is nil")
    }

    capital["china"] = "beijing"
    capital["japan"] = "tokyo"
    capital["england"] = "london"
    fmt.Println(capital)
    fmt.Println(capital["england"])

    b1 := [] int {0, 1, 2, 3, 4, 5, 6}
    for i := 0; i < 7 ; i++ {
        fmt.Println("i[", i, "]", b1[i])
    }

    for k, v := range b1 {
        fmt.Println("k->",k, "v=", v)
    }

    for k, v := range capital {
        fmt.Println("k->",k, "v=", v)
    }
}

// F:\GoProject\src\test2079>go run test02.go