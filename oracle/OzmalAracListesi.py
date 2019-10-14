import cx_Oracle
con = cx_Oracle.connect('TMS/TMS1907@alsrac-scan.alisannak.com:1521/local',encoding = "UTF-8", nencoding = "UTF-8")
cursor = con.cursor()
cursor.arraysize=50
cursor.execute("""SELECT v.PLATE_NO as PLAKA, vs.NAME as DURUM, vst.NAME as GROUP_ADI, vst.CODE as GROUP_KODU, v.MODEL_YEAR, v.OGS_NO,
    v.KGS_NO, v.TTS_NO, vt.NAME as ARAC_TIPI, c.COMPANY_TITLE as FIRMA, vb.NAME as MARKA from
    VEHICLE v, VEHICLE_TYPE vt, COMPANY c, VEHICLE_BRAND_MODEL vb, VEHICLE_STATUS vs, VEHICLE_STATEMENT vst
    where
    v.VEHICLE_TYPE_ID = vt.ID and v.COMPANY_ID = c.ID and v.VEHICLE_BRAND_MODEL_ID = vb.ID and
    v.VEHICLE_STATUS_ID = vs.ID and v.VEHICLE_STATEMENT_ID = vst.ID and vst.CODE != 'SP' ORDER BY PLAKA ASC""")
rows = cursor.fetchall()
for result in rows:
    print(result)
print("successful")