##Дополнительное практическое задание по модулю: "Классы и объекты."#module_5_5
###Задание "Свой YouTube"
import sys
import time
import string
class User:
    counter = 0
    def __init__(self,  nickname, password, age):
        self.password= password
        self.age=age
        User.counter +=1

class UrTube:
    def _init__(self, users, videos, current_user):
#        self.users= User.users
#        self.videos= Video.videos
        self.current_user= current_user
        users=[]
        for i in User.counter:
            users.append(User(i))
        self.users = users
        videos=[]
        for i in Video.counter:
            videos.append(Video(i))
        self.videos = videos
    def login(self, nickname, password):
        if nickname in self.users: #!!!возможно надо установить указатель на nickname
            if hash(password)== hash(self.password):
                self.current_user=nickname ##self.users ##
            else:
                print('Неверный пароль')
        else:
            print('Вам необходимо пройти процедуру регистрации')
    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users[nickname]=[password, age]
        self.current_user = nickname ## self.users  ##
#        self.login(nickname, password, age)
    def logout(self, nickname):
        self.current_user= None

    def add(self, *args):
        for v in args:
            print(str(v.title))
            if v.title.lower() not in videos:
                self.videos.append(v.string.lower())
    def get_videos(self, xname):
        xspis=[]
        if xname.lower in self.videos:
            for i in range(len(self.videos)):
                if self.videos[i](xname.lower):
                    xspis.append(self.videos[i])
                i += 1
                continue
    def watch_video(self, xname):
        if self.current_user== None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        elif self.current_user.age <18 and self.adult_mode==True:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for i in range(self.duration):
                time.sleep(0.1)
                i +=1
                print(i, sep=" ")
            print('Конец видео')

class Video:
    counter = 0
    def __init__(self, title, duration, time_now=0, adult_mode = False, bool=False):
       self.title=title
       self.duration= duration
       self.time_now= time_now
       self.adult_mode= adult_mode
       self.bool= bool
       Video.counter += 1


#
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
