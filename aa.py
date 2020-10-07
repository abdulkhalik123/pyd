import os, re, requests, sys


def aws_key():
	os.system('cls')
	print('[+] GHOSTBIN  / PASTEBIN HARUS DI RAW')

	try:
		print("")
		url = input('[+] URL untuk grab ( jangan ber password ): ')
		tolol = requests.get(url).text
		KONTOLLLLLL = re.findall('URL: (.*)', tolol)
		kntol = re.findall('AWS_KEY:(.*)' , tolol)
		kntol2 = re.findall('AWS_SECRET:(.*)' , tolol)
		kntol3 = re.findall('AWS_REGION:(.*)' , tolol)

		#print(KONTOLLLLLL)
		
		for dananjing in KONTOLLLLLL:
			y = dananjing.strip()
			open('url.txt', 'a').write(y+'\n')
			print(y)
		for mailuser in kntol:
			user = mailuser.strip()
			open('username.txt', 'a').write(user+'\n')
			print(user)
		for mailpass in kntol2:
			pas = mailpass.strip()
			open('password.txt', 'a').write(pas+'\n')
			print(pas)
		for mailhost in kntol3:
			taiasu = mailhost.strip()
			open('host.txt', 'a').write(taiasu+'\n')
			print(taiasu)
		
	except Exception as e:
		print(e)

def aws_access_key():
	os.system('cls')
	print('[+] GHOSTBIN  / PASTEBIN HARUS DI RAW')

	try:
		print("")
		url = input('[+] URL untuk grab ( jangan ber password ): ')
		tolol = requests.get(url).text
		KONTOLLLLLL = re.findall('URL: (.*)', tolol)
		kntol = re.findall('AWS ACCESS KEY:(.*)' , tolol)
		kntol2 = re.findall('AWS SECRET KEY:(.*)' , tolol)
		kntol3 = re.findall('AWS REGION:(.*)' , tolol)

		#print(KONTOLLLLLL)
		
		for dananjing in KONTOLLLLLL:
			y = dananjing.strip()
			open('url.txt', 'a').write(y+'\n')
			print(y)
		for mailuser in kntol:
			user = mailuser.strip()
			open('username.txt', 'a').write(user+'\n')
			print(user)
		for mailpass in kntol2:
			pas = mailpass.strip()
			open('password.txt', 'a').write(pas+'\n')
			print(pas)
		for mailhost in kntol3:
			taiasu = mailhost.strip()
			open('host.txt', 'a').write(taiasu+'\n')
			print(taiasu)
		
	except Exception as e:
		print(e)

def strip():
	os.system('cls')
	print('[+] GHOSTBIN  / PASTEBIN HARUS DI RAW')

	try:
		print("")
		url = input('[+] URL untuk grab ( jangan ber password ): ')
		tolol = requests.get(url).text
		KONTOLLLLLL = re.findall('URL: (.*)', tolol)
		kntol = re.findall('MAILUSER:(.*)' , tolol)
		kntol2 = re.findall('MAILPASS:(.*)' , tolol)
		kntol3 = re.findall('MAILHOST:(.*)' , tolol)

		#print(KONTOLLLLLL)
		
		for dananjing in KONTOLLLLLL:
			y = dananjing.strip()
			open('url.txt', 'a').write(y+'\n')
			print(y)
		for mailuser in kntol:
			user = mailuser.strip()
			open('username.txt', 'a').write(user+'\n')
			print(user)
		for mailpass in kntol2:
			pas = mailpass.strip()
			open('password.txt', 'a').write(pas+'\n')
			print(pas)
		for mailhost in kntol3:
			kontolanjing = mailhost.split(".")
			open('host.txt', 'a').write(kontolanjing[1]+'\n')
			print(kontolanjing[1])
		
	except Exception as e:
		print(e)



def tai():
	os.system('cls')
	print('[+] GHOSTBIN  / PASTEBIN HARUS DI RAW')

	try:
		print("")
		url = input('[+] URL untuk grab ( jangan ber password ): ')
		tolol = requests.get(url).text
		KONTOLLLLLL = re.findall('URL: (.*)', tolol)
		kntol = re.findall('AWS_ACCESS_KEY_ID:(.*)' , tolol)
		kntol2 = re.findall('AWS_SECRET_ACCESS_KEY:(.*)' , tolol)
		kntol3 = re.findall('AWS_DEFAULT_REGION:(.*)' , tolol)

		#print(KONTOLLLLLL)
		
		for dananjing in KONTOLLLLLL:
			y = dananjing.strip()
			open('url.txt', 'a').write(y+'\n')
			print(y)
		for mailuser in kntol:
			user = mailuser.strip()
			open('username.txt', 'a').write(user+'\n')
			print(user)
		for mailpass in kntol2:
			pas = mailpass.strip()
			open('password.txt', 'a').write(pas+'\n')
			print(pas)
		for mailhost in kntol3:
			open('host.txt', 'a').write(mailhost+'\n')
			print(mailhost)
		
	except Exception as e:
		print(e)
def grab():
	a = open('url.txt', 'r').readlines()
	b = open('username.txt', 'r').readlines()
	c = open('password.txt', 'r').readlines()
	d = open('host.txt', 'r').readlines()

	for url,user,pas,reg in list(zip(a,b,c,d)):
		KONTOL= url.strip()
		u = user.strip()
		p = pas.strip()
		r = reg.strip()
		if u == "":
			pass
		else:
			anjing = '{}|{}|{}' .format(u,p,r)
			print(anjing)
			open('aws.txt', 'a').write(anjing+'\n')

print('[ 1 ] kalo username nya aws_key_id')
print('[ 2 ] SATUIN HASIL GRAB')
print('[ 3 ] kalo username mailuser')
print('[ 4 ] kalo username Aws_key')
print('[ 5 ] Kalo username AWS ACCESS KEY (boobs)')
print('[+] CARA PAKE')
print('[+] NO 1 dlu baru NO 2, yg 1 buat grab, yg 2 buat ngejadiin user|pass|region|bucket')
tong = input('[+] mana > ')
if tong == '1':
	tai()
elif tong == '2':
	grab()
	os.system('del url.txt')
	os.system('del username.txt')
	os.system('del password.txt')
	os.system('del host.txt')
	print('saved in aws.txt')
elif tong == '3':
	strip()
elif tong == '4':
	aws_key()
elif tong == '5':
	aws_access_key()
else:
	print('tolol')
