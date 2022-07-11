# This code may look unusually verbose for Ruby (and it is), but
# it performs some subtle and complex validation of JSON data.
#
# To parse this JSON, add 'dry-struct' and 'dry-types' gems, then do:
#
#   empty = Empty.from_json! "…"
#   puts empty.nil?
#
# If from_json! succeeds, the value returned matches the schema.

require 'json'
require 'dry-types'
require 'dry-struct'

module Types
  include Dry::Types.module

  Nil = Strict::Nil
end

class Empty
  def self.from_json!(json)
    JSON.parse(json, quirks_mode: true)
  end
end
