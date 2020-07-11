# 블랙잭
# 딜러와 1:1 상황
# 카드가 무제한
# 베팅금액은 100
# 올인이 되거나 종료하고 싶을 때 종료

# 초기세팅
money = 100
playercards = []
dealercards = []

# 배팅
def 배팅():
    while True:
        betting = int(input("배팅금액 입력: "))
        if betting > money:
            print("보유자금보다 베팅금액이 큽니다")
        else:
            break
    return betting
'''
betting
def betting():
    global betting
    while True:
        betting = int(input("배팅금액 입력: "))
        if betting > money:
            print("보유자금보다 베팅금액이 큽니다")
        else:
            break
betting()
'''
# 카드받기
# 1~10중 하나 뽑기
import random
def 카드받기():
    for i in range(2):
        card = random.randrange(1,11)
        playercards.append(card)
        card = random.randrange(1,11)
        dealercards.append(card)
    print("플레이어의 카드 : ", playercards)
    print("딜러 카드 1장 오픈 : ", dealercards[0])

# 플레이어 카드받기 결정
def 카드받기결정():
    while True:
        receive = input("카드를 받으시겠습니까?(y/n) : ")
        if receive == "y" :
            card = random.randrange(1,11)
            playercards.append(card)
            print("플레이어의 카드 : ", playercards)
            #21을 넘었을경우 ==> 1 == 11
            sumplayercards = sum(playercards)
            if sumplayercards > 21:
                print(" 21을 초과하였습니다(버스트)")
                break
        elif receive == "n":
            break
    print("플레이어의 카드 : ", playercards)
    #딜러의 카드 오픈
    print("딜러의 카드 : ", dealercards)
    sumplayercards = sum(playercards)
    return sumplayercards

#딜러의 카드 받기
#17이상이 되기까지 받기
def 딜러의카드받기():
    sumdealercards = sum(dealercards)    
    while sumdealercards < 17:
        card = random.randrange(1,11)
        dealercards.append(card)
        print("딜러의 카드 : ", dealercards)
        sumdealercards = sum(dealercards)
        #21을 넘었을경우 ==> 1 == 11
        if sumdealercards > 21:
            print(" 21을 초과하였습니다(버스트)")
            break
    print("딜러의 카드 : ", dealercards)
    return sumdealercards

#결과
def 결과(sumplayercards, sumdealercards):
    if 1 in playercards and sumplayercards < 12:
        sumplayercards += 10
    print("플레이어 카드 총합 : ", sumplayercards)
    print("딜러 카드 총합 : ", sumdealercards)
    #case1 : 둘다 버스트가 아닌경우
    if sumplayercards < 22 and sumdealercards < 22:
        if sumplayercards > sumdealercards :
            print("플레이어가 승리했습니다")
        elif sumplayercards < sumdealercards :
            print("딜러가 승리했습니다")
        else:
            print("비겼습니다")

    elif sumplayercards > 21 and sumdealercards > 21:
        print("플레이어와 딜러 모두 버스트입니다")

    else:
        if sumplayercards >21:
            print("딜러가 승리하였습니다")
        else:
            print("플레이어가 승리하였습니다")




def main():
    while True:
        playercards = []
        dealercards = []
        if money <= 0:
            print ("배팅금액이 없습니다")
            break
        betting = 배팅()
        카드받기()
        플레이어_카드_총합 = 카드받기결정()
        딜러_카드_총합 = 딜러의카드받기()
        결과(플레이어_카드_총합, 딜러_카드_총합)

main()
