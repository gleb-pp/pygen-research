package main

import (
	"fmt"
	"os"
	"time"
)

const MAX_D = 100
const N = 1000000

func stage(in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		for v := range in {
			out <- v
		}
		close(out)
	}()
	return out
}

func main() {
	file, _ := os.Create("go_chain.txt")
	defer file.Close()

	for d := 1; d <= MAX_D; d++ {
		start := time.Now()

		for i := 0; i < N; i++ {
			var ch <-chan int

			base := make(chan int, 1)
			base <- 1
			close(base)

			ch = base

			for j := 0; j < d; j++ {
				ch = stage(ch)
			}

			for range ch {
			}
		}

		elapsed := time.Since(start)
		fmt.Printf("%d %f\n", d, elapsed.Seconds())
		fmt.Fprintf(file, "%d %f\n", d, elapsed.Seconds())
	}
}
