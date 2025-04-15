from django.shortcuts import render, redirect
from .models import Aluno

# Create your views here.
def criar_aluno(request):
    if request.method == "GET":
        return render(request, 'alunos/criar_alunos.html')
    elif request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        
        aluno = Aluno(nome=nome, email=email)
        
        aluno.save()
        
        return redirect("criar_aluno")
        
