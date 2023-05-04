import matplotlib
matplotlib.use('Agg')

import json
import random
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Post
from map.models import nodes
from .mqtt import start_mqtt_client

import matplotlib.pyplot as plt
import os
def start_mqtt(request):
    # Start the MQTT client
    start_mqtt_client()

    # Return a simple response to indicate that the client has started
    return render(request, 'interface.html', {})

def post_list(request, id):
    # Retrieve the latest Post object associated with the node with the given ID
    node = nodes.objects.get(id=id)
    post = Post.objects.filter(po_id=node.id).order_by('-id').first()

    # Render the template and pass the latest Post object as a context variable
    return render(request, 'interface.html', {'post': post})




# def plot_temperature_humidity(request):
#     temperature_data = []
#     humidity_data = []
#     timestamp_data = []
#     posts = Post.objects.all()
#     for post in posts:
#         if post.published_date:
#             temperature_data.append(post.temperature)
#             humidity_data.append(post.humidity)
#             timestamp_data.append(post.published_date.timestamp())

#     plt.subplot(2, 1, 1)
#     plt.plot(timestamp_data, temperature_data, "b.-")
#     plt.ylabel('Temperature (Celsius)')

#     plt.subplot(2, 1, 2)
#     plt.plot(timestamp_data, humidity_data, "r.-")
#     plt.xlabel('Timestamp')
#     plt.ylabel('Humidity (%)')

#     # Create the directory if it doesn't exist
#     if not os.path.exists('static/images/'):
#         os.makedirs('static/images/')

#     # Save the plot in the static/images/ directory
#     plot_path = os.path.join('static/images/', 'temperature_humidity_plot.png')
#     plt.savefig(plot_path)

#     context = {
#         'plot_filename': plot_path
#     }
#     return render(request, 'plot.html', context)



# def plot_temperature_humidity(request):
#     temperature_data = []
#     humidity_data = []
#     posts = Post.objects.all()
#     for post in posts:
#         temperature_data.append(post.temperature)
#         humidity_data.append(post.humidity)

#     plt.plot(humidity_data, temperature_data, "b.-")
#     plt.xlabel('Humidity (%)')
#     plt.ylabel('Temperature (Celsius)')
#     plt.title('Temperature vs. Humidity Data')

#     # Create the directory if it doesn't exist
#     if not os.path.exists('static/images/'):
#         os.makedirs('static/images/')

#     # Save the plot in the static/images/ directory
#     plot_path = os.path.join('static/images/', 'temperature_humidity_plot.png')
#     plt.savefig(plot_path)

#     context = {
#         'plot_filename': plot_path
#     }
#     return render(request, 'plot.html', context)

