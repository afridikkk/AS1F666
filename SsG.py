import os,platform
os.system('git pull')

aarch64=platform.architecture()[0]
if aarch64=="32bit":
    print('Sorry Update Your Phone...')
elif aarch64=="64bit":
    __import__("aarch64")
