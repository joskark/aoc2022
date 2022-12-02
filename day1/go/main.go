package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func main() {
	pwd, _ := os.Getwd()
	dat, err := os.ReadFile(pwd + "/input")
	check(err)
	sdata := string(dat)
	s := strings.Split(sdata, "\n\n")

	var final_slice []int

	for _, j := range s {
		tmp := strings.Split(j, "\n")
		res := 0
		for _, i := range tmp {
			val, _ := strconv.Atoi(i)
			res += val
		}
		final_slice = append(final_slice, res)
	}

	sort.Ints(final_slice)
	fmt.Println("Part 1:", final_slice[len(final_slice)-1])
	fmt.Println("Part 2:", sum(final_slice[len(final_slice)-3:]))
}
