from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import markdown2
import random
from . import util

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, entry):
    if returned_entry := util.get_entry(entry):
        html_entry = markdown2.markdown(returned_entry)
        return render(request, 'encyclopedia/entry.html', {
            "entry": entry.capitalize(),
            "html_entry": html_entry
        })
    else:
        print(f"entry not found for {entry}")
        # TQ: If an entry name is typed with the / at the end, it all throws an error...
        return render(request, 'encyclopedia/none.html', {
            "missing_entry": entry
        })

def random_entry(request):
    random_entry = random.choice(util.list_entries())
    # print(random_entry)
    return HttpResponseRedirect(f"{random_entry}")

# TODO: Finish search functionality
# Be sure to include for exact matches and partial matches
def search(request):
    if request.method == "POST":
        search_string = request.POST['q']
        entry_list = util.list_entries()
        # print(entry_list)
        if search_string.lower() in (entry.lower() for entry in entry_list):
            return HttpResponseRedirect(f"{search_string}")
        else:
            results = []
            for entry in entry_list:
                if search_string.lower() in entry.lower():
                    results.append(entry)
            if results:
                return render(request, "encyclopedia/search.html", {
                    "query": search_string,
                    "entries": results
                })
            else:
                return render(request, "encyclopedia/search.html", {
                    "query": search_string
                })
            
def new(request):
    return render(request, "encyclopedia/new.html")