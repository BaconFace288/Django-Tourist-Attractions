from django.shortcuts import render

attractions = [
  {'attraction_name': 'Niagara Falls', 'state': 'New York'},
  {'attraction_name': 'Grand Canyon National Park', 'state': 'Arizona'},
  {'attraction_name': 'Mall of America', 'state': 'Minnesota'},
  {'attraction_name': 'Mount Rushmore', 'state': 'South Dakota'},
  {'attraction_name': 'Times Square', 'state': 'New York'},
  {'attraction_name': 'Walt Disney World', 'state': 'Florida'}
]

def home(request):
  context = {"attractions": attractions}
  return render(request, 'tourist_attractions/home.html', context)

def details(request, statename):
  context = {"attractions": attractions, "statename": statename.replace("-", " ")}
  return render(request, 'tourist_attractions/details.html', context)
