from flask import request, render_template_string

def profile_page():
    username = request.args.get("username", "")
    template = "<h1>Welcome " + username + "</h1>"
    return render_template_string(template)

def search_page():
    query = request.args.get("q", "")
    return "<p>Results for: " + query + "</p>"