file=open('centos7_pu安_product.txt', mode='a',encoding='utf8')
i=10
while i<1025:
    m=str(i).zfill(4)


    file.write('''INSERT GOS_CAS.ProductInfo(ProductInfoID,ProductNum,Description,Reserved1,Reserved2,SMSID,SetCmdTime,AreaID) values (null,%d,"servic%d",1,1,4294967295,UNIX_TIMESTAMP(NOW()),65535);\n'''%(i,i))
    # file.write('''INSERT GOS_CAS.ACInfo(ACInfoID,ACIndex,ACData,BeginTime,EndTime,SetCmdTime,ACVersion,Reserved1,Reserved2,AreaID) values (null,"0001%s","3f000870ffff8a00000000639a5551000000007596000101800008","1671058769","1671058769",UNIX_TIMESTAMP(NOW()),10,7,7,1);\n''' % (m))
    i+=1
    print(i)#
file.close()