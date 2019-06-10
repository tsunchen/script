package main

import (
    "fmt"
)

type Coder interface {
    sleeping()
    coding()
}

type Pythoner struct {
    name string
}

type BlockChainer struct {
    name string
}

func (x *Pythoner) sleeping() {
    fmt.Println("python coder ", x.name, " is sleeping")
}

func (x *Pythoner) coding() {
    fmt.Println("python coder ", x.name, " is coding")
}

func (x *BlockChainer) sleeping() {
    fmt.Println("blockchain coder ", x.name, " is sleeping")
}

func (x *BlockChainer) coding() {
    fmt.Println("blockchain coder ", x.name, " is coding")
}

// 工厂模式
func school(name string, x int) Coder {
    if x == 1 {
        return &Pythoner {name}
    } else if x == 2 {
        return &BlockChainer{name}
    }
    return nil
}

// 多态
func main() {
    p1 := Pythoner {"python"}
    p1.sleeping()

    b2 := BlockChainer {"bchain"}
    b2.coding()

    x3 := school("unknown", 1)
    if x3 != nil {
        x3.coding()
        x3.sleeping()
    }

}

// F:\GoProject\src\test2079>go run test02.go