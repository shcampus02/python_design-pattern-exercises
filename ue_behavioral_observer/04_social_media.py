"""
Übung 4 - Social Media Plattform

Das Observer-Muster kann auch in einem Social-Media-System verwendet werden.
Ein User kann einem anderen User folgen und erhält dann Updates, wenn dieser User neue Posts veröffentlicht.

Implementieren Sie die Klassen 'Post', 'User' und 'SocialMediaPlatform'.
"""


class Post:
    pass


class User:
    pass


class SocialMediaPlatform:
    pass


if __name__ == "__main__":
    platform = SocialMediaPlatform()
    user1 = User()
    user2 = User()
    platform.follow(user1, user2)
    user2.post("This is my new post!")
    user1.update()