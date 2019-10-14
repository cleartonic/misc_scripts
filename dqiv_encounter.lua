function wait(number)
	--gui.text(0,20,memory)
	while number > 0 do
		emu.frameadvance()
		gui.text(0,0,'Active')
		number = number - 1
		
		table=input.get()
		gui.text(0,10,table.right)
	end
end

function walk_right(number)
	while number > 0 do
		joypad.set({right=true})
		wait(1)
		number = number - 1
	end
end
function walk_left(number)
	while number > 0 do
		joypad.set({left=true})
		wait(1)
		number = number - 1
	end
end
	
function start_walk()
	walk_left(20)
	walk_right(20)
	wait(300)
	
	digit = memory.readbyte(0x020C761C)
	digit2 = memory.readbyte(0x020C761D)
	
	file = io.open("encounter_log.txt","a")
	io.output(file)
	io.write(digit2)
	io.write(" | ")
	io.write(digit)
	io.write("\n")
	io.close()
	
end

while true do
	start_walk()
end