require 'roo'
require 'spreadsheet'
require 'enumerator'

include Math

s = Roo::Spreadsheet.open('op.xls')

zipcode = s.column(2)
city = s.column(3)
state = s.column(4)
county = s.column(6)
latitude = s.column(10).map(&:to_f)
longitude = s.column(11).map(&:to_f)


# puts zipcode[1]
# puts city[1]
# puts state[1]
# puts latitude[1] 
# puts longitude[1]
# puts county[1]

#puts "zipcode = "
#in1 = gets.chomp
# puts "distance (mi)="
# in2 = gets.chomp

# puts in1
# puts zipcode[1]

# # current zipcode
# in1 = "94027"
# # distance (in miles) to search
# in2 = "3"

class Numeric
	def to_rad
		self * PI / 180	
	end
	def to_deg
		self * 180 / PI
	end
end
# def deg2rad(deg)
# 	return deg * PI / 180 
# end

# def rad2deg(rad)
# 	return rad * 180 / PI
# end


while true

	puts "Enter zipcode: "
	in1 = gets.chomp
	puts "Enter Distance: "
	in2 = gets.chomp

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

	# puts latN
	# puts latS
	# puts longE
	# puts longW

	f1 = latitude.each_with_index
	f1 = f1.select { |lat, index| lat<=latN && lat>=latS }

	indexLat = f1.map {|item| item[1]}

	f2 = longitude.each_with_index
	f2 = f2.select { |long, index| indexLat.include? index}

	# Get the list of longitudes filtered by latitude and apply longitude filter
	f3 = (f2.map { |item| item[0] }).select { |long| long>=longW && long<=longE }

	# puts f1.length
	# puts f3.length
	# puts f3

	# Find the indexes again
	f4 = f2.select { |long, index| f3.include? long}

	indexFiltered = f4.map { |long, index| index}

	indexFiltered.each {|index| puts zipcode[index], city[index], state[index] }

end






