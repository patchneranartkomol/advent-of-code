package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"sync"
)

const Fname = "input.txt"

func nextSeq(row []int) []int {
	var newRow []int
	for i := 1; i < len(row); i++ {
		newRow = append(newRow, row[i] - row[i-1])
	}
	return newRow
}

func allZero(row []int) bool {
	for i := 0; i < len(row); i++ {
		if row[i] != 0 {
			return false
		}
	}
	return true
}

func partOne(lines [][]int) int {
	var wg sync.WaitGroup
	res := make(chan int, len(lines))
	for _, line := range lines {
		wg.Add(1)
		go func(line []int) {
			defer wg.Done()
			sum := line[len(line)-1]
			row := nextSeq(line)
			for !allZero(row) {
				sum += row[len(row)-1]
				row = nextSeq(row)
			}
			res <- sum
		}(line)
	}
	wg.Wait()

	total := 0
	for i := 0; i < len(lines); i++ {
		total += <-res
	}
	return total
}

func partTwo(lines [][]int) int {
	var wg sync.WaitGroup
	res := make(chan int, len(lines))
	for _, line := range lines {
		wg.Add(1)
		go func(line []int) {
			defer wg.Done()
			var firstEls []int
			firstEls = append(firstEls, line[0])
			row := nextSeq(line)
			for !allZero(row) {
				firstEls = append(firstEls, row[0])
				row = nextSeq(row)
			}

			value := 0
			for i := len(firstEls) - 1; i >= 0; i-- {
				value = firstEls[i] - value
			}
			res <- value
		}(line)
	}
	wg.Wait()

	total := 0
	for i := 0; i < len(lines); i++ {
		total += <-res
	}
	return total
}

func main() {
	var lines [][]int
	file, err := os.Open(Fname)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var row []int
		for _, v := range strings.Split(scanner.Text(), " ") {
			value, err := strconv.Atoi(v)
			if err != nil {
				log.Fatal(err)
			}
			row = append(row, value)
		}
		lines = append(lines, row)
	}

	fmt.Printf("Part one - sum of extrapolated values: %d\n", partOne(lines))
	fmt.Printf("Part two - sum of extrapolated values: %d\n", partTwo(lines))
}
