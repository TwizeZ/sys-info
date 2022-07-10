import os
import platform
# Resources for sys_info

rel = platform.release()


def windows():
    pass

def mac():


    ver, _, _ = platform.mac_ver()
    ver = float('.'.join(ver.split('.')[:2]))



    rel_name = ""

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

    ver_name = "(" + ver_name + ")"

    sys = f"{sys} / {rel_name}"

def linux():
    pass