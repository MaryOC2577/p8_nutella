# def get_product_page(self, number_of_page: int) -> list:
#         """Return a list of products JSON."""
#         payload = {
#             "search_terms": "",
#             "sort_by": "unique_scans_n",
#             "page_size": 1000,
#             "page": number_of_page,
#             # "content-length": 3000,
#             "json": 1,
#         }
#         res = requests.get(
#             "https://fr.openfoodfacts.org/cgi/search.pl?", params=payload
#         )

#         result = res.json()
#         self.products.extend(result["products"])

from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll
import requests


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("category", nargs="+", type=str)

    def handle(self, *args, **options):
        category_name = options["category"]
        response = requests.get(
            "https://world.openfoodfacts.org/cgi/search.pl?search_terms=pizza&search_simple=1&action=process&json=1&page=1&page_size=20"
        )
        print(response.json())
