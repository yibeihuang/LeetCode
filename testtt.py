__author__ = 'yibeihuang'
# def  krakenCount(m, n):
    # i,j= 1,1
    # dp = [1 for k in range(n)]
    # while i<m:
    #     j=1
    #     while j<n:
    #         if j==1:
    #             tmp,prev=1,dp[j]
    #             dp[j]=dp[j]+dp[j-1]+tmp
    #             j+=1
    #         else:
    #             tmp = dp[j]
    #             dp[j]=dp[j]+dp[j-1]+prev
    #             prev,j=tmp,j+1
    #     i+=1
    # #print (dp[j])
    # return dp[j-1]
#     dp1 = [1 for k in range(n)]
#     dp2 = [0 for k in range(n)]
#     i,j=1,0
#     while i<m:
#         j=0
#         while j<n:
#             if j==0:
#                 dp2[j]=dp1[j]
#                 j+=1
#             else:
#                 dp2[j]=dp1[j]+dp1[j-1]+dp2[j-1]
#                 j+=1
#         i+=1
#         if i<n:
#             tmp=dp1[:]
#             dp1=dp2[:]
#             dp2=tmp[:]
#         else:
#             return dp2[-1]
#     return dp1[-1]
#
#
# m=2
# n=3
# print(krakenCount(m,n))

def  decrypt(en_msg):
    pos = en_msg[-18:].lower()
    #pos=en_msg
    print(pos)
    origin = list('The quick brown fox jumps over the lazy dog')
    prekey = []
    for i in range(len(pos)):
        if pos[i]!=',' and pos[i]!=' ':
            prekey.append((ord(pos[i])-ord(origin[i]))%26)
    print prekey
    print (en_msg)
    j = 7
    while j>0:
        i = 0
        while i<7:
            if prekey[i]!=prekey[i+7]:break
            else:i+=1
        if i==7: break
        else:j-=1
    if j!=0:prekey=prekey[:j]
    print('======')
    print(prekey)
    rst = []
    i,j=0,0
    while i<len(en_msg):
        if en_msg[i].isalpha():
            if en_msg[i].islower() and ord(en_msg[i])-prekey[j%len(prekey)]>=ord('a'):
                rst.append(chr(ord(en_msg[i])-prekey[j%len(prekey)]))
            elif en_msg[i].islower() and ord(en_msg[i])-prekey[j%len(prekey)]<ord('a'):
                rst.append(chr(ord(en_msg[i])-prekey[j%len(prekey)]+26))
            elif en_msg[i].isupper() and ord(en_msg[i])-prekey[j%len(prekey)]>=ord('A'):
                rst.append(chr(ord(en_msg[i])-prekey[j%len(prekey)]))
            elif en_msg[i].isupper() and ord(en_msg[i])-prekey[j%len(prekey)]<ord('A'):
                rst.append(chr(ord(en_msg[i])-prekey[j%len(prekey)]+26))
            i,j=i+1,j+1
        else:
            rst.append(en_msg[i])
            i+=1
    return ''.join(rst)

# msg = 'Atvt hrqgse, Cnikg'
msg = 'Bjj rwkcs dwpyp fwz ovors wxjs vje tcez fqg'
print(decrypt(msg))