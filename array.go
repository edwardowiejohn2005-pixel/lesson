package main

import "fmt"

func main() {
    favorite := []string{"basketball", "food", "coding", "reading", "eating"}

    for i, item := range favorite {
        fmt.Printf("%d: %s\n", i+1, item)
    }
}