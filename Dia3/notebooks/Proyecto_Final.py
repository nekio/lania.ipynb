
# coding: utf-8

# In[ ]:

## Fecha Entrega: 27/11/2014
## Proyecto:      Localizador de ubicación (Hablado)
## Colabordadores:
##                Juana Valdez Jimenez
##                Giovany Emilio Marin Garcia
##                Sinesio Ivan Carrillo Heredia


# In[2]:

import android


# In[3]:

droide = android.Android()


# In[4]:

import time


# In[25]:

droide.dialogCreateAlert("¿Desea obtener su ubicación")
droide.dialogSetPositiveButtonText("Si")
droide.dialogSetNegativeButtonText("No")

droide.dialogShow()

acum = 0
response=droide.dialogGetResponse().result
droide.dialogDismiss()

if response.has_key("which"):
  result=response["which"]
    
  if result=="positive":
    droide.ttsSpeak("Obteniendo ubicación. Espere unos segundos por favor")
    droide.startLocating()                
    time.sleep(15)
    loc = droide.readLocation().result

    if loc == {}:
      loc = getLastKnownLocation().result
    if loc != {}:
      try:
        n = loc['gps']
      except KeyError:
        n = loc['network'] 
        
      la = n['latitude'] 
      lo = n['longitude']
      address = droide.geocode(la, lo).result
        
    droide.stopLocating()   
    
    noEncontrado = "Dato no encontrado"
    
    try:
        droide.ttsSpeak("Direccion")
        direccion=address[0]["thoroughfare"]
        droide.ttsSpeak(direccion)
    except BaseException as e:
        droide.ttsSpeak(noEncontrado)
        acum += 1
        print(e)
        
    try:
        droide.ttsSpeak("Localidad")
        droide.ttsSpeak(address[0]["locality"])
    except BaseException as e:
        droide.ttsSpeak(noEncontrado)
        acum += 1
        print(e)
    
    try:
        droide.ttsSpeak("Area")
        droide.ttsSpeak(address[0]["admin_area"])
    except BaseException as e:
        droide.ttsSpeak(noEncontrado)
        acum += 1
        print(e)
    
    try:
        droide.ttsSpeak("País")
        droide.ttsSpeak(address[0]["country_name"])
    except BaseException as e:
        droide.ttsSpeak(noEncontrado)
        acum += 1
        print(e)
    
    try:
        droide.ttsSpeak("Busqueda finalizada")
    except BaseException as e:
        print(e)
        
    if acum == 4:
        droide.ttsSpeak("No se pudo obtener la ubicacion. Le sugerimos tener activado el guai fai e intentarlo de nuevo.")
    
  elif result=="negative":
    droide.ttsSpeak("Finalizando aplicación")
elif response.has_key("canceled"):
  print "Busqueda cancelada"
else:
  print "Unknown response = ",response
 
print "Done"

