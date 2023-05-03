#!/usr/bin/env ruby
# Accept one argument
input = ARGV[0]

# Define a regular expression pattern
pattern = /hbt{2,5}n/i

# Match the input against the pattern
if input.match(pattern)
  puts ARGV[0].scan(pattern).join
end
