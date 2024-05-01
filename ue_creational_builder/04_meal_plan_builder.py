# Implement a MealPlanBuilder to construct a meal plan for a week.
# The builder should allow adding meals for different days and times (e.g., breakfast, lunch, dinner).



if __name__ == '__main__':
    meal_plan_builder = MealPlanBuilder()
    meal_plan = meal_plan_builder.add_meal("Monday", "Breakfast", "Oatmeal with fruits")\
                                 .add_meal("Monday", "Lunch", "Chicken salad")\
                                 .add_meal("Monday", "Dinner", "Grilled salmon with vegetables")\
                                 .build()
    print(meal_plan)
