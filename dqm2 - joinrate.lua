memory.usememorydomain("WRAM")
join = 0
nojoin = 0
total = 500
initialtotal = total
client.displaymessages = false




while (total > 0) do
	savestate.loadslot(0)
	emu.frameadvance();
	savestate.saveslot(0);
	
	gui.text(300,0,'Join:'..join)
	gui.text(300,20,'No join:'..nojoin)
	gui.text(300,40,'%:'..(join/(join+nojoin)))
	
	
	frames = 40

	joypad.set({A=true})
	emu.frameadvance();
	
	gui.text(300,0,'Join:'..join)
	gui.text(300,20,'No join:'..nojoin)
	gui.text(300,40,'%:'..(join/(join+nojoin)))
	
	while (frames > 0) do
		emu.frameadvance();
		gui.text(300,0,'Join:'..join)
		gui.text(300,20,'No join:'..nojoin)
		gui.text(300,40,'%:'..(join/(join+nojoin)))
		frames = frames - 1
	end
	if (memory.readbyte(0x1FB7) == 0xFC) then
		join = join + 1
	else 
		nojoin = nojoin + 1
	end
		total = total - 1
	

end


while true do
		emu.frameadvance()
		gui.text(300,0,'Total Runs:'..initialtotal)
		gui.text(300,20,'%:'..(join/(join+nojoin)))	
end