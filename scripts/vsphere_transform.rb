#!/usr/bin/env ruby

require 'json'

def transform(input)
  json = JSON.parse(input)
  data = {servers: []}
  json["VirtualMachines"].each do |vm|
    props = {}
    config = vm["Summary"]["Config"]
    run = vm["Runtime"]
    props[:host_name] = config["Name"]
    props[:description] = config["Annotation"]
    props[:assigned_id] = config["Uuid"]
    props[:ram_allocated_gb] = config["MemorySizeMB"] / 1024
    props[:cpu_count] = config["NumCpu"]
    props[:ram_used_gb] = run["MaxMemoryUsage"] / 1024
    props[:virtual] = true

    stats = vm["Summary"]["QuickStats"]
    custom = {status:  stats["GuestHeartbeatStatus"],
              product: config["Product"] ? config["Product"]["Name"] : false }
    props[:custom_fields] = custom
    props[:environment] = 'Development'

    data[:servers].push props
  end
  data
end

# Read in data from STDIN
data = STDIN.read

# Transform data
output = transform data

# Output transformed data to STDOUT
puts JSON.generate output
