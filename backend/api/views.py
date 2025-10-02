import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Load dinosaur data
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'api', 'data.json')

def load_dinosaur_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

@api_view(['GET'])
def get_all_dinosaurs(request):
    """Get all dinosaurs"""
    try:
        data = load_dinosaur_data()
        return Response(data)
    except Exception as e:
        return Response({'error': 'Failed to load dinosaur data'}, status=500)

@api_view(['GET'])
def get_dinosaur_by_name(request, dinosaur_name):
    """Get a specific dinosaur by name"""
    try:
        data = load_dinosaur_data()
        
        # Find dinosaur by name (case-insensitive)
        dinosaur = None
        for item in data:
            if item['name'].lower() == dinosaur_name.lower():
                dinosaur = item
                break
        
        if dinosaur:
            return Response(dinosaur)
        else:
            return Response("No dinosaur found.")
    except Exception as e:
        return Response({'error': 'Failed to load dinosaur data'}, status=500)
