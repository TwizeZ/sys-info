import os
import platform

os_name = os.name

sys = platform.system()

def windows():
	pass

def mac():
	pass

def linux():
	pass

rel = platform.release()

pl_ver = platform.version()

ver, _, _ = platform.mac_ver()
ver = float('.'.join(ver.split('.')[:2]))

ver_name = ""

rel_name = ""
if sys == "Darwin":
	if rel.startswith("22") and sys == "Darwin":
		ver_name = "Ventura"
		rel_name = "macOS"
	elif rel.startswith("21") and sys == "Darwin":
		ver_name = "Monterey"
		rel_name = "macOS"
	elif rel.startswith("20") and sys == "Darwin":
		ver_name = "Big Sur"
		rel_name = "macOS"
	elif rel.startswith("19") and sys == "Darwin":
		ver_name = "Catalina"
		rel_name = "macOS"
	elif rel.startswith("18") and sys == "Darwin":
		ver_name = "Mojave"
		rel_name = "macOS"
	elif rel.startswith("17") and sys == "Darwin":
		ver_name = "High Sierra"
		rel_name = "macOS"
	elif rel.startswith("16") and sys == "Darwin":
		ver_name = "Sierra"
		rel_name = "macOS"
	elif rel.startswith("15") and sys == "Darwin":
		ver_name = "El Capitan"
		rel_name = "OS X"
	elif rel.startswith("14") and sys == "Darwin":
		ver_name = "Yosemite"
		rel_name = "OS X"
	else:
		ver_name = "(Name not in database)"
		rel_name = "-"

	sys = f"{sys} / {rel_name}"
else:
	pass

machine = platform.machine()
processor = platform.processor()

print()

print(f"OS: {os_name}")

print()

print(f"System: {sys}")
print(f"Release: {rel}")
print(f"Version: {ver} ({ver_name})")
print(f"Full version: {pl_ver}")

print()

print(f"Machine: {machine}")
print(f"Processor: {processor}")

print()