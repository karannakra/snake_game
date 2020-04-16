import cx_Freeze
executables=[cx_Freeze.Executable('snakes.py')]
cx_Freeze.setup(
    name="snake",
    options={"build_exe":{"packages":["pygame"],"include_files":["images/apple.png","images/icon.png",
    "images/new.png","images/snake.png","audio/back_sound.mp3","audio/over_sound.mp3"]}},
    description="snake game tutorial",
    executables=executables
)