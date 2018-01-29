import cx_Freeze

#graphics
bgImg = ("assets/space.jpg")
playerImg = ("assets/spaceship.png")
mob1Img = ("assets/rock.png")
bulletImg = ("assets/bullet1.png")
mntdewImg = ("assets/mntdew.jpg")

#sounnds
pewOgg = ("assets/pew.wav")
wowOgg = ("assets/wow.ogg")
rektWav = ("assets/rekt.wav")
plus50 = ("assets/plus50.ogg")
bgMusic = ("assets/space.wav")
spMusic = ("assets/bgmusic.ogg")

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "Pygame_Project",
    options ={
        "build.exe":{
            "packages" : ["pygame"],
            "include_files":[
                bgImg,playerImg,mob1Img,bulletImg,
                mntdewImg,pewOgg,wowOgg,rektWav,plus50,bgMusic,
                spMusic
            ]
        }
    },
    executables = executables

)
