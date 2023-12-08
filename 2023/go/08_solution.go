package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

const fname = "input.txt"

type node struct {
	name  string
	left  string
	right string
}

func partOne(directions string, nodes []node, nodeMap map[string]int) int {
	var idx int
	dirsIdx, steps := 0, 0
	// Traverse the list of nodes until we start at AAA
	for i, node := range nodes {
		if node.name == "AAA" {
			idx = i
			break
		}
	}

	for nodes[idx].name != "ZZZ" {
		switch directions[dirsIdx] {
		case 'L':
			idx = nodeMap[nodes[idx].left]
		case 'R':
			idx = nodeMap[nodes[idx].right]
		}
		steps += 1
		dirsIdx += 1
		if dirsIdx == len(directions) {
			dirsIdx = 0
		}
	}
	return steps
}

func countSteps(directions string, nodes []node, nodeMap map[string]int, start string) int {
	var idx int
	dirsIdx, steps := 0, 0
	for i, node := range nodes {
		if node.name == start {
			idx = i
			break
		}
	}

	for nodes[idx].name[2] != 'Z' {
		switch directions[dirsIdx] {
		case 'L':
			idx = nodeMap[nodes[idx].left]
		case 'R':
			idx = nodeMap[nodes[idx].right]
		}
		steps += 1
		dirsIdx += 1
		if dirsIdx == len(directions) {
			dirsIdx = 0
		}
	}
	return steps
}

// greatest common divisor (GCD) via Euclidean algorithm
func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

// find Least Common Multiple (LCM) via GCD
func LCM(a, b int, integers ...int) int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}

	return result
}

func partTwo(directions string, nodes []node, nodeMap map[string]int) int {
	// key - starting position : value - step count
	var routeLengths []int
	for _, node := range nodes {
		if node.name[2] == 'A' {
			routeLengths = append(routeLengths, countSteps(directions, nodes, nodeMap, node.name))
		}
	}

	return LCM(routeLengths[0], routeLengths[1], routeLengths[2:]...)
}

func main() {
	file, err := os.Open(fname)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	directions := scanner.Text()
	var nodes []node
	nodeMap := make(map[string]int)
	scanner.Scan()
	i := 0
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "=")
		name := strings.Trim(line[0], " ")
		dirs := strings.Split(strings.Trim(line[1], " ()"), ",")
		left, right := dirs[0], strings.Trim(dirs[1], " ")
		nodes = append(nodes, node{name: name, left: left, right: right})
		nodeMap[name] = i
		i += 1
	}
	fmt.Printf("Part one: Number of steps: %d\n", partOne(directions, nodes, nodeMap))
	fmt.Printf("Part two: Number of steps: %d\n", partTwo(directions, nodes, nodeMap))
}
