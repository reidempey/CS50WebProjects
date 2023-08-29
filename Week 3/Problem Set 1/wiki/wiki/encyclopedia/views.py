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
    # TODO: As is, this will return False if the entry has no text to display.
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
    search_string = request.GET.get('q')
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
    form_message = ""
    form_title = ""
    form_content = ""
    if request.method == "POST":
        form_title = request.POST.get("new_page_title")
        form_content = request.POST.get("markdown")
        if form_title.lower() in (entry.lower() for entry in util.list_entries()):
            form_message = f"Sorry, an entry with the title {form_title} already exists. Please use a different title."
        else:
            with open(f"entries/{form_title}.md", "w") as file:
                file.write(form_content)
            form_message = f"An entry for {form_title} was successfully created!"

    return render(request, "encyclopedia/new.html", {
        "form_message": form_message,
        "form_title": form_title,
        "form_content": form_content
    })


def edit(request):
    return render(request, 'encyclopedia/edit.html', {
        "entries": util.list_entries()
    })

def edit_entry(request, entry):
    if returned_entry := util.get_entry(entry):
        if request.method == "POST":
            print(request.POST)
            util.save_entry(entry, request.POST.get('markdown'))
            return HttpResponseRedirect(reverse(entries, args=[entry]))
        return render(request, 'encyclopedia/edit_entry.html', {
            "entry_title": entry,
            "form_content": returned_entry
        })
    else:
        return HttpResponseRedirect(reverse("edit"))