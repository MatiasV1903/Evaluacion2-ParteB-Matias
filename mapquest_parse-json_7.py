import urllib.parse
import requests

api_mapquest_url = "https://www.mapquestapi.com/directions/v2/route?"
llave = "dNcG80ESAOw61x3e75ZcPwwOB6K7zie1"

while True:
   ubicación_inicial = input("Ciudad de origen: ")
   if ubicación_inicial == "salir" or ubicación_inicial == "s":
        break
   ubicación_destino = input("Ciudad de destino: ")
   if ubicación_destino == "salir" or ubicación_destino == "s":
        break
    
   url = api_mapquest_url + urllib.parse.urlencode({"key" :llave, "from" :ubicación_inicial, "to" :ubicación_destino, "locale": "es_MX"})

   información = requests.get(url).json()

   print("URL:" + (url))

   situación = información ["info"] ["statuscode"]

   if situación == 0:
       print("API en estado listo: " + str(situación) + " = Llamada exitosa de la ruta.\n")
       print("=============================================")
       print("Ubicación principal: " + (ubicación_inicial))
       print("Ubicación de destino: " + (ubicación_destino))
       print("Tiempo estimado:  " + (información["route"]["formattedTime"]))
       print("Kilometros:       " + str("{:.2f}".format((información["route"]["distance"])*1.61)))
       print("=============================================")
       for each in información["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
       print("=============================================\n")
       