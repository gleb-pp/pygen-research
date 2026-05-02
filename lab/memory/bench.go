package main

import (
	"fmt"
	"os"
	"runtime"
)

const MAX_N = 100000
const STEP = 1000

func worker() {
	select {}
}

func main() {
	file, _ := os.Create("go_memory.txt")
	defer file.Close()

	var m runtime.MemStats

	for n := 1; n <= MAX_N; n += STEP {
		runtime.GC()
		runtime.ReadMemStats(&m)
		before := m.Alloc

		for i := 0; i < n; i++ {
			go worker()
		}

		runtime.ReadMemStats(&m)
		after := m.Alloc

		fmt.Fprintf(file, "%d %d\n", n, after-before)
	}
}
