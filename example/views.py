# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from prajwal </h1>
            <p>The current time is { now }. <br>the app will be deployed sooon!</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
