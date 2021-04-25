from operator import itemgetter

def sort_restaurants(restaurants: list) -> list:
  restaurants.sort(key=itemgetter('rating', 'delivery_fee'))
  restaurants.sort(reverse=True, key=lambda x: x['rating'])

  return restaurants

restaurants = [
  {
    'name': 'Kibon Sorveteria - Saude',
    'rating': 4.9,
    'delivery_fee': 6.99
  },
  {
    'name': 'Makis Place - Saude',
    'rating': 4.7,
    'delivery_fee': 7.99
  },
  {
    'name': 'Sukiya - Saude',
    'rating': 4.6,
    'delivery_fee': 7.99
  },
  {
    'name': 'Viena - Shopping Santa Cruz',
    'rating': 4.4,
    'delivery_fee': 12.49
  },
  {
    'name': 'Girafas Carrefour Metrocar',
    'rating': 4.4,
    'delivery_fee': 5.99
  },
  {
    'name': 'A Feijoada',
    'rating': 4.4,
    'delivery_fee': 9.90
  }
]

sorted_restaurants = sort_restaurants(restaurants)
for restaurant in sorted_restaurants:
  print(restaurant)