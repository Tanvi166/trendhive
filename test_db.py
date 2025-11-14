import mysql.connector

db = mysql.connector.connect(
    host="mainline.proxy.rlwy.net",
    user="root",
    password="bsMapmRGNiMXLsNGqQyxrlAmFSKPDIOl",
    database="railway",
    port=41762,
    use_pure=True
)

print("Connected successfully!")
