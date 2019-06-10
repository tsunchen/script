package main

import (
    "fmt"
    "time"
)

func fib(x int) int {
    if x < 2 {
        return x
    }
    return fib(x - 1) + fib(x - 2)
}

func spinner(delay time.Duration) {
    for {
        for _, v := range `-\|/` {
            fmt.Printf("\r%c", v)
            time.Sleep(delay)
        }
    }
}


// 协程
func main() {
    go spinner(100 * time.Millisecond)
    const n = 45
    fibN := fib(n)
    fmt.Printf("\rFibonacci(%d) = %d\n", n, fibN)

}

// F:\GoProject\src\test2079>go run test02.go