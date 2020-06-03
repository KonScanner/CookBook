package main

import (
	"fmt"
	"net/http"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Woah, Go is cool!")

}

func aboutHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "'Expert web design by: KonScanner'")

}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/about/", aboutHandler)
	http.ListenAndServe(":8050", nil)

}
