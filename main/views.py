# main/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Article
from django.views import View
# from transformers import pipeline
# from elasticsearch import Elasticsearch

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

# class ChatbotView(View):
#     def get(self, request):
#         return render(request, 'chatbot.html')
    
#     def post(self, request):
#         question = request.POST.get('question')
#         generator = pipeline("text-generation")
#         response = generator(question, max_length=50, num_return_sequences=1)
#         answer = response[0]['generated_text']
#         return render(request, 'chatbot.html', {'question': question, 'answer': answer})

# es = Elasticsearch()

# class RagView(View):
#     def get(self, request):
#         query = request.GET.get('query')
#         results = es.search(index='articles', body={'query': {'match': {'content': query}}})
#         return render(request, 'rag_results.html', {'query': query, 'results': results})
