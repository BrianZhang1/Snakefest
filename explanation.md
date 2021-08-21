# Introduction

## Purpose

The following explains the file structure of the `pysnake\` project and the role of all files/folders. It acts as an introduction and a quick way to understand the project.

## Copying

Pysnake is an extended version of the popular Snake game.
Copyright (C) 2021  Brian Zhang

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>

## Structure

* [pysnake\\](..\\pysnake\\)
    * [snake\\](snake\\)
        * [assets\\](snake\\assets\\)
        * [game_classes\\](snake\\game_classes\\)
        * [global_helpers\\](snake\\global_helpers\\)
        * [states\\](snake\\states\\)
        * [app.py](snake\\app.py)
    * [.gitignore](.gitignore)
    * [COPYING](COPYING)
    * [explanation.md](explanation.md)
    * [README.md](README.md)
    * [requirements.txt](requirements.txt)
    * [start_app.py](start_app.py)

# Explanation

## [snake\\](snake\\)
Contains all files that are needed to run the app. The app itself can be started through `start_app.py`. Under `snake\\` and all its subdirectories, each file (usually) holds one class/purpose, and at the top of each file is a description that explains what the file/class does.

### [assets\\](snake\\assets\\)
Contains all assets (mostly images that act as sprites), sources for images when applicable, and Inkscape svgs incase I, or anybody else, want to ever edit the images.

### [game_classes\\](snake\\game_classes\\)
Contains all classes that are used in `states\\game.py`, which is the game part of the app (where you actually play snake).

### [global_helpers\\](snake\\global_helpers\\)
Helpers that are global (duh). For example, `assets.py` can be found here, which processes all images in `assets\\` into PhotoImage objects which can be used and rendered by other files. At the top of each file is a description that explains what the file

### [states\\](snake\\states\\)
Contains all the states. A state is like a page. Examples include `main_menu.py`, `game.py`, `map_select.py`.

### [app.py](snake\\app.py)
Controls the app at the highest level. Manages the current state, changing between states, and the tkinter event loop.

## [.gitignore](.gitignore)
List of files/directories to ignore when making commits/pushes.

## [explanation.md](explanation.md)
Hey, that's the file you're on right now!

## [COPYING](COPYING)
GNU GPL v3 license. Tells others what they are allowed to do with this code.

## [README.md](README.md)
Describes the project and other relevant topics.

## [requirements.txt](requirements.txt)
List of the packages required to run the app.

## [start_app.py](start_app.py)
Runs the app.
