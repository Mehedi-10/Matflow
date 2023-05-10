import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
import matplotlib.pyplot as plt
from django.http import HttpResponse

@api_view(['GET','POST'])
def hello_world(request):
    file = request.FILES.get('file')
    sv=pd.read_csv(file)

    print(sv)
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])

    # convert the figure to a PNG image and return it as a response
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()

    response = HttpResponse(image_png, content_type='image/png')
    return response
