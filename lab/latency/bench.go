package main

import (
	"fmt"
	"sync"
	"time"
)

const N = 1000000

func worker(wg *sync.WaitGroup) {
	time.Sleep(time.Millisecond)
	wg.Done()
}

func main() {
	var wg sync.WaitGroup

	start := time.Now()

	for i := 0; i < N; i++ {
		wg.Add(1)
		go worker(&wg)
	}

	wg.Wait()

	elapsed := time.Since(start)
	fmt.Printf("Go latency: %f\n", elapsed.Seconds())
}
