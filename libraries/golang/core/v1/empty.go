// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    empty, err := UnmarshalEmpty(bytes)
//    bytes, err = empty.Marshal()

package core

import "encoding/json"

type Empty interface{}

func UnmarshalEmpty(data []byte) (Empty, error) {
	var r Empty
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Empty) Marshal() ([]byte, error) {
	return json.Marshal(r)
}
