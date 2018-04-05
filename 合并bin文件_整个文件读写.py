import os

AllFile = os.listdir()
DocTimeDict = {}
for FileNameTmp in AllFile:
	DocTimeDict[FileNameTmp] = os.path.getmtime(FileNameTmp)
AllFileName = sorted(DocTimeDict.items(), key = lambda x:x[1])
AllFileNumber = len(AllFile)
print(AllFileNumber)
print(AllFileName)

for FileName in AllFileName:
	if FileName[0].split('.')[-1] == 'bin':
		with open(FileName[0], 'rb') as FileRead:
			print(FileName[0])
			FileReadData = FileRead.read()
			with open('testreadwrite.bin', 'ab') as FileWrite:
				FileWrite.write(FileReadData)
				# for i in SingleLineData:
				# 	print('%02X '%i, end = '')
				
			print()
			
