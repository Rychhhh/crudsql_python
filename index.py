import mysql.connector

koneksi = mysql.connector.connect(
    host = "127.0.0.1",
    user= "root",
    password = "",
    database= "coba_python_sql"
)

mycursor = koneksi.cursor()

lanjut = True
if lanjut:
    print("")
    print("")
    print("")
    print("CRUD Python")
    print("1. Lihat User")
    print("2. Tambah User")
    print("3. Edit User")
    print("4. Delete User")
    print("5. Keluar")
    print("")
else: 
    print("Out...")

guest = int(input("Pilih Menu : "))
print("")

if(guest == 1) :
    mycursor.execute("SELECT * FROM user")
    result = mycursor.fetchall()
    print("=====================")
    print("(id,nama,email,no hp)")
    for x in result: 
        print(x)

elif(guest == 2):

    nama = input("Nama : ")
    email = input("Email : ")
    nohp = input("No Hp : ")
    sql = "insert into user (nama,email,no_hp) values (%s, %s, %s)"
    val = (nama,email,nohp)
    mycursor.execute(sql, val)
    koneksi.commit()
    print(mycursor.rowcount, "Data Berhasil di tambahkan")

elif(guest == 3):
    id = input("ID User :")
    mycursor.execute("SELECT * FROM user WHERE id ="+ id)
    result = mycursor.fetchall()
    user = None
    for x in result:
        user = x
        if(user != None):
            nama = input("Nama : (" + user[1] +"): ") or user[1]
            email =  input("Email : (" + user[2] +"): ") or user[2]
            nohp =  input("No Hp : (" + user[3] +"): ") or user[3]
            sql = "UPDATE user SET nama=%s, email=%s, no_hp=%s WHERE id=%s"
            val = (nama,email,nohp,id)
            mycursor.execute(sql,val)
            koneksi.commit()
            print(mycursor.rowcount, "Data Berhasil Di Ubah")
        else:
            print("Data Tidak Ditemukan")
elif(guest == 4):
    id = input("ID User :")
    mycursor.execute("SELECT * FROM user WHERE id ="+ id)
    result = mycursor.fetchall()
    user = None
    for x in result:
        user = x
        if(user != None):
            print("Menghapus data:", user)
            sql = "DELETE FROM user WHERE id ="+ id
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount, "Data Berhasil Di Hapus")
        else:
            print("Data Tidak Ditemukan")
    
elif(guest == 5):
    lanjut = False