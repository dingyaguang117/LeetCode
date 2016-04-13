package main
import (
    "fmt"
)

func _isIsomorphic(s string, t string) bool {
    var m = make(map[rune] rune);
    for i, ch := range(s){
        ch_t := rune(t[i])
        ch_t_exist, ok := m[ch]
        if ok {
            if ch_t != ch_t_exist{
                return false
            }
        }else{
            m[ch] = ch_t
        }
    }
    return true;
}

func isIsomorphic(s string, t string) bool {
    return _isIsomorphic(s, t) && _isIsomorphic(t, s)
}

func main(){
    fmt.Println(isIsomorphic("ab", "ab"))
}