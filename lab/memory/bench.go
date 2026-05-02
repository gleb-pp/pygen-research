package main

import (
	"fmt"
	"runtime"
)

const N = 100000

func worker() {
	select {}
}

func main() {
	var m runtime.MemStats

	runtime.GC()
	runtime.ReadMemStats(&m)
	before := m.Alloc

	for i := 0; i < N; i++ {
		go worker()
	}

	runtime.ReadMemStats(&m)
	after := m.Alloc

	fmt.Printf("Memory: %.2f MB\n", float64(after-before)/1024/1024)
}
