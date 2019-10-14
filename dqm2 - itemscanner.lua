memory.usememorydomain("WRAM")

filename = "dumps/dqm2-tempitems.txt"
readdata = 0
iteration = 1

-- itemID1 = memory.readbyte(0x0C26)
-- itemID2 = memory.readbyte(0x0C2E)
-- itemID3 = memory.readbyte(0x0C36)
-- itemID4 = memory.readbyte(0x0C3E)
-- itemID5 = memory.readbyte(0x0C46)
-- itemID6 = memory.readbyte(0x0C4E)
-- itemID7 = memory.readbyte(0x0C56)
-- itemID8 = memory.readbyte(0x0C5E)
-- itemID9 = memory.readbyte(0x0C66)
-- itemID10 = memory.readbyte(0x0C6E)





-- TO DO : map ItemIDs to appropriate values (upon 019E becoming 42), then export to text file. Figure out how to make a data table from it

-- If 0x019E is 42, dump items

	
function checkplace()
	if (memory.readbyte(0x019E) == 68) then
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		emu.frameadvance()
		if memory.readbyte(0x0C25) == 0 then
			itemID1 = memory.readbyte(0x0C26)
		elseif memory.readbyte(0x0C25) == 1 then
			itemID1 = "Gold"
		end
		if memory.readbyte(0x0C2D) == 0 then
			itemID2 = memory.readbyte(0x0C2E)
		elseif memory.readbyte(0x0C2D) == 1 then
			itemID2 = "Gold"
		end
		if memory.readbyte(0x0C35) == 0 then
			itemID3 = memory.readbyte(0x0C36)
		elseif memory.readbyte(0x0C35) == 1 then
			itemID3 = "Gold"
		end
		if memory.readbyte(0x0C3D) == 0 then
			itemID4 = memory.readbyte(0x0C3E)
		elseif memory.readbyte(0x0C3D) == 1 then
			itemID4 = "Gold"
		end
		if memory.readbyte(0x0C45) == 0 then
			itemID5 = memory.readbyte(0x0C46)
		elseif memory.readbyte(0x0C45) == 1 then
			itemID5 = "Gold"
		end
		if memory.readbyte(0x0C4D) == 0 then
			itemID6 = memory.readbyte(0x0C4E)
		elseif memory.readbyte(0x0C4D) == 1 then
			itemID6 = "Gold"
		end
		if memory.readbyte(0x0C55) == 0 then
			itemID7 = memory.readbyte(0x0C56)
		elseif memory.readbyte(0x0C55) == 1 then
			itemID7 = "Gold"
		end
		if memory.readbyte(0x0C5D) == 0 then
			itemID8 = memory.readbyte(0x0C5E)
		elseif memory.readbyte(0x0C5D) == 1 then
			itemID8 = "Gold"
		end
		if memory.readbyte(0x0C65) == 0 then
			itemID9 = memory.readbyte(0x0C66)
		elseif memory.readbyte(0x0C65) == 1 then
			itemID9 = "Gold"
		end
		if memory.readbyte(0x0C6D) == 0 then
			itemID10 = memory.readbyte(0x0C6E)
		elseif memory.readbyte(0x0C6D) == 1 then
			itemID10 = "Gold"
		end
		if memory.readbyte(0x0C75) == 0 then
			itemID11 = memory.readbyte(0x0C76)
		elseif memory.readbyte(0x0C75) == 1 then
			itemID11 = "Gold"
		end
		if memory.readbyte(0x0C7D) == 0 then
			itemID12 = memory.readbyte(0x0C7E)
		elseif memory.readbyte(0x0C7D) == 1 then
			itemID12 = "Gold"
		end
		if memory.readbyte(0x0C85) == 0 then
			itemID3 = memory.readbyte(0x0C86)
		elseif memory.readbyte(0x0C85) == 1 then
			itemID3 = "Gold"
		end
		if memory.readbyte(0x0C8D) == 0 then
			itemID14 = memory.readbyte(0x0C8E)
		elseif memory.readbyte(0x0C8D) == 1 then
			itemID14 = "Gold"
		end
		if memory.readbyte(0x0C95) == 0 then
			itemID15 = memory.readbyte(0x0C96)
		elseif memory.readbyte(0x0C95) == 1 then
			itemID15 = "Gold"
		end
		
		gui.text(1,1,'Calling')
		file = io.open(filename,"a")
		io.output(file)
		io.write(iteration,',',emu.framecount()-30,',',itemID1,',',itemID2,',',itemID3,',',itemID4,',',itemID5,',',itemID6,',',itemID7,',',itemID8,',',itemID9,',',itemID10)
		--  ,',',itemID11,',',itemID12,',',itemID13,',',itemID14,',',itemID15)
		io.write("\n")
		io.close()
		iteration = iteration + 1
		readdata = 1
	else
		gui.text(1,1,memory.readbyte(0x019E))
	end
end



while iteration < 1001 do
	joypad.set({Right=false})
	savestate.loadslot(0)
	emu.frameadvance()
	joypad.set({Right=true})
	savestate.saveslot(0)
	while readdata == 0 do
		checkplace()
		emu.frameadvance()
	end
	readdata = 0
end

