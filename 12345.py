import os
count0=0
count1=0

def fun(path):
	global count0,count1
	li=os.listdir(path)
	for i in li:
		p1=path+'\\'+i
		# if ' .scr' in p1:
		# 	os.remove(p1)
		# 	count0+=1

		# 	print('remove:',p1)
		if target=='folder':
			if os.path.isdir(p1):
				if operation=='hide':
					os.system('attrib +a +s +h +r '+p1)
					count1+=1
					print('attrib +a +s +h +r '+p1)
				else:
					os.system('attrib -a -s -h -r '+p1)
					count1+=1
					print('attrib -a -s -h -r '+p1)
				if recursion=='yes':
					fun(p1)
		if target=='file':
			if os.path.isfile(p1):
				if operation=='hide':
					os.system('attrib +a +s +h +r '+p1)
					count1+=1
					print('attrib +a +s +h +r '+p1)
				else:
					os.system('attrib -a -s -h -r '+p1)
					count1+=1
					print('attrib -a -s -h -r '+p1)
			else:
				if recursion=='yes':
					fun(p1)

		if target=='all':
			if operation=='hide':
				os.system('attrib +a +s +h +r '+p1)
				count1+=1
				print('attrib +a +s +h +r '+p1)
			else:
				os.system('attrib -a -s -h -r '+p1)
				count1+=1
				print('attrib -a -s -h -r '+p1)
			if os.path.isdir(p1):
				if recursion=='yes':
					fun(p1)


path=input('path:')
while True:
	operation=input('操作类型:hide or recovery\n')
	if operation=='hide' or operation=='recovery':
		break

while True:
	target=input('文件类型:file or folder or all\n')
	if target=='file' or target=='folder' or target=='all':
		break

while True:
	recursion=input('是否递归:yes or no\n')
	if recursion=='yes' or recursion=='no':
		break

fun(path)

# print('病毒数量：',count0)
print('处理文件数量:',count1)
