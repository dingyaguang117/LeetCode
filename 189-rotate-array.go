package main
import (
    "fmt"
)

func reverse(nums []int, begin int,end int){
    for {
        if begin >= end{
            break
        }
        nums[begin], nums[end] = nums[end], nums[begin]
        begin ++
        end --
    }
}

func rotate(nums []int, k int)  {
    k = k % len(nums)
    mid := len(nums) - k
    reverse(nums, 0, mid-1)
    reverse(nums, mid, len(nums)-1)
    reverse(nums, 0, len(nums)-1)   
}


func main() {
    var nums = []int{-2}
    rotate(nums, 2);
    fmt.Println(nums)
}