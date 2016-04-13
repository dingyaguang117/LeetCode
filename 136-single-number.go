package main
import (
    "fmt"
)

func singleNumber(nums []int) int {
    var result = 0;
    for _, item := range(nums) {
        result ^= item
    }
    return result
}


func main() {
    var nums = []int{1, 1, -2, 3, 3};
    fmt.Println(singleNumber(nums));
}