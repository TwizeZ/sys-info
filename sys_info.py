import os
import platform
import resources

osn = os.name

sys = platform.system()

rel = platform.release()

pl_ver = platform.version()


ver = "TEST"

ver_name = ""


machine = platform.machine()
processor = platform.processor()

def main():
	print()

	print(f"OS: {osn}")

	print()

	print(f"System: {sys}")
	print(f"Release: {rel}")
	print(f"Version: {ver} {ver_name}")
	print(f"Full version: {pl_ver}")

	print()

	print(f"Machine: {machine}")
	print(f"Processor: {processor}")

	print()

if __name__ in "__main__":
	
	if osn == "Darwin":
		resources.mac()
	elif osn == "Windows":
		resources.windows()
	elif osn == "Linux":
		resources.linux()
	
	main()