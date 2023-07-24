from django.shortcuts import render
from django.middleware import csrf
from django.http import JsonResponse
from rest_framework import exceptions as rest_exceptions, response, decorators as rest_decorators, permissions as rest_permissions
from rest_framework_simplejwt import tokens, views as jwt_views, serializers as jwt_serializers, exceptions as jwt_exceptions
from django.contrib.auth.decorators import login_required
import openai
from decouple import config
import json

api_key = config("OPENAI_API_KEY")
openai.api_key = api_key

@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def gpt_chat_coding(request):

    query = request.data['query']
    prompt = """
Generate the code based on the requirement. Use the following below JSON format.
```
{language: "", code: ""}

`language` is the programme language of the requirement, for instance python, cpp, csharp, Java...
`code` is the generated code based on the requirement.
```
"""
    res = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        temperature = 0.2,
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ]
    )
    result = res["choices"][0]["message"]["content"]
    print(result)
    code = ""
    type = ""
    try:
        code = json.loads(str(result))['code']
        type = json.loads(str(result))['language']
    except:
        code = "please ask more detailed."

    return response.Response(({"message": code, "type": type}))



@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def gpt_chat_presentation(request):
    presentation_title ='Please provide the slides and presentation about '+ request.data['query']
    query_json = """{
    "input_text": "[[QUERY]]",
    "output_format": "json",
    "json_structure": {
        "slides": "{{presentation_slides}}"
        }
}"""
    question = "Generate a 10 slide presentation for the topic. Produce 60 to 70 words per slide. "+ presentation_title + ".Each slide should have a {{header}}, {{content}}. Each {{header}} should contain title and meaningful of each content. Each {{content}} should contain 2 and more lists. The final slide should be a list of discussion questions.. The Return as JSON."
    prompt = query_json.replace("[[QUERY]]", question)

    res = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{"role": "user", "content":prompt}]
    )

    result = res["choices"][0]["message"]["content"]
    slides = json.loads(str(result))['slides']
    print(slides)
    return response.Response(({"message": slides}))