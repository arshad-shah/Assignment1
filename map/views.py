from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from . import models


@login_required
def update_location(request):
    print("recieved request")
    try:
        user_profle = models.Profile.objects.get(user=request.user)
        print("got user profile", user_profle)
        if not user_profle:
            raise ValueError("Can't get User details")
        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)
        user_profle.last_location = point
        user_profle.save()
        return JsonResponse({"message": f"Set location to {point.wkt}."}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
