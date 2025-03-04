from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from school.models import School, Classroom
from school.form import SchoolForm, ClassroomForm
import json

@method_decorator(csrf_exempt, name="dispatch")
class SchoolViewSet(View):
    def get(self, request, *args, **kwargs):
        schools = School.objects.all()
        if not schools:
            return HttpResponse(json.dumps({"error": "No schools found"}), status=404)
        return HttpResponse(json.dumps(list(schools.values())), status=200)
    
    def post(self, request, *args, **kwargs):
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            form = SchoolForm(data)
        except json.JSONDecodeError:
            # If not JSON, try form data
            form = SchoolForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"message": "School created successfully"}), status=201)
        return HttpResponse(json.dumps({"error": form.errors}), status=400)
      
    def put(self,request,*args,**kwargs):
        try:
            school = School.objects.get(id=self.kwargs.get("pk"))
        except School.DoesNotExist:
            return HttpResponse(json.dumps({"error": "School not found"}), status=404)
        
        try:
            data = json.loads(request.body)
            form = SchoolForm(data, instance=school)
        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"error": "Invalid JSON data"}), status=400)
        
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"message": "School updated successfully"}), status=200)
        return HttpResponse(json.dumps({"error": form.errors}), status=400)
    
    def delete(self,request,*args,**kwargs):
        try:
            school=School.objects.get(id=self.kwargs.get("pk"))
        except School.DoesNotExist:
            return HttpResponse(json.dumps({"error":"School not found"}),status=404)
        school.delete()
        return HttpResponse(json.dumps({"message":"School deleted successfully"}),status=200)
    
    def patch(self, request, *args, **kwargs):
        try:
            school = School.objects.get(id=self.kwargs.get("pk"))
        except School.DoesNotExist:
            return HttpResponse(json.dumps({"error": "School not found"}), status=404)
        
        try:
            data = json.loads(request.body)
            # Only update fields that are provided in the request
            for field, value in data.items():
                if hasattr(school, field):
                    setattr(school, field, value)
            school.save()
            return HttpResponse(json.dumps({"message": "School updated successfully"}), status=200)
        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"error": "Invalid JSON data"}), status=400)
        except Exception as e:
            return HttpResponse(json.dumps({"error": str(e)}), status=400)


@method_decorator(csrf_exempt, name="dispatch")
class ClassroomViewSet(View):
    def get(self, request, *args, **kwargs):
        classrooms = Classroom.objects.all()
        if not classrooms:
            return HttpResponse(json.dumps({"error": "No classrooms found"}), status=404)
        return HttpResponse(json.dumps(list(classrooms.values())), status=200)
    
    def post(self, request, *args, **kwargs):
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            form = ClassroomForm(data)
        except json.JSONDecodeError:
            # If not JSON, try form data
            form = ClassroomForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"message": "Classroom created successfully"}), status=201)
        return HttpResponse(json.dumps({"error": form.errors}), status=400)
      
    def put(self, request, *args, **kwargs):
        try:
            classroom = Classroom.objects.get(id=self.kwargs.get("pk"))
        except Classroom.DoesNotExist:
            return HttpResponse(json.dumps({"error": "Classroom not found"}), status=404)
        
        try:
            data = json.loads(request.body)
            form = ClassroomForm(data, instance=classroom)
        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"error": "Invalid JSON data"}), status=400)
        
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"message": "Classroom updated successfully"}), status=200)
        return HttpResponse(json.dumps({"error": form.errors}), status=400)
    
    def delete(self, request, *args, **kwargs):
        try:
            classroom = Classroom.objects.get(id=self.kwargs.get("pk"))
        except Classroom.DoesNotExist:
            return HttpResponse(json.dumps({"error": "Classroom not found"}), status=404)
        classroom.delete()
        return HttpResponse(json.dumps({"message": "Classroom deleted successfully"}), status=200)
    
    def patch(self, request, *args, **kwargs):
        try:
            classroom = Classroom.objects.get(id=self.kwargs.get("pk"))
        except Classroom.DoesNotExist:
            return HttpResponse(json.dumps({"error": "Classroom not found"}), status=404)
        
        try:
            data = json.loads(request.body)
            # Only update fields that are provided in the request
            for field, value in data.items():
                if hasattr(classroom, field):
                    setattr(classroom, field, value)
            classroom.save()
            return HttpResponse(json.dumps({"message": "Classroom updated successfully"}), status=200)
        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"error": "Invalid JSON data"}), status=400)
        except Exception as e:
            return HttpResponse(json.dumps({"error": str(e)}), status=400)


