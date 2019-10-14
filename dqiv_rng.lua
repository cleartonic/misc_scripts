function wait(number)
	while number > 0 do
		emu.frameadvance()
		gui.text(0,0,'Active')
		number = number - 1
	end
end


iteratenum = 1
function start()
	wait(1)
	rng = memory.readword(0x0211A7C4)
	rng2 = memory.readword(0x0211A7C6)
	joypad.set({A=true})
	wait(2)
	joypad.set({A=false})	
	change = memory.readbyte(0x020D0774)
	new_rng = memory.readword(0x0211A7C4)
	new_rng2 = memory.readword(0x0211A7C6)
	
	file = io.open("rng_log.txt","a")
	io.output(file)
	io.write(iteratenum.."|"..rng.."|"..rng2.."|"..change.."\n")
	io.close()
	
	savestate.load(0)
	memory.writeword(0x0211A7C4,new_rng)
	memory.writeword(0x0211A7C6,new_rng2)
	iteratenum = iteratenum + 1
end

while true do
	savestate.save(0)
	start()
end


