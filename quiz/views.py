from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Answer
from django.http import HttpResponse



def index(request):
    return HttpResponse("Welcome to the quiz app!")
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    if request.method == 'POST':
        score = 0
        for question in quiz.questions.all():
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1
        return HttpResponse(f'Your score: {score} / {quiz.questions.count()}')

    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})
