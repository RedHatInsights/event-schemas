package com.redhat.cloud.event.core.v1;

import com.fasterxml.jackson.annotation.*;

/**
 * An error reported by an application.
 */
public class ErrorClass {
    private String code;
    private String message;
    private Severity severity;
    private String stackTrace;

    /**
     * Machine-readable error code that identifies the error.
     */
    @JsonProperty("code")
    public String getCode() { return code; }
    @JsonProperty("code")
    public void setCode(String value) { this.code = value; }

    /**
     * Human readable description of the error.
     */
    @JsonProperty("message")
    public String getMessage() { return message; }
    @JsonProperty("message")
    public void setMessage(String value) { this.message = value; }

    /**
     * The severity of the error.
     */
    @JsonProperty("severity")
    public Severity getSeverity() { return severity; }
    @JsonProperty("severity")
    public void setSeverity(Severity value) { this.severity = value; }

    /**
     * The stack trace/traceback (optional)
     */
    @JsonProperty("stack_trace")
    public String getStackTrace() { return stackTrace; }
    @JsonProperty("stack_trace")
    public void setStackTrace(String value) { this.stackTrace = value; }
}
