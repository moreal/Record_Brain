# 콘솔에 출력할 때는 print 함수를 사용한다.
# print의 형식은 다음과 같다. print(value, ..., sep=' ', end="\n",file=sys.stdout,flush=False)
# 인자가 하나 더 있었던 것 같지만 일단은 그러하다. 이를 통해 파일 쓰기도 정말 손쉽게 가능하다.

print("hello","world", sep='\n', end="")

# 출력할 값들을 python2와 동일하게 가변으로 받지만 sep을 기본값인 ' '에서 '\n' 로 바꾸워서 한줄 한줄 출력하게 나온다.
# end도 "\n"을 "" 로 바꾸어 맨 마지막에는 개행이 안 되도록 처리하였다.