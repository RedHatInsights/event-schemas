package com.redhat.cloud.event.apps.advisor.v1;

import com.fasterxml.jackson.annotation.*;

/**
 * Event data for Advisor Recommendations.
 */
public class AdvisorRecommendations {
    private AdvisorRecommendation[] advisorRecommendations;
    private RHELSystem system;

    /**
     * Advisor recommendations for a system
     */
    @JsonProperty("advisor_recommendations")
    public AdvisorRecommendation[] getAdvisorRecommendations() { return advisorRecommendations; }
    @JsonProperty("advisor_recommendations")
    public void setAdvisorRecommendations(AdvisorRecommendation[] value) { this.advisorRecommendations = value; }

    @JsonProperty("system")
    public RHELSystem getSystem() { return system; }
    @JsonProperty("system")
    public void setSystem(RHELSystem value) { this.system = value; }
}
