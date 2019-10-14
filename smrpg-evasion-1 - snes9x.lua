--  174 frames. If 7EFC11 is [check value] when 150 frames from confirming attack, miss. 

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


hit = 0
miss = 0
error1 = 0
counter1 = 150
total = 1000
byteread = 0x7EFC11
-- 00FC11 for Czar  |  00FC91 for Zombone
-- 7EFDC5
bytevalue = 64
-- 120 for Czar | Variable (8) for Zombone
state1 = savestate.create(1)

function advance()
	counter2 = counter1
	while counter2 > 0 do
		emu.frameadvance()
		counter2 = counter2 - 1
		gui.text(0,0,'Hit:'..hit)
		gui.text(0,10,'Miss:'..miss)
		gui.text(0,20,'Percentage:'..(hit/(hit+miss)))
		gui.text(0,30,memory.readbyte(byteread))
	end
	emu.frameadvance()
	
end


while total > 0 do 
	savestate.load(state1)
	emu.frameadvance();
	emu.frameadvance();
	joypad.set({A=true},1)	
	savestate.save(state1);
	gui.text(0,0,'Hit:'..hit)
	gui.text(0,10,'Miss:'..miss)
	gui.text(0,20,'Percentage:'..(hit/(hit+miss)))
	gui.text(0,30,memory.readbyte(byteread))
	advance()
	if memory.readbyte(byteread) == bytevalue then
		miss = miss + 1
		gui.text(0,0,'MISS')
		gui.text(0,10,memory.readbyte(byteread))
	else
		hit = hit + 1
		gui.text(0,10,memory.readbyte(byteread))
		gui.text(0,20,'HIT')
	end

	emu.frameadvance();
	emu.frameadvance();
	emu.frameadvance();
	emu.frameadvance();
	emu.frameadvance();
	emu.frameadvance();
	emu.frameadvance();
	
	
	total = total - 1
end

while true do 
	emu.frameadvance();	
	gui.text(0,0,'Hit:'..hit)
	gui.text(0,20,'Miss:'..miss)
	gui.text(0,40,'Percentage:'..(hit/(hit+miss)))

end

		