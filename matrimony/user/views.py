from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import PartnerPreferenceDetails,UserModel,SixPhoto,IdProof,DocumentAddress,CompatibilityMatch,ReviewSection,ProfileCompletes,Habits,Hobbies
from .serializer import PartnerPreferenceDetailsSerializer,UserModelSerializer,SixPhotoSerializer,IdProofSerializer,DocumentAddressSerializer,CompatibilityMatchSerializer,ReviewSectionSerializer,ProfileCompletesSerializer,HabitsSerializer,HobbiesSerializer
 
# Create your views here.
 
 
class PartnerPreferenceDetailsAPIView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            partner_preference = get_object_or_404(PartnerPreferenceDetails, pk=pk)
            serializer = PartnerPreferenceDetailsSerializer(partner_preference)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            partner_preferences = PartnerPreferenceDetails.objects.all()
            serializer = PartnerPreferenceDetailsSerializer(partner_preferences, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        serializer = PartnerPreferenceDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self, request, pk):
        partner_preference = get_object_or_404(PartnerPreferenceDetails, pk=pk)
        serializer = PartnerPreferenceDetailsSerializer(partner_preference, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        partner_preference = get_object_or_404(PartnerPreferenceDetails, pk=pk)
        serializer = PartnerPreferenceDetailsSerializer(partner_preference, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        partner_preference = get_object_or_404(PartnerPreferenceDetails, pk=pk)
        partner_preference.delete()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 
 
 
class UserModelAPIView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            user_model = get_object_or_404(UserModel, pk=pk)
            serializer = UserModelSerializer(user_model)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            user_models = UserModel.objects.all()
            serializer = UserModelSerializer(user_models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self, request, pk):
        user_model = get_object_or_404(UserModel, pk=pk)
        serializer = UserModelSerializer(user_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        user_model = get_object_or_404(UserModel, pk=pk)
        serializer = UserModelSerializer(user_model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        user_model = get_object_or_404(UserModel, pk=pk)
        user_model.delete()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
   
 
 
class SixPhotoAPIView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            six_photo = get_object_or_404(SixPhoto, pk=pk)
            serializer = SixPhotoSerializer(six_photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            six_photos = SixPhoto.objects.all()
            serializer = SixPhotoSerializer(six_photos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        serializer = SixPhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self, request, pk):
        six_photo = get_object_or_404(SixPhoto, pk=pk)
        serializer = SixPhotoSerializer(six_photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        six_photo = get_object_or_404(SixPhoto, pk=pk)
        serializer = SixPhotoSerializer(six_photo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        six_photo = get_object_or_404(SixPhoto, pk=pk)
        six_photo.delete()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
   
 
class IdProofAPIView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            id_proof = get_object_or_404(IdProof, pk=pk)
            serializer = IdProofSerializer(id_proof)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            id_proofs = IdProof.objects.all()
            serializer = IdProofSerializer(id_proofs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        serializer = IdProofSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self, request, pk):
        id_proof = get_object_or_404(IdProof, pk=pk)
        serializer = IdProofSerializer(id_proof, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        id_proof = get_object_or_404(IdProof, pk=pk)
        serializer = IdProofSerializer(id_proof, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        id_proof = get_object_or_404(IdProof, pk=pk)
        id_proof.delete()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
   
 
class DocumentAddressAPIView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            document_address = get_object_or_404(DocumentAddress, pk=pk)
            serializer = DocumentAddressSerializer(document_address)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            document_addresses = DocumentAddress.objects.all()
            serializer = DocumentAddressSerializer(document_addresses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        serializer = DocumentAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self, request, pk):
        document_address = get_object_or_404(DocumentAddress, pk=pk)
        serializer = DocumentAddressSerializer(document_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        document_address = get_object_or_404(DocumentAddress, pk=pk)
        serializer = DocumentAddressSerializer(document_address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        document_address = get_object_or_404(DocumentAddress, pk=pk)
        document_address.delete()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 
 
class CompatibilityMatchAPIView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            compatibility_match = get_object_or_404(CompatibilityMatch, pk=pk)
            serializer = CompatibilityMatchSerializer(compatibility_match)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            compatibility_matches = CompatibilityMatch.objects.all()
            serializer = CompatibilityMatchSerializer(compatibility_matches, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        serializer = CompatibilityMatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self, request, pk):
        compatibility_match = get_object_or_404(CompatibilityMatch, pk=pk)
        serializer = CompatibilityMatchSerializer(compatibility_match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        compatibility_match = get_object_or_404(CompatibilityMatch, pk=pk)
        serializer = CompatibilityMatchSerializer(compatibility_match, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        compatibility_match = get_object_or_404(CompatibilityMatch, pk=pk)
        compatibility_match.delete()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
   
 
 
class ReviewSectionAPIView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            review = get_object_or_404(ReviewSection, pk=pk)
            serializer = ReviewSectionSerializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            reviews = ReviewSection.objects.all()
            serializer = ReviewSectionSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        serializer = ReviewSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self, request, pk):
        review = get_object_or_404(ReviewSection, pk=pk)
        serializer = ReviewSectionSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        review = get_object_or_404(ReviewSection, pk=pk)
        serializer = ReviewSectionSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        review = get_object_or_404(ReviewSection, pk=pk)
        review.delete()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
   
 
class ProfileCompletesAPIView(APIView):
    def get(self, request, pk=None, format=None):
        # Fetch user profile based on the primary key (pk)
        try:
            user_profile = ProfileCompletes.objects.get(pk=pk)
        except ProfileCompletes.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)
        
        # Initialize the completion percentage
        completion_percentage = 0

        # Increment the completion percentage based on profile details
        if user_profile.profile_photo:
            completion_percentage += 10
        if user_profile.basic_details_completed:
            completion_percentage += 20
        if user_profile.education_details_completed:
            completion_percentage += 10
        if user_profile.horoscope_details_completed:
            completion_percentage += 10
        if user_profile.family_details_completed:
            completion_percentage += 10
        if user_profile.partner_preference_details_completed:
            completion_percentage += 10
        if user_profile.habits_details_completed:
            completion_percentage += 10
        if user_profile.hobbies_details_completed:
            completion_percentage += 10
        if user_profile.interest_details_completed:
            completion_percentage += 10

        # Return the completion percentage
        if completion_percentage > 0:
            return Response({"message": f"The profile update percentage is {completion_percentage}%"}, status=200)
        else:
            return Response({"message": "Please update your profile"}, status=200)
    
 
    def post(self, request):
        serializer = ProfileCompletesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    
    def patch(self, request, pk):
        profile = get_object_or_404(ProfileCompletes, pk=pk)
        serializer = ProfileCompletesSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    
   
 
class HabitsView(APIView):
 
    def get(Self,request,pk=None):
        if pk:
            basic_info=Habits.objects.get(pk=pk)
            serializer=HabitsSerializer(basic_info)
            return Response(serializer.data)
       
        else:
            basic_info=Habits.objects.all()
            serializer=HabitsSerializer(basic_info,many=True)
            return Response(serializer.data)
 
 
    def post(self,request):
        serializer=HabitsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def put(self,request,pk):
        basic_info=Habits.objects.get(pk=pk)
        serializer=HabitsSerializer(basic_info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def patch(self,request,pk):
        basic_info=Habits.objects.get(pk=pk)
        serializer=HabitsSerializer(basic_info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def delete(self,request,pk):
        basic_info=Habits.objects.get(pk=pk)
        basic_info.delete()
        return Response({"message":"Record Deleted....!!"})
 
 
class HobbiesView(APIView):
 
    def get(Self,request,pk=None):
        if pk:
            basic_info=Hobbies.objects.get(pk=pk)
            serializer=HobbiesSerializer(basic_info)
            return Response(serializer.data)
       
        else:
            basic_info=Hobbies.objects.all()
            serializer=HobbiesSerializer(basic_info,many=True)
            return Response(serializer.data)
 
 
    def post(self,request):
        serializer=HobbiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def put(self,request,pk):
        basic_info=Hobbies.objects.get(pk=pk)
        serializer=HobbiesSerializer(basic_info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def patch(self,request,pk):
        basic_info=Hobbies.objects.get(pk=pk)
        serializer=HobbiesSerializer(basic_info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    def delete(self,request,pk):
        basic_info=Hobbies.objects.get(pk=pk)
        basic_info.delete()
        return Response({"message":"Record Deleted....!!"})
 
 