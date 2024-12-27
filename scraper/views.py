from django.shortcuts import render


def scrape_twitter(request):
    if request.method == "POST":
        search_query = request.POST.get("search_query")
        tweets = [i for i in range(5)]

        # Render a template with the scraped data
        return render(request, "results.html", {"tweets": tweets})

    return render(request, "index.html")
