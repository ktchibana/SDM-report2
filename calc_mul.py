#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^\d+$') # 整数のみをマッチさせる正規表現
        if p.match(ai) and p.match(bi): # A, Bの両方が整数であることを確認
                a=int(ai) # Aを整数に変換
                b=int(bi) # Bを整数に変換
                if 0 < a < 1000 and 0 < b <1000: # A, Bの範囲を修正
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
