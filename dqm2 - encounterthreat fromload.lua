memory.usememorydomain("WRAM")

file = io.open("test.txt", "a")
io.output(file)

run = 1



function Wait(number)

	while number > 0 do
		emu.frameadvance()
		gui.text(1,1,'Threat:'..memory.readbyte(0x08DF))
		number = number - 1
	end
	io.write(memory.readbyte(0x08DF))
end

while true do
	savestate.loadslot(0)
	emu.frameadvance()
	savestate.saveslot(0)
	joypad.set({A=true})	
	Wait(120)
end

