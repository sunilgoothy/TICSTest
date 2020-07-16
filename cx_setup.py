from cx_Freeze import setup, Executable 

setup(name = "test_loop_cx" , 
	version = "0.1" , 
	description = "" , 
	executables = [Executable("test_loop.py")]) 
