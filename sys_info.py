import os
import platform
import resources

osn = os.name
name = platform.node()

rel = platform.release()

ver = ""

ver_name = ""


machine = platform.machine()
processor = platform.processor()

def main():
	print()

	print(f"OS: {osn}")
	print(f"Comupter name: {name}")

	print()

	print(f"System: {resources.sys}")
	print(f"Release: {rel}")
	print(f"Version: {ver}")

	print()

	print(f"Machine: {machine}")
	print(f"Processor: {processor}")

	print()

if __name__ in "__main__":
	
	if osn == "Darwin":
		var = resources.mac()
		print(var)
	elif osn == "Windows":
		resources.windows()
	elif osn == "Linux":
		resources.linux()
	
	main()