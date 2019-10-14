--  174 frames. If 00FC11 is 44 when 174 frames from confirming attack, miss. 

-- Geno : 100 frames
-- Bowser : 72 frames
-- Mario : 100 frames (to be safe)

--
-- Hammer Bro: 10%
-- Croco: 20%
-- Valentina: 10%
-- Czar Dragon: 20%
-- Axem Red: 10%
--

memory.usememorydomain("WRAM")
hit = 0
miss = 0
error1 = 0
counter1 = 100
total = 1000
byteread = 0x00FC11
-- 00FC11 for Czar  |  00FC91 for Zombone
bytevalue = 146
-- 120 for Czar | Variable (8) for Zombone

savestate.loadslot(0)
savestate.saveslot(9)
	
function advance()
	counter2 = counter1
	while counter2 > 0 do
		emu.frameadvance()
		counter2 = counter2 - 1
		gui.text(300,0,'Hit:'..hit)
		gui.text(300,20,'Miss:'..miss)			
		gui.text(300,40,'Percentage:'..(hit/(hit+miss)))
	end
	emu.frameadvance()
	
end


while total > 0 do 
	savestate.loadslot(9)
	emu.frameadvance();
	emu.frameadvance();
	joypad.set({A=true},1)	
	savestate.saveslot(9);
	gui.text(300,0,'Hit:'..hit)
	gui.text(300,20,'Miss:'..miss)
	gui.text(300,40,'Percentage:'..(hit/(hit+miss)))
	advance()
	if memory.readbyte(byteread) == bytevalue then
		miss = miss + 1
		gui.text(300,60,'MISS')
		gui.text(300,80,'MISS')
	else
		hit = hit + 1
		gui.text(300,60,'HIT')
	end

	emu.frameadvance();
	total = total - 1
end

while true do 
	emu.frameadvance();	
	gui.text(300,0,'Hit:'..hit)
	gui.text(300,20,'Miss:'..miss)
	gui.text(300,40,'Percentage:'..(hit/(hit+miss)))

end

		