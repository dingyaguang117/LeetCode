package main

import "fmt"

func _isValidBST(root *TreeNode) (bool, int, int) {
	min_val := root.Val
	max_val := root.Val

	if root.Left != nil {
		valid, min, max := _isValidBST(root.Left)
		if !valid || max >= root.Val {
			return false, 0, 0
		}
		min_val = min
	}
	if root.Right != nil {
		valid, min, max := _isValidBST(root.Right)
		if !valid || min <= root.Val {
			return false, 0, 0
		}
		max_val = max
	}
	return true, min_val, max_val
}

func isValidBST(root *TreeNode) bool {
	if root == nil {
		return true
	}

	valid, _, _ := _isValidBST(root)
	return valid
}
