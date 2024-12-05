from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Content
import json

@csrf_exempt  # Only for testing - remove in production and handle CSRF properly
def get_content(request, code):
    # This gets the specific content row matching the code from the URL
    content = get_object_or_404(Content, code=code)
    
    if request.method == 'GET':
        data = {
            'id': content.id,
            'code': content.code,  # Added code to response
            'image_url': content.image_url,
            'title': content.title,
            'description': content.description,
            'link': content.link,
            'prompt': content.prompt,
            'greeting': content.greeting,
            'rating': content.rating,
            'topic': content.topic,
            'studyNote': content.studyNote
        }
        return JsonResponse(data)
        
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Verify we're updating the correct content by checking code
            if 'code' in data and data['code'] != code:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Code mismatch'
                }, status=400)
            
            # Update fields if they're in the request
            if 'rating' in data:
                content.rating = data['rating']
            if 'topic' in data:
                content.topic = data['topic']
            if 'studyNote' in data:
                content.studyNote = data['studyNote']
                
            content.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Content updated successfully',
                'content': {
                    'code': content.code,
                    'rating': content.rating,
                    'topic': content.topic,
                    'studyNote': content.studyNote
                }
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)