import cx_Oracle
import csv
con = cx_Oracle.connect('LOS/LO1907@alsrac-scan.alisannak.com:1521/local') 
cursor = con.cursor() 
cursor.arraysize=50    
cursor.execute("""select * from CARIAGRO_CN where AGROCODE='8681957313010' 
                    and DURUM_ZAMAN >= TO_DATE('01/01/2019','DD/MM/YYYY') AND DURUM_ZAMAN <= TO_DATE('25/12/2019','DD/MM/YYYY')
                    and GLN IN ('0012000980015','0012000980008','0072000490006',
                                '0422000670005','0352000300001','0352000300018',
                                '0102003840000','0352000220002','0352000220019',
                                '0012001110008','0012001110015','0552001660009',
                                '0452002690008','0012001220011','0012001220004',
                                '0632003030007','0632003030021','0332002290005',
                                '0552001670008','0072002910007','0422004100003',
                                '0592004020004','0422000820004','0352004200000')""")
with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([ i[0] for i in cursor.description ]) 
    writer.writerows(cursor.fetchall())