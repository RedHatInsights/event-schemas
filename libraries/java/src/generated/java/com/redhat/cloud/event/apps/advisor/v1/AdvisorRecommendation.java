package com.redhat.cloud.event.apps.advisor.v1;

import com.fasterxml.jackson.annotation.*;
import java.time.OffsetDateTime;

public class AdvisorRecommendation {
    private OffsetDateTime publishDate;
    private boolean rebootRequired;
    private String ruleDescription;
    private String ruleID;
    private String ruleURL;
    private String totalRisk;

    @JsonProperty("publish_date")
    public OffsetDateTime getPublishDate() { return publishDate; }
    @JsonProperty("publish_date")
    public void setPublishDate(OffsetDateTime value) { this.publishDate = value; }

    @JsonProperty("reboot_required")
    public boolean getRebootRequired() { return rebootRequired; }
    @JsonProperty("reboot_required")
    public void setRebootRequired(boolean value) { this.rebootRequired = value; }

    @JsonProperty("rule_description")
    public String getRuleDescription() { return ruleDescription; }
    @JsonProperty("rule_description")
    public void setRuleDescription(String value) { this.ruleDescription = value; }

    @JsonProperty("rule_id")
    public String getRuleID() { return ruleID; }
    @JsonProperty("rule_id")
    public void setRuleID(String value) { this.ruleID = value; }

    @JsonProperty("rule_url")
    public String getRuleURL() { return ruleURL; }
    @JsonProperty("rule_url")
    public void setRuleURL(String value) { this.ruleURL = value; }

    @JsonProperty("total_risk")
    public String getTotalRisk() { return totalRisk; }
    @JsonProperty("total_risk")
    public void setTotalRisk(String value) { this.totalRisk = value; }
}
