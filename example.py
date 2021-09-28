from GradientGen import PrintGradient
from os import system


title = r"""      _________ __                           __  ___  ______
     /   _____/|__| ____   _____ _____      /  |/  / / ____/
     \_____  \ |  |/ ___\ /     \\__  \    / /|_/ / / /     
     /        \|  / /_/  |  | |  \/ __ \  / /  / / / /___   
    /_________/|__\___  /|__|_|__/_____/ /_/  /_/  \____/   
                 /_____/                  """

system('cls') # the best way to get ascii escape codes to work on windows is to clear the console
PrintGradient("#25e2d9", "#15ed18", title)
input()
