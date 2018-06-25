#Verify that the subdomain exists
# -*- coding:utf-8 -*-  
import requests
import sys

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'} 

class Validation_survive:
	
	def readURL(self,filePath,httpType):
		with open(filePath, 'r') as f1:
			list1 = f1.readlines()
		for i in range(0,len(list1)):
			list1[i] = httpType+'://'+list1[i].rstrip('\n')
		return list1
		
	def getCode(self,UrlList):
		trueList =[]
		
		for i in range(0,len(UrlList)):	
			try:
				#verify=False  关闭对https证书的校验
				r = requests.get(UrlList[i],headers=headers, timeout=2,verify=True)
				print(r.status_code)
				print(UrlList[i])
				if(r.status_code == 200 or r.status_code == 301):					
					trueList.append(UrlList[i])
			except Exception as e:
				print("Error")
		return trueList
		
	def writefile(self,trueList):
		for i in range(0,len(trueList)):
			with open('aaa.txt', 'a') as f2:
				f2.write(trueList[i]+'\n')
				
if __name__ == "__main__":
	if(len(sys.argv) != 3):
		print("Usage:")
		print("python test.py url.txt http  or https ")
	else:	
		vs = Validation_survive()
		list1 = vs.readURL(sys.argv[1],sys.argv[2])
		trueList = vs.getCode(list1)
		vs.writefile(trueList)
	