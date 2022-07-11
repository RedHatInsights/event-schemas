// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    advisorRecommendations, err := UnmarshalAdvisorRecommendations(bytes)
//    bytes, err = advisorRecommendations.Marshal()

package advisor

import "encoding/json"

func UnmarshalAdvisorRecommendations(data []byte) (AdvisorRecommendations, error) {
	var r AdvisorRecommendations
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *AdvisorRecommendations) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

// Event data for Advisor Recommendations.
type AdvisorRecommendations struct {
	AdvisorRecommendations []AdvisorRecommendation `json:"advisor_recommendations"`// Advisor recommendations for a system
	System                 RHELSystem              `json:"system"`                 
}

type AdvisorRecommendation struct {
	PublishDate     string `json:"publish_date"`    
	RebootRequired  bool   `json:"reboot_required"` 
	RuleDescription string `json:"rule_description"`
	RuleID          string `json:"rule_id"`         
	RuleURL         string `json:"rule_url"`        
	TotalRisk       string `json:"total_risk"`      
}

// A RHEL system managed by console.redhat.com
type RHELSystem struct {
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
