import json
from django.http import JsonResponse
from .models import Student

def student_api(request):

    if request.method == "GET":
        students = Student.objects.all()

        data = []

        for s in students:
            data.append({
                "id": s.id,
                "name": s.name,
                "age": s.age,
                "email": s.email})

        return JsonResponse(data, safe=False)


    if request.method == "POST":
        body = json.loads(request.body)

        student = Student.objects.create(
            name=body.get("name"),
            age=body.get("age"),
            email=body.get("email"))

        return JsonResponse({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email})