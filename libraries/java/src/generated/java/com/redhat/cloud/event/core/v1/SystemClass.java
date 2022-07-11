package com.redhat.cloud.event.core.v1;

import com.fasterxml.jackson.annotation.*;

/**
 * A RHEL system managed by console.redhat.com
 */
public class SystemClass {
    private String displayName;
    private String hostURL;
    private String hostname;
    private String inventoryID;
    private String rhelVersion;
    private RHELSystemTag[] tags;

    @JsonProperty("display_name")
    public String getDisplayName() { return displayName; }
    @JsonProperty("display_name")
    public void setDisplayName(String value) { this.displayName = value; }

    @JsonProperty("host_url")
    public String getHostURL() { return hostURL; }
    @JsonProperty("host_url")
    public void setHostURL(String value) { this.hostURL = value; }

    @JsonProperty("hostname")
    public String getHostname() { return hostname; }
    @JsonProperty("hostname")
    public void setHostname(String value) { this.hostname = value; }

    @JsonProperty("inventory_id")
    public String getInventoryID() { return inventoryID; }
    @JsonProperty("inventory_id")
    public void setInventoryID(String value) { this.inventoryID = value; }

    @JsonProperty("rhel_version")
    public String getRHELVersion() { return rhelVersion; }
    @JsonProperty("rhel_version")
    public void setRHELVersion(String value) { this.rhelVersion = value; }

    @JsonProperty("tags")
    public RHELSystemTag[] getTags() { return tags; }
    @JsonProperty("tags")
    public void setTags(RHELSystemTag[] value) { this.tags = value; }
}
