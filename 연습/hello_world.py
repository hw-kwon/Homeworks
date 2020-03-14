# from random import*
# online = randint(4, 28)
# offline = randint(4, 28)

# print('오프라인 스터디 모임 날짜는 매월' + str(offline) + '일로 선정되었습니다.')
# print('온라인 스터디 모임 날자는 매월' + str(online) + '일로 전정되었습니다.')

# a = '권현우'
# print(a.find('건'))
# print(a.index('권'))

# print('나는 %d 살 입니다' % 20)
# print('나는 %s 을 좋아해요' % '파이싼')
# print('apple 은 %c 로 시작해요' % 'a')
# print('나는 %s 와 %s,%s 를 좋아해요' % ('축구', '농구', '야구'))

# print('나는 {}살 입니다' .format(20))
# print('나는 {1} 와 {0} 를 좋아해요'.format(1, 2))
# print('나는 {age}이며 {color}을 좋아해요'.format(age=27, color='blue'))

# age = 27
# color = 'blue'
# print(f'나는 {age}이며 {color}을 좋아해요')

# print('백문이 불여 일견 \n 백견이 불여일타')
# print('저는 "나도 코딩"입니다')
# print('저는 \'나도 코딩\' 입니다.')

# # // : 문장 내에서 \
# print('가\\나\\다')
# # \r : 커서를 맨 앞으로
# print('red apple\rpine')
# # \b : 백스페이스
# print('권현우우\b우')


# url = 'https://naver.com'
# my_str = url.replace('https://', '')
# # print(my_str)
# my_str = my_str[:my_str.index('.')]
# # print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
# print('%s 의 비밀번호는 %s 입니다.' % (url, password))

# url = 'https://google.com'
# # 조건1
# my_str = url.replace('https://', '')
# # 조건2
# my_str = my_str[:6]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('g')) + '$$'
# # print('{}의 비밀 번호는 {}입니다.'.format(url, password))

# subway = ['유재석', '박명수', '조세호']
# print(subway.index('유재석')+1)

# subway.append('하하')
# print(subway)

# subway.insert(1, '정형돈')
# print(subway)

# subway.pop()
# print(subway)

# subway.pop(2)
# print(subway)

# subway.insert(1, '유재석')
# print(subway)
# print(subway.count('유재석'))

# # 숫자 정렬
# num_list = [1, 2, 5, 8, 6]
# num_list.sort()
# print(num_list)

# cabinet = {1: '유재석', 4: '박명수'}
# print(cabinet[1])
# print(cabinet.get(4))
# print(cabinet.get(5, '사용가능'))
# cabinet[4] = '하하'
# print(cabinet[4])
# cabinet[5] = '정준하'
# print(cabinet)
# print(cabinet.keys())

# cabinet.clear()
# print(cabinet)

# 튜플
# menu = ('돈까스', '치즈까스')
# print(menu[1])
# print(menu)

# (name, age, hobby) = ('김종국', 20, '헬스')
# print(name, age, hobby)

# 집합
# # 중복 안됨, 순서없음
# my_set = {1, 2, 3, 4, 4, 4, 5}
# print(my_set)

# java = {'재석', '명수', '하하'}
# python = set({'재석', '준하', '광희'})
# # 교집합
# print(java & python)
# # 힙집합
# print(java | python)
# # 차집합(자바는 가능 파이써는 불가)
# print(java - python)
# python.add('태호')
# print(python)
# java.remove('재석')
# print(python)


# menu = {'커피', '주스', '우유'}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# from random import*
# user = range(1, 21)
# user = list(user)
# # print(type(user))
# shuffle(user)
# print(user)
# winner = sample(user, 4)
# print(winner)

# print('치킨 당첨자 : {}' .format(winner[0]))
# print('커피 당첨자 : {}'.format(winner[1:4]))

# weather = input('오늘 날씨?')
# if weather == '비':
#     print('준비 우산')

# for waiting_no in range(1, 100, 10):
#     print('대기번호 : {0}'.format(waiting_no))

# absent = [2, 5]
# for student in range(1,10):
#     if student in absent:
#         continue
#     print

from random import*
customer = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if time >= 5 and time <= 15:
        print('[o] {}번째 손님 (소요시간 : {}'.format(i, time))
        customer += 1
    else:
        print('[x] {}번째 손님 (소요시간 : {}'.format(i, time))
print('총 탑승 승객 : {}'.format(customer))

# def open_account():
#     print('새로운 계좌')


# def deposit(balance, money):
#     print('입금 완료. 잔액 : {}'.format(balance + money))
#     return balance + money
# def withdraw(balance,money):

# balance = 0
# balance = deposit(balance, 1000)
# print(balance)

# def profile(name, age=14, main_lang='없음'):
#     print('이름 : {0}, 나이 : {1}, 언어 : {2}'
#           .format(name, age, main_lang))


# profile('유재석', 20, '파이썬')
# profile('김태호', 21, '자바')
# profile('정준하')
# profile('하하')

# def profile(name, age, hobby):
#     print(name, age, hobby)


# profile(name='유재석', hobby='soccer', age='12')

# def std_weight(height, gender):
#     if gender == '남자':
#         return height * height * 22
#     else:
#         return height * height*21


# height = 178
# gender = '남자'
# weight = round(std_weight(height/100, gender), 2)
# print('키{0}cm {1}의 표준체중은 {2}kg 입니다.' .format(height, gender, weight))


# print('가', '나', sep=',', end='?')

# scores = {'수학': 0, '영어': 10, '코딩': 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=':')

# for number in range(1, 21):
#     print('대기번호 :' + str(number).zfill(3))

# answer = input('아무거나 : ')
# print('입력값은' + answer + '입니다')


# # # 3자리마다 콤마
# # print('{0:+,}'.format(10000000000))

# # print('{0:^<+50,}'.format(100000000))

# # # 소수점
# # print('{0:.2f}'.format(5/2))

# # class
# class unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print('{}유닛 생성'.format(self.name))
#         print('체력{},공격력{}'.format(self.hp, self.damage))


# class attack_unit:
#      def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print('{}유닛 생성'.format(self.name))
#         print('체력{},공격력{}'.format(self.hp, self.damage))

#     def attack(self,location):
#         print('{}:{} 방향으로 적 공격. 공격력{}'.format(self.name, location, self.damage))


#     def damaged(self, damage):
#         print()
