package main

import "fmt"

func describe(score int) {
	if score >= 90 {
		fmt.Println("Excellent!")
	} else if score >= 70 {
		fmt.Println("Good job!")
	} else {
		fmt.Println("Keep practicing!")
	}
}

func main() {
	describe(95) 
	describe(75) 
	describe(50) 

	
	for i := 1; i <= 10; i++ {
		fmt.Printf("%d\n", i)
	}
}