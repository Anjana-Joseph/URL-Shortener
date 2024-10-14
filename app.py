from flask import Flask, request, redirect, render_template
import uuid
import json

app = Flask(__name__)

# Load or initialize the URL database (urls.json)
def load_urls():
    try:
        with open("urls.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, create it with an empty dictionary
        with open("urls.json", "w") as file:
            json.dump({}, file)
        return {}
    except json.JSONDecodeError:
        # If JSON is invalid, reset the file to an empty dictionary
        with open("urls.json", "w") as file:
            json.dump({}, file)
        return {}

# Save the URL mappings back to the JSON file
def save_urls(urls):
    with open("urls.json", "w") as file:
        json.dump(urls, file)

# Home route for entering the long URL
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form["long_url"]
        custom_url = request.form.get("custom_url")
        urls = load_urls()  # Load existing URLs

        # Check for custom short URL
        if custom_url:
            if custom_url in urls:
                return "Custom URL is already taken!", 400
            short_url = custom_url
        else:
            short_url = str(uuid.uuid4())[:6]  # Generate a unique short URL

        # Save the new URL mapping with a click count
        urls[short_url] = {"url": long_url, "clicks": 0}
        save_urls(urls)

        return render_template("index.html", short_url=short_url)

    return render_template("index.html")

# Redirection route with click tracking
@app.route("/<short_url>")
def redirect_to_url(short_url):
    urls = load_urls()  # Load existing URLs

    if short_url in urls:
        urls[short_url]["clicks"] += 1  # Increment click count
        save_urls(urls)  # Save updated clicks
        return redirect(urls[short_url]["url"])  # Redirect to the original URL
    else:
        return "URL not found", 404

# Route to display statistics
@app.route("/stats/<short_url>")
def stats(short_url):
    urls = load_urls()  # Load existing URLs

    if short_url in urls:
        url_info = urls[short_url]
        return f"URL: {url_info['url']}<br>Clicks: {url_info['clicks']}"
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)
