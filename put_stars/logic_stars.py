class RecipeStars:
    def __init__(self, ratings: list = []):
        self.ratings = ratings

    def add_stars(self, rating: float):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            raise ValueError("Рейтинг должен быть от 1 до 5 звезд.")

    def calculate_average_stars(self):
        return sum(self.ratings) / len(self.ratings)

# Пример использования
# recipe = RecipeRating([3.0])
# recipe.add_rating(5)
# recipe.add_rating(5)

# average_rating = recipe.calculate_average_rating()
# print(f"Средний рейтинг рецепта: {average_rating:.1f}")
