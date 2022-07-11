package com.redhat.cloud.event.core.v1;

import com.fasterxml.jackson.annotation.*;

public class RHELSystemTag {
    private String key;
    private String namespace;
    private String value;

    @JsonProperty("key")
    public String getKey() { return key; }
    @JsonProperty("key")
    public void setKey(String value) { this.key = value; }

    @JsonProperty("namespace")
    public String getNamespace() { return namespace; }
    @JsonProperty("namespace")
    public void setNamespace(String value) { this.namespace = value; }

    @JsonProperty("value")
    public String getValue() { return value; }
    @JsonProperty("value")
    public void setValue(String value) { this.value = value; }
}
