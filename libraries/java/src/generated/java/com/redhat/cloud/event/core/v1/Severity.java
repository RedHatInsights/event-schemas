package com.redhat.cloud.event.core.v1;

import java.io.IOException;
import com.fasterxml.jackson.annotation.*;

/**
 * The severity of the error.
 */
public enum Severity {
    CRITICAL, ERROR, WARNING;

    @JsonValue
    public String toValue() {
        switch (this) {
            case CRITICAL: return "critical";
            case ERROR: return "error";
            case WARNING: return "warning";
        }
        return null;
    }

    @JsonCreator
    public static Severity forValue(String value) throws IOException {
        if (value.equals("critical")) return CRITICAL;
        if (value.equals("error")) return ERROR;
        if (value.equals("warning")) return WARNING;
        throw new IOException("Cannot deserialize Severity");
    }
}
