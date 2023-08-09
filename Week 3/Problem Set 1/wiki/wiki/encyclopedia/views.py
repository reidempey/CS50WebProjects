from django.http import HttpResponse
from django.shortcuts import render
import markdown2
from . import util

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, entry):
    # TODO: Fix this so it works with templates
    if returned_entry := util.get_entry(entry):
        html_entry = markdown2.markdown(returned_entry)
        return render(request, 'encyclopedia/entry.html', {
            "entry": entry.capitalize(),
            "html_entry": html_entry
        })
    else:
        # TQ: If an entry name is typed with the / at the end, it all throws an error...
        return render(request, 'encyclopedia/none.html', {
            "missing_entry": entry
        })
