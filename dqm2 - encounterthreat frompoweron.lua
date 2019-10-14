memory.usememorydomain("WRAM")
enixmenu = 43
dqm2 = 59
loadmenu = 73
confirm = 18

file = io.open("test.txt", "a")
io.output(file)

run = 1

function Wait(number)

	temp = number
	while temp > 2 do
		emu.frameadvance()
		temp = temp - 1
	end
	temp = temp - 2
	emu.frameadvance()
	joypad.set({A=true})
	emu.frameadvance()
	joypad.set({A=true})	
end


function Wait2(number)

	while number > 0 do
		emu.frameadvance()
		gui.text(1,1,'Threat:'..memory.readbyte(0x08DF))
		number = number - 1
	end
	io.write(memory.readbyte(0x08DF))
end

while true do
	savestate.loadslot(1)
	Wait(enixmenu)
	Wait(dqm2)
	Wait(loadmenu)
	Wait(confirm)
	Wait2(120)
	dqm2 = dqm2 + 2

end

