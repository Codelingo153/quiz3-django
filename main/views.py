from django.shortcuts import render

def student_list(request):
    students = [
        {
            "StudentID": "024A-12627",
            "Name": "Joshua A. Antioquia",
            "Age": 19,
            "Course": "BSIT",
            "Section": "3C",
            "Email": "Antioquia@gmail.com",
            "Phone_Number": "0917-123-4567"
        },
        {
            "StudentID": "024A-12628",
            "Name": "Justin Rodriguez",
            "Age": 20,
            "Course": "BSIT",
            "Section": "3C",
            "Email": "Rodriguez@gmail.com",
            "Phone_Number": "0918-123-4567"
        },
        {
            "StudentID": "024A-12629",
            "Name": "Lord Raphael Lorena",
            "Age": 21,
            "Course": "BSIT",
            "Section": "3C",
            "Email": "Lorena@gmail.com",
            "Phone_Number": "0919-123-4567"
        }
    ]

    context = {
        "students": students,
        "student_count": len(students)
    }

    return render(request, "main/home.html", context)

def home(request):
    return student_list(request)
