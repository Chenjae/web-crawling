import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

#네이버 검색어 순위 크롤링
#https://blog.naver.com/euijun54/221615620057

#파싱 페이지 요청
request = requests.get('http://www.naver.com/')
#target 페이지 정상 접속 확인, 200번대가 나오면 정
#print(request)

#페이지 정보중 html 코드만 얻어옴
html = request.text

soup = BeautifulSoup(html, 'html.parser')

# findAll('태그 이름',{'속성이름':'속성값'})
# 네이버 실시간 검색어는 class 속성이 'ah_k'인 span태그 내부에 들어있다.
words = soup.findAll('span',{'class':'ah_k'})
#print(words)

now = dt.now()
print("{} 현재 naver 실시간 검색어 top 20".format(now))
for i in range(20) :
    print('{0:2d}위 => {1}'.format(i+1, words[i].text))
