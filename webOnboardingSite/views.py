"""
Routes and views for the flask application.
"""
import re
import bcrypt
import os
import base64
import bson
import gridfs
import flask
#import session
from bson.binary import Binary
from datetime import datetime
from flask import render_template
from webOnboardingSite import app
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId

#from app import app

UPLOAD_FOLDER = 'C:\\Proyectos\\Proyectos\\doctos\\'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

#bcrypt = Bcrypt()
client = MongoClient("mongodb://localhost:27017")
database = client["onboarding"]
collection = database["pyme"]
fs = gridfs.GridFS(database)


#@app.route('/')
@app.route('/addPyme')
def home():
    """Renders the home page."""
    
    #flask.session.pop('file', None)

    query = {"folio": 1234569789}
    cursor = collection.find(query)
    ##print(cursor)
    
    if cursor:
        data = {}
        for doc in cursor:         
            #print(doc)
            session["folio_objectid"] = str(doc["_id"])
            session['regimenopt'] = str(doc["regimen"])
            data["folio"]			= doc["folio"]
            #data["regimen"] 		= doc["regimen"] 
            data["nombre"] 			= doc["nombre"] 
            data["apellido_paterno"]= doc["apellido_paterno"] 
            data["apellido_materno"]= doc["apellido_materno"] 
            data["correo"] 			= doc["correo"] 
            data["telefono"] 		= doc["telefono"] 
            data["nombre_empresa"] 	= doc["nombre_empresa"] 
            data["sector"]			= doc["sector"]
        session["data"] = data
            
    ##print(session["data"])
    return render_template(
        'addPyme.html',
        title='Onboarding',
        titulo="¡Comencemos! Indica bajo qué régimen opera tu empresa",
        tarea="Régimen",
        formAnte = "AddPyme",
        porcentaje ="01/05",
        year=datetime.now().year,
    )

#********************Inincio************************
@app.route('/',methods=['POST','GET'])
def generaFolio():
 #   form = request.form
 #   if request.method=='POST':
  #      if request.form.get('generaFolio'):
 #           otp=form.get('folio')
  #          session['otp']=otp
   #         print(otp)
  #          return render_template('getOTP.html',otp)
        return render_template('inicio.html')
            
    

#********************Inincio************************


<<<<<<< HEAD
=======
@app.route('/inicio', methods=["GET", "POST"])
def inicio():
    context={

    }
    return render_template('inicio.html', **context)

>>>>>>> 824f55b... Listo para el video
#********************Inincio************************
@app.route('/getOTP', methods=['GET','POST'])
def enviaSMS():
    context={

    }
    return render_template('getOTP.html', **context)
#********************Inincio************************

@app.route('/loadData', methods=["GET", "POST"])
def loadData():
    if request.method == 'POST':
        session['regimenopt'] = request.form.get('hdoptions') #request.form"flexRadioDefault")
        #print(session['regimenopt'] )

    dict = {}
    if(session["data"]):
        dict = session["data"]

    return render_template(       
        'loadData.html',
        title='Datos Generales',
        titulo="Datos generales de tu empresa",
        tarea="Datos generales",
        formAnte = "AddPyme",
        porcentaje ="02/05",
        avance = "40%",
        year=datetime.now().year,
        dict = dict
    )
#@app.route('/loadData')
#def loadData():   
#    return render_template(       
#        'loadData.html',
#        title='Datos Generales',
#        titulo="Datos generales de tu empresa",
#        tarea="Datos generales",
#        formAnte = "AddPyme",
#        porcentaje ="02/05",
#        year=datetime.now().year,
#        dict = None
#    )

#@app.route('/loadCard')
#def loadCard():   
#    return render_template(       
#        'loadCard.html',
#        title='Selecciona tipo de cuenta', 
#        titulo="Elige la cuenta que más se acomoda a tus necesidades",
#        tarea="Tipo de Cuenta",
#        formAnte = "loadData",
#        porcentaje ="03/05",
#        year=datetime.now().year,
#    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/loadCard', methods=["GET", "POST"])
def loadCard():
<<<<<<< HEAD
#@app.route("/save", methods=["GET", "POST"])
#def save():
    form = request.form
    message = ""
    dict = {} 
    message = {} 
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'    
    #print("load")
    if request.method == "POST":
        #print('post')
        #regimen = request.form.get("hdregimen")
        nombre = request.form.get("nombre")
        apellido_paterno = request.form.get("apellido_paterno")
        apellido_materno = request.form.get("apellido_materno")
        correo = request.form.get("correo")
        telefono = request.form.get("telefono")
        nombre_empresa = request.form.get("nombre_empresa")
        sector = request.form.get("sector")
        #contrasena = request.form.get("contrasena")
        #confcontrasena = request.form.get("confcontrasena")
        
        #print(session['regimenopt'] )
        ##print(confcontrasena)

        dict["regimen"] = session['regimenopt']
        dict["nombre"] = nombre
        dict["apellido_paterno"] = apellido_paterno
        dict["apellido_materno"] = apellido_materno
        dict["correo"] = correo
        dict["telefono"] = telefono
        dict["nombre_empresa"] = nombre_empresa
        dict["sector"] = sector
        #dict["contrasena"] = contrasena
        #dict["confcontrasena"] = confcontrasena


        if not nombre:
            message["nombre"] = "Ingresa tu Nombre"
        if not apellido_paterno:
            message["apellido_paterno"] = "Ingresa tu Apellido Paterno"
        if not apellido_materno:
            message["apellido_materno"] = "Ingresa tu Apellido Materno"
        if not correo:
            message["correo"] = "Ingresa tu Correo"
        elif(not re.fullmatch(regex, correo)):
            message["correo"] = "Correo invalido"
        if not nombre_empresa:
            message["nombre_empresa"] = "Ingresa el Nombre de la Empresa"
        if not telefono:
            message["telefono"] = "Ingresa tu número de Telefono"        
        if sector == '0':
            message["sector"] = "Selecciona una opción"
        #if not contrasena:
        #    message["contrasena"] = "Ingresa tu contraseña"
        #elif len(contrasena)<8:
        #    message["contrasena"] ="Usa 8 caracteres o más para tu contraseña"            
        #if not confcontrasena:
        #    message["confcontrasena"] = "Confirma tu contraseña"   
        #if(contrasena and confcontrasena and  contrasena != confcontrasena):
        #    message["confcontrasena"] = "Las contraseñas no coinciden. Vuelve a intentarlo"

        if len(message.keys()) == 0:
            #del dict['contrasena']
            #del dict['confcontrasena']
            #password = bcrypt.hashpw(contrasena.encode('utf8'), bcrypt.gensalt(10))
            #dict["password"] = password

            if(session["folio_objectid"]):
                #print("actualiza")
                #print(dict["sector"])
                mongo_id = bson.ObjectId(session["folio_objectid"]) 
                #print(mongo_id)
                collection.update_one({"_id": mongo_id}, 
                                 {"$set": 
                                      {    
                                           "regimen": session['regimenopt'],
                                            "nombre": dict["nombre"],
                                            "apellido_paterno": dict["apellido_paterno"],
                                            "apellido_materno": dict["apellido_materno"],
                                            "correo": dict["correo"],
                                            "telefono": dict["telefono"],
                                            "nombre_empresa": dict["nombre_empresa"],
                                            "sector": dict["sector"]
                                      }
                                  })
            else:
                objectid = collection.insert(dict)
            #session['objectid'] =  str(objectid)
            ##print(session['objectid'])
             

            if request.form.get("continuar"):
                 return render_template(       
                        'loadCard.html',
                        title='Selecciona tipo de cuenta', 
                        titulo="Elige la cuenta que más se acomoda a tus necesidades",
                        tarea="Tipo de Cuenta",
                        formAnte = "loadData",
                        porcentaje ="03/05",
                        avance = "60%",
                        year=datetime.now().year,
                    )
            elif request.form.get("guardar"):
                mensaje="Datos almacenados satisfactoriamente"
                return render_template('loadData.html', message = None, dict = None, year=datetime.now().year, mensaje=mensaje,
                                       titulo="Datos generales de tu empresa",tarea="Datos generales",formAnte = "AddPyme",porcentaje ="02/05")
        else:            
            return render_template('loadData.html', form=form, message = message, dict = dict, year=datetime.now().year,
                                   titulo="Datos generales de tu empresa",tarea="Datos generales",formAnte = "AddPyme",porcentaje ="02/05",)
=======
    context={

    }
    return render_template('loadCard.html', **context)
>>>>>>> 824f55b... Listo para el video

@app.route('/loadDocument', methods=["GET", "POST"])
def loadDocument():

    cuenta = ""
    if request.form.get("cuentacorrienteempresa"):
        cuenta = "Cuenta Corriente Empresas"
    elif request.form.get("cuentaCorrienteremunerada"):
        cuenta = "Cuenta Corriente Remunerada"
    elif request.form.get("cuentaCorrientetradicional"):
        cuenta = "Cuenta Corriente Tradicional"
    elif request.form.get("cuentaahorroempresarial"):
        cuenta = "Cuenta de Ahorro Empresarial"
    elif request.form.get("cuentaahorrofijo"):
        cuenta = "Cuenta de Ahorro Fijo"
    elif request.form.get("cuentaahorrodiario"):
        cuenta = "Cuenta Ahorradiario"

    session["cuenta"] = cuenta

    doctoidentidadvis = "hidden"
    loadFiles()

    return render_template(
        'loadDocument.html',
        title='About',
        titulo="Has seleccionado " + cuenta + ". Por favor sube los siguientes documentos",
        tarea="Documentos Oficiales",
        formAnte = "loadCard",
        porcentaje ="04/05",
        avance= "80%",
        year=datetime.now().year,
        file = session["file"],
        doctoidentidadvis=doctoidentidadvis)
    
    #if session.get('file') == True:
    #    print("variable de sesion")
    #    print(session["file"])
    #    return render_template(
    #    'loadDocument.html',
    #    title='About',
    #    titulo="Has seleccionado " + cuenta + ". Por favor sube los siguientes documentos",
    #    tarea="Documentos Oficiales",
    #    formAnte = "loadCard",
    #    porcentaje ="04/05",
    #    avance= "80%",
    #    year=datetime.now().year,
    #    file = session["file"],
    #    doctoidentidadvis=doctoidentidadvis
    #)
    #else:
    #    return render_template(
    #    'loadDocument.html',
    #    title='About',
    #    titulo="Has seleccionado " + cuenta + ". Por favor sube los siguientes documentos",
    #    tarea="Documentos Oficiales",
    #    formAnte = "loadCard",
    #    porcentaje ="04/05",
    #    avance= "80%",
    #    year=datetime.now().year,
    #    file = None,
    #    doctoidentidadvis=doctoidentidadvis)



    #print("datos a cargar en load document cuando file existe")
    #print(session.get('file'))
    #print(archivo)
    #return render_template(
    #    'loadDocument.html',
    #    title='About',
    #    titulo="Has seleccionado " + cuenta + ". Por favor sube los siguientes documentos",
    #    tarea="Documentos Oficiales",
    #    formAnte = "loadCard",
    #    porcentaje ="04/05",
    #    avance= "80%",
    #    year=datetime.now().year,
    #    file = archivo,
    #    doctoidentidadvis=doctoidentidadvis
    #)

def loadFiles():
    file = {}
    
    query = {"file" : {"$exists": "True"}, "folio" : 1234569789 }
    result = collection.find_one(query) #{"$and":[ {"file":{"$exists": True}}, {"folio":{"$eq": "1234569789"}}]})
    #collection.find(query)

    print("result")
    print(result)

    if result:
        query = {"folio": 1234569789}
        cursor = collection.find(query)
        print("cursor")
        print(cursor)
    
        if cursor:        
            for doc in cursor:         
                ##print(doc["file"]["name"])
                #file = doc["file"] 
                #if doc["file"] != None:
                #if "file" in doc:
                print(doc["file"]["tipo_docto"])
                if doc["file"]["tipo_docto"] == "Documento de Identidad":
                    file["doctoidentidadname"] = doc["file"]["name"]
                    file["doctoidentidadid"] = str(doc["file"]["_id"])
                    doctoidentidadvis = "visible"
                    session["file"] = file
        else:
            file = None
    else:
        session["file"] = None
        #print(file)


#@app.route('/saveRegimen', methods=["GET", "POST"])
#def saveRegimen():
#    if request.method == 'POST':
#        session['regimenopt'] = request.form.get('hdoptions') #request.form"flexRadioDefault")
#        #print(session['regimenopt'] )
        
#    return render_template(       
#        'loadData.html',
#        title='Datos Generales',
#        titulo="Datos generales de tu empresa",
#        tarea="Datos generales",
#        formAnte = "AddPyme",
#        porcentaje ="02/05",
#        year=datetime.now().year,
#        dict = None
#    )







@app.route("/saveDocto", methods=["GET", "POST"])
<<<<<<< HEAD
def saveDocto():
    if request.method == 'POST':
        print("post")
        mensajeerror=""
        if request.form.get("download"):
            #print("download")
            return download()
        #elif request.form.get("remove"):
        #    #print("delete")
        #    return delete()
        
        elif request.form.get("deletedoctoidentidad"):
            if(session["file"]):
                file = session["file"]
                file_id = file['doctoidentidadid'] if 'doctoidentidadid' in file else ""
                print("id para eliminar: " + file_id)
                delete(session["folio_objectid"], file_id)

        elif request.form.get("uploaddoctoidentidad"):
            file = request.files['file'] 
            print(file)
            if file.filename == '':
                print(file.filename)
                mensajeerror="Seleccione un archivo"
                doctoidentidadvis ="hidden",
                #return render_template(
                #    'loadDocument.html',
                #    title='loadDocument',
                #    titulo="Has seleccionado " + session["cuenta"] + ". Por favor sube los siguientes documentos",
                #    tarea="Documentos Oficiales",
                #    formAnte = "loadCard",
                #    porcentaje ="04/05",
                #    avance= "80%",
                #    year=datetime.now().year,
                #    mensajeerror='Seleccione un archivo',
                #    visible="hidden",
                #    file = session["file"]
                #)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #os.rename(filename, 'niloofar.jpg')
                #with open("", "rb") as f:
                #encoded = Binary(f.read())
                print(filename)
                fileID = fs.put( open( os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb')  )
                out = fs.get(fileID)

                if request.form.get("uploaddoctoidentidad"):
                    tipo_docto = "Documento de Identidad"
                
                    #print("tipo_docto:"+tipo_docto)
                
                print(session["folio_objectid"])
                if(session["folio_objectid"]):
                    ##print("actualiza")
                    ##print(dict["sector"])
                    mongo_id = bson.ObjectId(session["folio_objectid"]) 
                    #print(mongo_id)
                    countrows = collection.update_one({"_id": mongo_id, "file.tipo_docto": tipo_docto}, 
                                     {"$set": 
                                          {    
                                               "file": {"_id" : bson.ObjectId(fileID), "name": filename, "tipo_docto": tipo_docto}

                                          }
                                      })
                    if countrows.matched_count == 0:
                         collection.update_one({"_id": mongo_id}, 
                                     {"$set": 
                                          {    
                                               "file": {"_id" : bson.ObjectId(fileID), "name": filename, "tipo_docto": tipo_docto}

                                          }
                                      })


                    mensajeerror=None
                    doctoidentidadvis="visible"


                #return render_template(
                #    'loadDocument.html',
                #    title='loadDocument',
                #    titulo="Has seleccionado " + session["cuenta"] + ". Por favor sube los siguientes documentos",
                #    tarea="Documentos Oficiales",
                #    formAnte = "loadCard",
                #    porcentaje ="04/05",
                #    avance= "80%",
                #    year=datetime.now().year,
                #    mensajeerror=None,
                #    visible="visible",
                #    file = session["file"]
                #)

    #file = {}
    loadFiles()     
    #if session.get('file') == True:
    #    file = session["file"]

    return render_template(
                    'loadDocument.html',
                    title='loadDocument',
                    titulo="Has seleccionado " + session["cuenta"] + ". Por favor sube los siguientes documentos",
                    tarea="Documentos Oficiales",
                    formAnte = "loadCard",
                    porcentaje ="04/05",
                    avance= "80%",
                    year=datetime.now().year,
                    mensajeerror=mensajeerror,
                    file = session["file"] 
                )
                #db.actgrupalopenDataLocalesMadrid.update({_id: doc._id},{$set:{"revision":  {  _id: ObjectId(), prox_inspeccion: 10, puntuacion: 80, comentario: "separar las mesas"}}});

                #encoded = Binary(out)
                #collection.insert({"filename": filename, "file": out, "description": "test" })
                #return render_template('loadCard.html', year=datetime.now().year)
    

    #if request.method == 'POST':        
    #    file = request.form.get("fileLoad")
    #    #print(file)
    #    if file and allowed_file(file.filename):
    #        filename = secure_filename(file.filename)
    #        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #        os.rename(UPLOAD_FOLDER + filename, 'niloofar.jpg')
    #return  render_template('loadCard.html', year=datetime.now().year)

=======


def saveDocto():
    context={

    }
    return render_template('spinner.html', **context)
 
>>>>>>> 824f55b... Listo para el video
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




#def delete():
#    fileId = ObjectId("6171bbed152b45b44fad4caa")
#    fs.delete(fileId); #delete(ObjectId(id));
#    return "delete"



def delete(_id, file_id):
    print("file_id: "+ file_id)
    collection.update_one({"_id": bson.ObjectId(_id)}, 
                           {
                               #"$push": {"file._id": bson.ObjectId(file_id)}
                               "$unset": {"file": { "_id": bson.ObjectId(file_id) }}
                                
                            })
    fs.delete(bson.ObjectId(file_id) ); 
    return "delete"




def download():
    id = "6172d9705e66ba9bc108b50e"
    grid_fs_file =  fs.get(ObjectId(id)) #fs.find_one({'filename': file_name})
    response = flask.Response(grid_fs_file.read())
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers["Content-Disposition"] = "attachment; filename={}".format("Paola.docx")
    return response


    
    #response = flask.Response(grid_fs_file.__iter__())
    #response.headers['Content-Type'] = 'application/octet-stream'
    #response.headers["Content-Disposition"] = "attachment; filename={}".format("C:\Proyectos\Proyectos\doctos\Paola.jpg")
    #return grid_fs_file




    #response = make_response(grid_fs_file.read())
    #response.headers['Content-Type'] = 'application/octet-stream'
    #response.headers["Content-Disposition"] = "attachment; filename={}".format("namefile")
    #return response


    ####file = fs.get(ObjectId(id)) #GridFS(getDBConnection().upload).get(ObjectId(id))
    #####print("file by objectID")
    #####print(file)
    #####response =  flask.Response(file)
    #####response['Content-Disposition'] = 'attachment; filename=%s' % str("Paola")
    #####response['Content-Length']      = file.length 
    ####response = flask.Response(file.__iter__())
    #####print(response)
    #####print("response")
    #####print(file.metadata)
    #####response.headers['content-type'] = file.metadata['content_type']
    #####print("content_type")
    ####response.content_length = file.length

    ####return response

def downloadDocument():
    if request.method == 'POST':
        #fsg = MotorGridFSBucket(database)
        file_id = "6171bbed152b45b44fad4caa"
        #file = open('C:\Proyectos\Proyectos\doctos\myfile.jpg','wb+')
        #fsg.download_to_stream(file_id, file)
        #file.seek(0)
        #contents = file.read()
       
    #downloadStream = gridFSBucket.openDownloadStream(fileId)
    #fileLength = downloadStream.getGridFSFile().getLength();
    #fs = GridFSBucket(database)
    # Get file to write to
    #if not os.path.exists('my_directory'):
    #    os.makedirs('my_directory')

    #file = open('C:\Proyectos\Proyectos\doctos','wb')
    #fs.download_to_stream_by_id("test_file", file)

#    ObjectId fileId = new ObjectId("60345d38ebfcf47030e81cc9");
#try (GridFSDownloadStream downloadStream = gridFSBucket.openDownloadStream(fileId)) {
#    int fileLength = (int) downloadStream.getGridFSFile().getLength();
#    byte[] bytesToWriteTo = new byte[fileLength];
#    downloadStream.read(bytesToWriteTo);
#    System.out.#println(new String(bytesToWriteTo, StandardCharsets.UTF_8));
#}
@app.route("/validateOTP")
def validateOTP():
    """Renders the validateOTP page."""
    return render_template(
            'validateOTP.html',
            title='Código',
            year=datetime.now().year,
            message='Security code validation'
        )

@app.route("/folio")
def folio():
    """Renders the folio page."""
    return render_template(
            'folio.html',
            title='Folio',
            year=datetime.now().year,
            message='Folio de sesion'
        )  

<<<<<<< HEAD
@app.route("/account")
def account():
    """Renders the account page."""
    return render_template(
            'account.html',
            title='account',
            year=datetime.now().year,
            message='account de sesion'
        )  

@app.route("/accountC")
def accountC():
    """Renders the accountC page."""
    return render_template(
            'accountC.html',
            title='accountC',
            year=datetime.now().year,
            message='accountC de sesion'
        )     
=======
@app.route("/account", methods=['GET','POST'])
def account():
    context={

    }
    return render_template('spinner.html', **context)

>>>>>>> 824f55b... Listo para el video

@app.route("/spinner")
def spinner():
    """Renders the spinner page."""
    return render_template(
            'spinner.html',
            title='spinner',
            year=datetime.now().year,
            message='spinner de sesion'
        ) 

@app.route("/final")
<<<<<<< HEAD
def final():
    """Renders the final page."""
    return render_template(
            'final.html',
            title='final',
            year=datetime.now().year,
            message='final de sesion'
        )
=======

def final():
    context={

    }
    return render_template('final.html', **context)
>>>>>>> 824f55b... Listo para el video
