import pygame
import random
import sys
import linecache
from config import gamespeed,width,height
from box.opening import opening
mode = 0

OP = opening(width,height,gamespeed)

OP.animation()
