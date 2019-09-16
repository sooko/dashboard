[app]
title = Fi Tacho
version = 0.3
package.name = FiTacho
package.domain = www.sooko.io
source.dir = .
orientation = sensorLandscape
p4a.local_recipes = ../../recipes
fullscreen = 0
# (str) Icon of the application
#icon.filename = /home/han/PycharmProjects/untitled1/able/examples/fi/icon.png
#presplash.filename = /home/han/PycharmProjects/untitled1/able/examples/fi/icon.png
source.include_exts = py,png,jpg,kv,atlas,ttf
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION,WAKE_LOCK,INTERNET,ACCESS_NETWORK_STATE
requirements = hostpython2,kivy,android,able,plyer
android.wakelock = True
p4a.bootstrap = sdl2
[buildozer]
warn_on_root = 1
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2


