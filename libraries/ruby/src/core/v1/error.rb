# This code may look unusually verbose for Ruby (and it is), but
# it performs some subtle and complex validation of JSON data.
#
# To parse this JSON, add 'dry-struct' and 'dry-types' gems, then do:
#
#   error = Error.from_json! "{…}"
#   puts error.error.code
#
# If from_json! succeeds, the value returned matches the schema.

require 'json'
require 'dry-types'
require 'dry-struct'

module Types
  include Dry::Types.module

  Hash     = Strict::Hash
  String   = Strict::String
  Severity = Strict::String.enum("critical", "error", "warning")
end

# The severity of the error.
module Severity
  Critical = "critical"
  Error    = "error"
  Warning  = "warning"
end

# An error reported by an application.
class ErrorClass < Dry::Struct

  # Machine-readable error code that identifies the error.
  attribute :code, Types::String

  # Human readable description of the error.
  attribute :message, Types::String

  # The severity of the error.
  attribute :severity, Types::Severity

  # The stack trace/traceback (optional)
  attribute :stack_trace, Types::String.optional

  def self.from_dynamic!(d)
    d = Types::Hash[d]
    new(
      code:        d.fetch("code"),
      message:     d.fetch("message"),
      severity:    d.fetch("severity"),
      stack_trace: d["stack_trace"],
    )
  end

  def self.from_json!(json)
    from_dynamic!(JSON.parse(json))
  end

  def to_dynamic
    {
      "code"        => @code,
      "message"     => @message,
      "severity"    => @severity,
      "stack_trace" => @stack_trace,
    }
  end

  def to_json(options = nil)
    JSON.generate(to_dynamic, options)
  end
end

# Event data for an application error.
class Error < Dry::Struct
  attribute :error, ErrorClass

  def self.from_dynamic!(d)
    d = Types::Hash[d]
    new(
      error: ErrorClass.from_dynamic!(d.fetch("error")),
    )
  end

  def self.from_json!(json)
    from_dynamic!(JSON.parse(json))
  end

  def to_dynamic
    {
      "error" => @error.to_dynamic,
    }
  end

  def to_json(options = nil)
    JSON.generate(to_dynamic, options)
  end
end
