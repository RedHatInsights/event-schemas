// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    rHELSystem, err := UnmarshalRHELSystem(bytes)
//    bytes, err = rHELSystem.Marshal()

package core

import "encoding/json"

func UnmarshalRHELSystem(data []byte) (RHELSystem, error) {
	var r RHELSystem
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *RHELSystem) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

// Event data for a RHEL system.
type RHELSystem struct {
	System SystemClass `json:"system"`
}

// A RHEL system managed by console.redhat.com
type SystemClass struct {
	DisplayName *string         `json:"display_name,omitempty"`
	HostURL     *string         `json:"host_url,omitempty"`    
	Hostname    *string         `json:"hostname,omitempty"`    
	InventoryID string          `json:"inventory_id"`          
	RHELVersion *string         `json:"rhel_version,omitempty"`
	Tags        []RHELSystemTag `json:"tags,omitempty"`        
}

type RHELSystemTag struct {
	Key       string `json:"key"`      
	Namespace string `json:"namespace"`
	Value     string `json:"value"`    
}
