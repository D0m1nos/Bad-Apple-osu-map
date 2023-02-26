import subprocess

begin = int(input("Create video from part (included): "))
end = int(input("to part (included): "))

for i in range(begin, end+1):
    subprocess.call(['danser-cli.exe', '-t=Bad Apple!!', '-c=ouranhshc', f'-d=part{i}', '-settings=show map', f'-out=part{i}', '-skip'])