package main

import (
	"fmt"
	"net/http"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {

	fmt.Fprintf(w, `<h1>Hello there, general Kennobi!</h1>
	<p>Go is fast!</p>
	<p>Go is simple!</p>
	<p>You %s are %s</p>
	`, "friend", "<strong>cool</strong>")

}

func main() {
	http.HandleFunc("/", indexHandler)
	http.ListenAndServe(":8050", nil)
}
