package main

import (
	"encoding/xml"
	"fmt"
	"io/ioutil"
	"net/http"
)

type Location struct {
	Loc string `xml:"loc"`
}

type SitemapIndex struct {
	Locations []Location `xml:"url"`
}

func (l Location) String() string {
	return fmt.Sprintf(l.Loc)
}

func main() {

	response, _ := http.Get("https://www.washingtonpost.com/news-blogs-technology-sitemap.xml")
	bytes, _ := ioutil.ReadAll(response.Body)
	// stringBody := string(bytes)
	// fmt.Println(stringBody)

	response.Body.Close()
	var s SitemapIndex
	xml.Unmarshal(bytes, &s)
	fmt.Println(s.Locations)

}
