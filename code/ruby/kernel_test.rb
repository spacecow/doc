p test(?e,"/etc/passwd")     # e for exist, true
p test(?e,"/does/not/exist") # false
p test(?e,"/etc")            # true
p test(?d, "/etc")           # d for directory, true
p test(?d, "/etc/passwd")    # false
p test(?r, "/etc/passwd")    # r for readable, true
p test(?w, "/etc/passwd")    # w for writable, false
