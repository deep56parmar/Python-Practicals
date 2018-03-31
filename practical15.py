import pyrebase

config = {
"apiKey": "AIzaSyC9YAW5chVp8QAmgfFd-MmO-x2z7Q1hyGM",
    "authDomain": "zfgzsdgas.firebaseapp.com",
    "databaseURL": "https://zfgzsdgas.firebaseio.com",
    "storageBucket": "zfgzsdgas.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

user = auth.sign_in_with_email_and_password("deep56parmar@hotmail.com","D.d.d.@56")
db = firebase.database()
Deep = {"Enrollment" : "140130107055", "Name" : "Deep Parmar" , "sem" : "8","Branch": "CE"}
Payal = {"Enrollment" : "140130107018", "Name" :"Payal Chaudhary" , "sem" : "8" ,"Branch" : "CE"}
Sneha = {"Enrollment" : "140130107008", "Name" :"Sneha Bhattasana" , "sem" : "8" ,"Branch" : "CE"}
db.child("Data").child("student1").set(Deep,user['idToken'])
db.child("Data").child("student2").set(Payal,user['idToken'])
db.child("Data").child("student3").set(Sneha,user['idToken'])
db.child("Data").child("student1").update({"Name": "Mortiest Morty"},user['idToken'])
db.child("Data").child("student3").remove()
