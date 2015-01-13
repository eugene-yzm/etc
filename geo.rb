require 'roo'
require 'spreadsheet'
require 'enumerator'

include Math

s = Roo::Spreadsheet.open('./CA.xls')

zipcode = s.column(1)
city = s.column(2)
state = s.column(3)
latitude = s.column(4)
longitude = s.column(5)
county = s.column(6)

# current zipcode
in1 = "94027"
# distance (in miles) to search
in2 = "3"

class Numeric
	def to_rad
		self * PI / 180	
	end
	def to_deg
		self * 180 / PI
	end
end

# puts zipcode.find_index(in1)
zc_index = zipcode.find_index(in1)
lat1 = latitude[zc_index]
long1 = longitude[zc_index]
dist = in2.to_f
radius = 3959


latN = (asin(sin(lat1.to_rad) * cos(dist/radius) + cos(lat1.to_rad) * sin(dist/radius) * cos(0.to_rad))).to_deg
latS = (asin(sin(lat1.to_rad) * cos(dist/radius) + cos(lat1.to_rad) * sin(dist/radius) * cos(180.to_rad))).to_deg
longE = (long1.to_rad + atan2(sin(90.to_rad) * sin(dist/radius) * cos(lat1.to_rad) , cos(dist/radius) - sin(lat1.to_rad) * sin(latN.to_rad))).to_deg
longW = (long1.to_rad + atan2(sin(270.to_rad) * sin(dist/radius) * cos(lat1.to_rad) , cos(dist/radius) - sin(lat1.to_rad) * sin(latN.to_rad))).to_deg

f1 = latitude.each_with_index
f1 = f1.select { |lat, index| lat<=latN && lat>=latS }

indexLat = f1.map {|item| item[1]}

f2 = longitude.each_with_index
f2 = f2.select { |long, index| indexLat.include? index}

# Get the list of longitudes filtered by latitude and apply longitude filter
f3 = (f2.map { |item| item[0] }).select { |long| long>=longW && long<=longE }

# Find the indexes again
f4 = f2.select { |long, index| f3.include? long}

p indexFiltered = f4.map { |item| item[1]}

indexFiltered.each {|index| puts zipcode[index], city[index], state[index] }








