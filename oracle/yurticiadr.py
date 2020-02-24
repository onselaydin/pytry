import cx_Oracle
import csv
con = cx_Oracle.connect('TMS/TMS1907@alsrac-scan.alisannak.com:1521/local') 
cursor = con.cursor() 
cursor.arraysize=50    
cursor.execute("""select
TM.CODE
,SM.CODE as LOAD_CODE
,TM.START_DATE
,BP.NAME as ADR
,COM.NAME as CUSTOMERS
,regexp_replace(PROD.NAME, '([^,]+)(,\1)+', '\1') as PRODUCT_NAME
,PC.NAME as PRODUCT_CATEGORY_NAME
,SM.PALLET_QUANTITY
,regexp_replace(TR.PLATE_NO, '([^,]+)(,\1)+', '\1')  as PLATE_NO
,(select E.CODE from TMS.EQUIPMENT E ,TMS.TRANSPORTATION_EQUIPMENT T where E.ID = T.EQUIPMENT_ID and E.EQUIPMENT_TYPE_ID ='9818B4B013D5264CBBB7ADEE7B748A76' and T.TRANSPORTATION_MASTER_ID = TM.ID) as CONTAINER_NO
,SM.QUANTITY
,SM.UN_NO
,PT.NAME
,aco.name adr_code_name
,ac.name adr_class_name
,p.is_adr
,p.un_no
from TMS.SHIPMENT_MASTER SM
left outer join TMS.TRANSPORTATION_MASTER TM on TM.ID = SM.TRANSPORT_ID
left outer join TMS.BUSINESS_PROCESS BP on TM.BUSINESS_PROCESS_ID=BP.ID
left outer join TMS.COMPANY COM on COM.ID = SM.CUSTOMER_MASTER_ID
left outer join TMS.TRANSPORT_TRUCK TR on TR.TRANSPORTATION_MASTER_ID = SM.TRANSPORT_ID
left outer join TMS.TRANSPORT_TREYLER TT on TT.TRANSPORTATION_MASTER_ID = SM.TRANSPORT_ID
left outer join (select ID ,LISTAGG(to_char(NAME),',') WITHIN GROUP (ORDER BY 1) NAME from TMS.PRODUCT group by ID) PROD on PROD.ID = SM.PRODUCT_ID
left outer join TMS.ORDER_STATUS OS on OS.ID = SM.STATUS_ID
left outer join TMS.TRANSPORT_TYPE T on T.ID = SM.TRANSPORT_TYPE_ID
left outer join TMS.PRODUCT_CATEGORY PC on PC.ID =SM.PRODUCT_CATEGORY_ID
left outer join CORE.PROJECT PROJ on  PROJ.ID = SM.PROJECT_ID
left outer join TMS.PACKAGE_TYPE PT ON SM.PACKAGE_TYPE_ID=PT.ID
left outer join tms.product P ON SM.PRODUCT_ID=P.ID
left outer join tms.adr_class ac on p.adr_class_id=ac.id
left outer join tms.adr_code aco on p.adr_code_id=aco.id
WHERE TM.START_DATE >= to_date('01.01.2019','DD.MM.YYYY') and TM.START_DATE < to_date('01.01.2020','DD.MM.YYYY') and bp.id='267AB720713BC841A3A5D4C99759008B' or bp.id='700122E4EFF1B6D8E053790F100A1A03'""")
with open('YURT_ICI_ADR.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([ i[0] for i in cursor.description ])
    writer.writerows(cursor.fetchall())