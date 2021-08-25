cluster = 4096
fileSize = int(input("Nhap vao kich thuoc file (Don vi byte) : "))
fileCount = 0

fileCount = (fileSize // cluster) * 4 if ((fileSize % cluster) == 0) else (fileSize // cluster + 1) * 4

print(f"So KB ma file do chiem la : {fileCount}KB")