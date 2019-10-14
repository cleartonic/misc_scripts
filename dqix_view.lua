while true do
	gui.text(0,0,'RNG A: '..memory.readbyte(0x020EEE90)
	--gui.text(0,20,'RNG B: '..memory.readbyte(0x020EEE90)
	emu.frameadvance()
end