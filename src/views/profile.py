from flask import request, render_template_string

def profile_page():
    # VULNERABLE: user input rendered directly into HTML
    username = request.args.get("username", "")
    template = f"<h1>Welcome {username}</h1>"
    return render_template_string(template)

def search_page():
    # VULNERABLE: XSS via query param
    query = request.args.get("q", "")
    return f"<p>Results for: {query}</p>"
