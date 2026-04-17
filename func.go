package main

import "fmt"

func greet(name string) {
    fmt.Printf("Hello, %s! Welcome to Go.\n", name)
}

func add(a, b int) int {
    return a + b
}

func main() {
    greet("Edward")

    result := add(23, 4)
    fmt.Printf("23 + 4 = %d\n", result)
}