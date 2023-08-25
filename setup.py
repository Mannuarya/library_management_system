from cx_Freeze import setup, Executable

setup(
    name = "abcd.db",
    version ="0.1",
    description ="Only for testing",
    executables = [Executable(r"front.py")] ,
)
