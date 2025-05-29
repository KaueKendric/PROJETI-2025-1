from django.shortcuts import render


def todo_list(request):
    nome = "Cleyson"
    alunos = ["Martelov2", "Pedro pacifico", "Lockless"]
    return render(request, "todos/todo_list.html", {"nome": nome, "alunos": alunos})
