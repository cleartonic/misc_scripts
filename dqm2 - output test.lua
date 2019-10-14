function dumpscript()
	file = io.open("logs/log_1.txt","a")
	io.output(file)
	io.write("Test\n")
	io.close()
end
while true do
	emu.frameadvance()
	dumpscript()
end