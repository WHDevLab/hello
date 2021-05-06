package main

import (
	"encoding/json"
	"fmt"
)
type personInfo struct {
	ID string
	Name string
	Address string
}
func calc(a int, b int) string{
	var r = a + b
	var x = fmt.Sprintf("%d", r)
	myMap := map[string] string{"result": x}
	data, _ := json.Marshal(&myMap)
	return string(data)
}

func main() {
	fmt.Println(calc(4,5))
}