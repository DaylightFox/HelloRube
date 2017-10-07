package main

import "fmt"

func main() {
	fmt.Printf(helloWorld())
}

func ello(arr []string) {
	if arr[0] == "a" {
		panic("back to helloWorld")
	} //already Print "ello"

	max := arr[0]
	id := 0
	for index, x := range arr {
		if x > max {
			max = x
			id = index
		}
	}
	arr[id] = "a"

	defer fmt.Printf(max) 

	ello(arr)
}

func helloWorld() (hello string) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Printf(" ")
		}
	}()

	defer func() {
		hello += "World"
	}()

	for i := 0; i < 100; i++ {
		if i == 72 {
			fmt.Printf(string(i)) //Print "H"
		}
	}

	ello([]string{"e", "l", "l", "o"}) //Print "ello"

	return hello
}
