from flask import Flask, escape, request

app = Flask(__name__)

DB = {
    "students": [],
    "classes": []
}

sid = 10000

cid = 100

#Hello, Brian Hsu!

@app.route('/')

def hello():
    
    name = request.args.get("name","Brian Hsu")
    
    return f'Hello, {escape(name)}!'


#create student

@app.route('/students',methods=['POST'])

def create_students():
   
   global sid
   
   name = request.json["name"]
   
   DB["students"].append({"id":sid,"name":name})
   
   sid = sid + 1
   
   return DB


#retrieve student

@app.route('/students/<s_id>',methods=['GET'])

def retrieve_students(s_id):
 
 for student in DB["students"]:
  
  if (int(s_id) ==  student["id"]):
   
   return student


#create class

@app.route('/classes',methods=['POST'])

def create_classes():
   
   global cid
   
   name = request.json["name"]
   
   DB["classes"].append({"id":cid,"name":name,"students":[]})
   
   cid = cid + 1
   
   return DB


#retrieve class

@app.route('/classes/<c_id>',methods=['GET'])

def retrieve_classes(c_id):
 
 for clas in DB["classes"]:
  
  if (int(c_id) ==  clas["id"]):
   
   return clas


#add student to class

@app.route('/classes/<c_id>',methods=['PATCH'])

def add_student_to_classes(c_id):

 sid = request.json["id"]

 for clas in DB["classes"]:
      
  if (int(c_id) ==  clas["id"]):

   for student in DB["students"]:
      
    if (int(sid) ==  student["id"]):

     clas["students"].append(student)
 
     return clas





      




  
 


 
  











