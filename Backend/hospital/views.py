import pymongo
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson import json_util

def obtenerSegDonacion(request):
    cliente = pymongo.MongoClient("mongodb://localhost:27017")
    db = cliente["hospital"]
    coleccion = db["seguimiento_donaciones"]

    resultados = list(coleccion.find())

    # Extraer solo los valores relevantes de cada documento
    arreglo_resultados = []
    for doc in resultados:
        arreglo_resultados.append({
            "paciente_ID": doc.get("paciente_ID"),
            "donador_ID": doc.get("donador_ID"),
            "solicitud_ID": doc.get("solicitud_ID"),
            "personal_medico_ID": doc.get("personal_medico_ID"),
            "fecha_seguimiento": doc.get("datos_post_trasplante", {}).get("fecha_seguimiento"),
            "sintomas": doc.get("datos_post_trasplante", {}).get("sintomas", []),
        })

    return JsonResponse(arreglo_resultados, safe=False)

@csrf_exempt 
def insertarSegDonacion(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
            
            cliente = pymongo.MongoClient("mongodb://localhost:27017")
            db = cliente["hospital"]
            coleccion = db["seguimiento_donaciones"]
            resultado = coleccion.insert_one(datos)
            
            return JsonResponse({"id_insertado": str(resultado.inserted_id)})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)