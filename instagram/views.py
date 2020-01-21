from django.shortcuts import render, redirect
from instagram.models import DBUSER, Comments, loggedinUser
# Create your views here.

def index(request):
    dbusers = DBUSER.show_db_users()
    return render(request, "main/index.html", context={"dbusers":dbusers})


def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        searched_db_users = DBUSER.search_dbuser_by_name(search_term)
        results = len(searched_db_users)
        message = "{}".format(search_term)
        
        return render(request, "main/search.html", context={"message":message,
                                                            "dbusers":searched_db_users,
                                                            "results":results})
    else:
        message = "You have not searched for any user"
        return render(request, "main/index.html", context={"message":message})
