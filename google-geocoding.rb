require 'net/http'
require 'uri'
# requires json gem installation
require 'json'

site = "https://maps.googleapis.com/maps/api/geocode/"
rtype = "json"
query = "514 High St."
api_key = ""

#Encode query to be a valid url segment
query = URI.encode(query)

url = site + rtype + "?address=" + query + "&key=" + api_key

uri= URI.parse(url)
http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true
request = Net::HTTP::Get.new(uri)
response = http.request(request)

puts gc_array = JSON.parse(response.body)

# while true
# 	puts "Enter value: "
# 	val = gets.chomp
# 	puts gc_array[val]
# end