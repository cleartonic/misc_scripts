memory.usememorydomain("WRAM")

file = io.open("test.txt", "a")
io.output(file)
temp = 0
swap = 0


while true do
	if memory.readbyte(0x08DF) ~= 0x00 then
		temp =  emu.framecount()
		client.pause()
	end
	
	emu.frameadvance()
	gui.text(1,1,'Threat:'..memory.readbyte(0x08DF))
	gui.text(1,20,'Frame Count:'..temp)	

end

