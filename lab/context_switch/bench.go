package main

import (
	"fmt"
	"time"
)

const N = 10000000

func main() {
	ch := make(chan struct{})

	go func() {
		for {
			<-ch
		}
	}()

	start := time.Now()

	for i := 0; i < N; i++ {
		ch <- struct{}{}
	}

	elapsed := time.Since(start)
	avg := float64(elapsed.Nanoseconds()) / float64(N)

	fmt.Printf("Go: %.2f ns\n", avg)
}
