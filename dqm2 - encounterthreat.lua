memory.usememorydomain("WRAM")
enixmenu = 54
dqm2 = 59
loadmenu = 71
confirm = 15


run = 1

function Wait(number)

	temp = number
	while temp > 2 do
		emu.frameadvance()
		temp = temp - 1
	end
	joypad.set({A=true})
	temp = temp - 2
	emu.frameadvance()
	emu.frameadvance()	
	joypad.set({A=false})
end

function Wait2(number)

	while number > 0 do
		emu.frameadvance()
		gui.text(1,1,'Threat:'..memory.readbyte(0x08DF))
		number = number - 1
	end
end

while true do
	savestate.loadslot(1)
	Wait(enixmenu)
	Wait(dqm2)
	Wait(loadmenu)
	Wait(confirm)
	Wait(52)	-- Hardcode	
	Wait2(120)
	enixmenu = enixmenu + 1

end

