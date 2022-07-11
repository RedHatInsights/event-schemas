# This code may look unusually verbose for Ruby (and it is), but
# it performs some subtle and complex validation of JSON data.
#
# To parse this JSON, add 'dry-struct' and 'dry-types' gems, then do:
#
#   rhel_system = RHELSystem.from_json! "{…}"
#   puts rhel_system.rhel_system_system.tags&.first.key
#
# If from_json! succeeds, the value returned matches the schema.

require 'json'
require 'dry-types'
require 'dry-struct'

module Types
  include Dry::Types.module

  Hash   = Strict::Hash
  String = Strict::String
end

class RHELSystemTag < Dry::Struct
  attribute :key,       Types::String
  attribute :namespace, Types::String
  attribute :value,     Types::String

  def self.from_dynamic!(d)
    d = Types::Hash[d]
    new(
      key:       d.fetch("key"),
      namespace: d.fetch("namespace"),
      value:     d.fetch("value"),
    )
  end

  def self.from_json!(json)
    from_dynamic!(JSON.parse(json))
  end

  def to_dynamic
    {
      "key"       => @key,
      "namespace" => @namespace,
      "value"     => @value,
    }
  end

  def to_json(options = nil)
    JSON.generate(to_dynamic, options)
  end
end

# A RHEL system managed by console.redhat.com
class SystemClass < Dry::Struct
  attribute :display_name, Types::String.optional
  attribute :host_url,     Types::String.optional
  attribute :hostname,     Types::String.optional
  attribute :inventory_id, Types::String
  attribute :rhel_version, Types::String.optional
  attribute :tags,         Types.Array(RHELSystemTag).optional

  def self.from_dynamic!(d)
    d = Types::Hash[d]
    new(
      display_name: d["display_name"],
      host_url:     d["host_url"],
      hostname:     d["hostname"],
      inventory_id: d.fetch("inventory_id"),
      rhel_version: d["rhel_version"],
      tags:         d["tags"]&.map { |x| RHELSystemTag.from_dynamic!(x) },
    )
  end

  def self.from_json!(json)
    from_dynamic!(JSON.parse(json))
  end

  def to_dynamic
    {
      "display_name" => @display_name,
      "host_url"     => @host_url,
      "hostname"     => @hostname,
      "inventory_id" => @inventory_id,
      "rhel_version" => @rhel_version,
      "tags"         => @tags&.map { |x| x.to_dynamic },
    }
  end

  def to_json(options = nil)
    JSON.generate(to_dynamic, options)
  end
end

# Event data for a RHEL system.
class RHELSystem < Dry::Struct
  attribute :rhel_system_system, SystemClass

  def self.from_dynamic!(d)
    d = Types::Hash[d]
    new(
      rhel_system_system: SystemClass.from_dynamic!(d.fetch("system")),
    )
  end

  def self.from_json!(json)
    from_dynamic!(JSON.parse(json))
  end

  def to_dynamic
    {
      "system" => @rhel_system_system.to_dynamic,
    }
  end

  def to_json(options = nil)
    JSON.generate(to_dynamic, options)
  end
end
