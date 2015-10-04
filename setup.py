import cx_Freeze

executables = [cx_Freeze.Executable("mygame.py")]

cx_Freeze.setup(
    name = "A bit Racey",
    options = {"build.exe":{"packages":["pygame"],
                            "include_files":["car.png"]}},
    executables = executables    
    )
