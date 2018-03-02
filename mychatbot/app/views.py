from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
import aiml
import os
from .forms import FormData
from mychatbot.constant.response_obj import *

@api_view(['GET'])
def hello(request):
    return render(request, 'chat.html', {'form': "form"})


@api_view(['POST'])
@parser_classes((JSONParser,))
def ask(request):
    form = FormData(request.POST)
    message = str(form.cleaned_data['messageText'])
    kernel = aiml.Kernel()
    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile="bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles=os.path.abspath("aiml/std-startup.xml"), commands="load aiml b")
        kernel.saveBrain("bot_brain.brn")
        # kernel now ready for use
    while True:
        if message == "quit":
            exit()
        elif message == "save":
            kernel.saveBrain("bot_brain.brn")
        else:
            bot_response = kernel.respond(message)
            print(bot_response)
            return_obj = ReturnObj.ret(200)
            return_obj['content']['answer'] = bot_response
            return Response(data=return_obj['content'], status=return_obj['status'])

