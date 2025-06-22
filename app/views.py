from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse,HttpResponse
from .models import *
from django.db.models.functions import Length

def home(request):
    return HttpResponse("this is image")

@api_view(['POST'])
def upload_image(request):
    image_url = request.data.get('image_url')
    print("1")
    if image_url:
        print("yes")
        print("Received image URL:", image_url)
        # Save to DB if needed
        return Response({"message": "Image URL received"}, status=status.HTTP_201_CREATED)
    return Response({"error": "No image URL provided"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def applicants(request):
    try:
        data = json.loads(request.body)
        # print(data)
        applicant = Applied_users.objects.create(
            full_name=data.get("fullName"),
            email=data.get("email"),
            phone_number=data.get("phone"),
            education=data.get("education"),
            program_experience=data.get("programmingExperience"),
            need_to_join=data.get("motivation"),
            carrier_goals=data.get("goals"),
            referral_code=data.get("referralCode"),
            payment_screenshot=data.get("transactionId")
        )
        # print("saved")
        return JsonResponse({"message": "saved"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        # print(e)
        return JsonResponse({"message": "error"}, status=status.HTTP_201_CREATED)
    
@api_view(["GET"])
def get_applicants(request):
    applicants = Applied_users.objects.all().order_by("-created_at")
    refer_count = Applied_users.objects.annotate(
        ref_length=Length('referral_code')
    ).filter(ref_length=12).count()
    
    response_data = [
        {
            "name": applicant.full_name,
            "code": applicant.create_refer,
            "refered_count": refer_count
        }
        for applicant in applicants
    ]

    return Response(response_data)

@api_view(["POST"])
def save_message(request):
    try:
        data = json.loads(request.body)
        message = ContactForm.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            subject=data.get("subject"),
            message=data.get("message"),
        )
        return JsonResponse({"message": "saved"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"message": "error"}, status=status.HTTP_201_CREATED)