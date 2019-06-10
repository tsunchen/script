package main

import (
    "fmt"
)

type Human struct {
    name   string
    age    int
    gender string
}

type SuperMan struct {
    Human
    name string
    level int
}

func (p *Human) setName(xn string){
    p.name = xn
}

func (p *Human) setAge(xa int) {
    p.age = xa
}

func (p *SuperMan) setLevel(l int) {
    p.level = l
}

// 继承
func main() {
     h1 := Human{"TSunx", 38, "male"}
     var s1 SuperMan
     s1.Human = h1
     s1.name = "Chaos"
     s1.setLevel(1)

     fmt.Println(h1)
     fmt.Println(s1)
}

// F:\GoProject\src\test2079>go run test02.go