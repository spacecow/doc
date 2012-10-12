#data.txt
#it has
#2 lines

File.open("data.txt", "r").each_line do |line|
  p line
end
#--> it has\n
#--> 2 lines\n
