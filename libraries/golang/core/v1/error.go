// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    error, err := UnmarshalError(bytes)
//    bytes, err = error.Marshal()

package core

import "encoding/json"

func UnmarshalError(data []byte) (Error, error) {
	var r Error
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Error) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

// Event data for an application error.
type Error struct {
	Error ErrorClass `json:"error"`
}

// An error reported by an application.
type ErrorClass struct {
	Code       string   `json:"code"`                 // Machine-readable error code that identifies the error.
	Message    string   `json:"message"`              // Human readable description of the error.
	Severity   Severity `json:"severity"`             // The severity of the error.
	StackTrace *string  `json:"stack_trace,omitempty"`// The stack trace/traceback (optional)
}

// The severity of the error.
type Severity string
const (
	Critical Severity = "critical"
	SeverityError Severity = "error"
	Warning Severity = "warning"
)
