package main

import (
    "fmt"
    "runtime"
    "time"
)

func sendNum(c chan int) {
    fmt.Println("begin call sendNum...")
    c <- 7
    fmt.Println("end call sendNum...")
}


// 同步机制
func main() {
    // 创建一个管道
    c := make(chan int)
    go sendNum(c) // 启动协程

    // 为了防止忘记关闭
    defer close(c)

    // 睡眠3s，为了验证写端是否阻塞
    time.Sleep(time.Second * 3)
    num := <- c

    fmt.Println("num = ", num)

    runtime.Gosched() // 保证除此以外的协程彻底结束
}

// F:\GoProject\src\test2079>go run test02.go