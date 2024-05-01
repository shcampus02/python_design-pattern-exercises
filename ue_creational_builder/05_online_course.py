# Create a builder to construct the structure of an online course including modules, lessons, and quizzes.




if __name__ == '__main__':
    course_builder = OnlineCourseBuilder("Introduction to Python")
    course = course_builder.add_module("Basics")\
                           .add_lesson("Basics", "Introduction to Python")\
                           .add_lesson("Basics", "Variables and Data Types")\
                           .add_quiz("Basics", "Basic Python Quiz")\
                           .build()
    print(course)
