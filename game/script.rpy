# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define n = Character(None)
define al = Character("Алексей", color="#fc3838")
define el = Character("Елена", color="#38befc")
define nik = Character("Николай", color="#fcbe38")
define pet = Character("Пётр Сергеевич", color="#bcefff")
define gal = Character("Галина Викторовна", color="#377528")
define mil = Character("Милана", color="#f0b944")

#fade — смена сцены с постепенным затемнением.
#dissolve — плавное переключение между изображениями.
#moveinleft — перемещение с левого края экрана.
#moveoutright — перемещение за правый край.
define sb = Character("Служба безопасности", color = "#eb16bd" )
define olg = Character("Ольга", color = "#eb1616" )
define vadim = Character("Вадим", color = "#2a3d7a" )
define oleg = Character("Олег", color = "#d86cc1" )
define zmb = Character("Зомби", color = "#27011f" )
define q = Character("Королева", color = "#941616")
define pr = Character("Президент", color = "#2a3d7a")
define s = Character("Солдат", color = "#2a881e")
define kom = Character("Командир", color = "#6eb928")


# Определяем кастомные переходы
init:
    # Переход растворением длительностью 2 секунды
    define dissolve_slow = Dissolve(2.0)
    # Переход через затухание (fade) длительностью 1 секунды
    define fade_fast = Fade(0.5, 0.5, 0.5)
    # Кастомный переход с наложением белого экрана
    define white_flash = Fade(0.5, color="#FFFFFF")

    transform shake_large:
        linear 0.05 yoffset 5
        linear 0.05 xoffset -5
        linear 0.05 yoffset -5
        linear 0.05 xoffset 5
        repeat
    transform alexey_kill_pos:
        xalign 0.3
        yalign 1.0
    transform queen_trans_pos:
        xalign 0.3
        yalign 1.0
    transform cright:
        xalign 0.7
        yalign 1.0





# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    $ startState = StartSceneState()
    $ stateMachine = StateMachine(startState)
    $ stateMachine.Start()
    return
