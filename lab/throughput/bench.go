package main

import (
	"fmt"
	"os"
	"sync"
	"time"
)

const MAX_N = 100000
const STEP = 1000

func worker(wg *sync.WaitGroup) {
	time.Sleep(time.Millisecond)
	wg.Done()
}

func run(n int) (float64, float64) {
	var wg sync.WaitGroup

	start := time.Now()

	for i := 0; i < n; i++ {
		wg.Add(1)
		go worker(&wg)
	}

	wg.Wait()

	total := time.Since(start).Seconds()

	throughput := float64(n) / total
	latency := total / float64(n) * 1e9

	return throughput, latency
}

func main() {
	file, _ := os.Create("go_async.txt")
	defer file.Close()

	for n := 1; n <= MAX_N; n += STEP {
		fmt.Printf("Running with %d goroutines...\n", n)
		t, l := run(n)
		fmt.Fprintf(file, "%d %f %f\n", n, t, l)
	}
}
