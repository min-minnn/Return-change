"""
사용자는 1000원 지폐, 500원 동전, 100원 동전을 사용할 수 있다.
구매할 물건값을 입력하고 1000원, 500원, 100원의 개수를 입력하면 거스름돈을 계산하여 반환해주는 프로그램을 작성

<조건>
1) 거스름돈은 500원과 100원으로 반환
2) 물건값보다 투입한 돈이 더 적을 경우 "돈이 부족합니다" 메시지 나타나며 종료
"""

cost = int(input('물건값: '))
cheon = int(input('1000원 개수: '))
oback = int(input('500원 개수: '))
back = int(input('100원 개수: '))

money = cheon * 1000 + oback * 500 + back * 100

if money == cost:
    print('-----거스름돈-----')
    print('500원 개수: 0 , 100원 개수: 0')
elif money < cost:
    print('돈이 부족합니다.')
else:
    change = abs(cost - money)
    
    five = change//500
    one = (change - 500*five)//100

    print('-----거스름돈-----')
    print('500원 개수: ', five, ', 100원 개수: ', one)