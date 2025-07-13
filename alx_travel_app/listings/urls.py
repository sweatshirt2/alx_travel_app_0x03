from rest_framework import renders

from .views import ListingViewSet

listing_list = ListingViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

listing_detail = ListingViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "put": "update", "delete": "destroy"}
)
