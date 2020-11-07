# Gomoku

### 1. Description
This is just for reinforece learning.<br>
Usally described game protocol, data schema, and so on.<br>

### 2. Execute or Install
1. Environment :
```
Package					  Version
------------------------- ---------
numpy 1.19.3
pyinstaller 4.0
pyinstaller-hooks-contrib 2020.10
PyQt5 5.15.1
PyQt5-sip 12.8.1
...
```
2. Executing with python 3.x
> $ python3 main.py

3. Install with PyInstaller 4.x (Unstable)
> $ ./setup.sh

### 3. Game Introduction
It just a 'Gomoku' game. In Korean, "오목".
1. Initial Display
<img src="https://github.com/ndo04343/Gomoku/blob/main/pic/pic_init.png" alt="Initial Display" width="400" height="300">
If you start the game, you'll see this. And you can start the game with black stone.
2. In Game
<img src="https://github.com/ndo04343/Gomoku/blob/main/pic/pic_ingame.png" alt="In Game Display" width="400" height="300">
Maybe you keep the game like this picture. In this game, you must follow "33 rule".
3. Rule
<img src="https://github.com/ndo04343/Gomoku/blob/main/pic/pic_three_three.png" alt="33 Display" width="400" height="300">
If you are a black stone user, you have to follow "33 rule".<br>
I don't know about it. Just search it.
<br>
<img src="https://github.com/ndo04343/Gomoku/blob/main/pic/pic_cannot.png" alt="Cannot Display" width="400" height="300">
You can see also this picture if you put the stone on the position that is already putted. <br>
4. Game Set
<img src="https://github.com/ndo04343/Gomoku/blob/main/pic/pic_white_win.png" alt="Game Set Display" width="400" height="300">
If the game is setted, this picture be displayed.

 ### 4. Game Protocol
 You can modify this codes so that I want to you to create a reinforcement learning agent. Maybe, it's very easy to change just the main function a little. If you want to change it, please concentrate on <strong>Gomoku.py</strong>, not <strong>main.py</strong>.
```
# Gomoku.py
...
GAME_BLACK_TURN 
GAME_WHITE_TURN

GAME_BLACK_WIN
GAME_WHITE_WIN
...
```
These are flag of the game. In game class, there is a flag variable.
You can check or modify this variable compactly.
```
# Gomoku.py
...
RES_CANNOT
RES_NOTHING
RES_THREE_THREE
RES_BLACK_WIN
RES_WHITE_WIN
...
```
These are result of method <strong>.putStone(x, y, type)</strong> . Each cases are matched with pictures above. You have to handle it.
```
# Gomoku.py
...
STONE_BLANK
STONE_BLACK
STONE_WHITE 
...
```
If you want to use .putStone() method, the third parameter called "type" is matched with these variable. 
