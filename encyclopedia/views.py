from . import util

from django.shortcuts import render

from markdown2 import markdown


def index(request):
    context = {
        "entries": util.list_entries(),
        "random_entry": util.get_random_entry()
    }
    return render(request, "encyclopedia/index.html", context)


def encyclopedia(request, title):
    markdown_text = util.get_entry(title)

    if markdown_text:
        encyclopedia_html = markdown(markdown_text)
        context = {
            "title": title,
            "encyclopedia_html": encyclopedia_html,
            "random_entry": util.get_random_entry()
        }
        return render(request, "encyclopedia/encyclopedia.html", context)

    context = {
            "title": "Encyclopedia Not Found",
            "error": f"Encyclopedia of {title} is not present.\
                 Please feel free to add.",
            "random_entry": util.get_random_entry()
        }
    return render(request, "encyclopedia/error.html", context)
