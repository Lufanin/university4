import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"{self.nickname}"


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __str__(self):
        return f"Video: {self.title}, Duration: {self.duration} seconds"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, passowrd):
        for user in self.users:
            if user.nickname == nickname and hash(passowrd) == hash(passowrd):
                self.current_user = user
                break
            elif nickname == user and hash(passowrd) != hash(user.passowrd):
                print('Не верный пароль')
                break
            else:
                print('Такого пользователя не существует')
                break

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return result

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в  аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                print(f'Воспроизведение видео: {video.title}')
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(f'{video.time_now}')
                    time.sleep(1)
                print('Конец видео')
                video.time_now = 0
                return
            continue

    def __str__(self):
        return f"UrTube with {len(self.users)} users and {len(self.videos)} videos"

    def __contains__(self, item):
        if isinstance(item, User):
            return item in self.users
        elif isinstance(item, Video):
            return item in self.videos
        return False



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')








