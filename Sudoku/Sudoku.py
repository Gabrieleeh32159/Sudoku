#LIBRERÍAS
from colorama import *
import os
from random import choice
import time
import json
import pandas as pd
from collections import OrderedDict

#Tableros
sudokus9x9 = [
[[5, 7, 6, 8, 1, 2, 3, 9, 4],
[9, 1, 4, 7, 5, 3, 6, 8, 2],
[3, 2, 8, 9, 4, 6, 7, 1, 5],
[6, 9, 3, 2, 8, 7, 5, 4, 1],
[2, 5, 1, 4, 6, 9, 8, 3, 7],
[4, 8, 7, 5, 3, 1, 9, 2, 6],
[1, 3, 5, 6, 9, 4, 2, 7, 8],
[7, 6, 9, 1, 2, 8, 4, 5, 3],
[8, 4, 2, 3, 7, 5, 1, 6, 9]],
[[3, 1, 2, 8, 9, 5, 6, 7, 4],
[6, 5, 9, 1, 7, 4, 8, 2, 3],
[4, 7, 8, 6, 2, 3, 1, 5, 9],
[9, 4, 5, 7, 8, 1, 2, 3, 6],
[8, 3, 6, 9, 5, 2, 7, 4, 1],
[1, 2, 7, 4, 3, 6, 9, 8, 5],
[7, 8, 4, 3, 6, 9, 5, 1, 2],
[2, 9, 3, 5, 1, 7, 4, 6, 8],
[5, 6, 1, 2, 4, 8, 3, 9, 7]],
[[7, 4, 1, 3, 2, 8, 5, 9, 6],
[9, 5, 3, 6, 1, 4, 8, 2, 7],
[2, 8, 6, 9, 7, 5, 3, 4, 1],
[8, 6, 9, 2, 3, 1, 7, 5, 4],
[5, 1, 2, 4, 8, 7, 9, 6, 3],
[4, 3, 7, 5, 9, 6, 1, 8, 2],
[3, 2, 8, 7, 6, 9, 4, 1, 5],
[6, 9, 5, 1, 4, 3, 2, 7, 8],
[1, 7, 4, 8, 5, 2, 6, 3, 9]],
[[8, 7, 5, 4, 3, 1, 2, 6, 9],
[6, 3, 4, 9, 2, 8, 5, 7, 1],
[1, 2, 9, 5, 7, 6, 3, 4, 8],
[5, 1, 7, 8, 6, 9, 4, 2, 3],
[9, 4, 6, 3, 1, 2, 7, 8, 5],
[2, 8, 3, 7, 4, 5, 9, 1, 6],
[4, 5, 2, 1, 8, 3, 6, 9, 7],
[3, 6, 1, 2, 9, 7, 8, 5, 4],
[7, 9, 8, 6, 5, 4, 1, 3, 2]],
[[1, 7, 9, 2, 3, 5, 8, 4, 6],
[2, 6, 8, 9, 4, 7, 1, 5, 3],
[4, 5, 3, 1, 6, 8, 7, 9, 2],
[9, 8, 5, 4, 1, 6, 3, 2, 7],
[6, 4, 1, 7, 2, 3, 9, 8, 5],
[7, 3, 2, 8, 5, 9, 6, 1, 4],
[8, 9, 4, 3, 7, 2, 5, 6, 1],
[3, 1, 6, 5, 8, 4, 2, 7, 9],
[5, 2, 7, 6, 9, 1, 4, 3, 8]],
[[1, 6, 5, 3, 2, 9, 7, 8, 4],
[9, 7, 8, 4, 1, 6, 2, 5, 3],
[3, 4, 2, 8, 7, 5, 1, 6, 9],
[2, 8, 4, 6, 3, 1, 9, 7, 5],
[7, 3, 9, 5, 4, 2, 6, 1, 8],
[5, 1, 6, 9, 8, 7, 3, 4, 2],
[8, 5, 1, 7, 9, 3, 4, 2, 6],
[4, 2, 3, 1, 6, 8, 5, 9, 7],
[6, 9, 7, 2, 5, 4, 8, 3, 1]],
[[1, 3, 5, 8, 9, 7, 4, 6, 2],
[6, 4, 8, 1, 5, 2, 3, 9, 7],
[7, 2, 9, 4, 3, 6, 1, 5, 8],
[5, 6, 4, 2, 7, 8, 9, 3, 1],
[2, 8, 1, 9, 4, 3, 5, 7, 6],
[9, 7, 3, 6, 1, 5, 2, 8, 4],
[4, 9, 7, 3, 8, 1, 6, 2, 5],
[3, 5, 6, 7, 2, 4, 8, 1, 9],
[8, 1, 2, 5, 6, 9, 7, 4, 3]],
[[3, 9, 6, 7, 8, 2, 4, 5, 1],
[1, 7, 5, 4, 9, 3, 8, 2, 6],
[8, 4, 2, 5, 6, 1, 7, 9, 3],
[5, 8, 1, 6, 3, 4, 2, 7, 9],
[7, 6, 9, 2, 1, 8, 3, 4, 5],
[4, 2, 3, 9, 5, 7, 6, 1, 8],
[2, 5, 8, 3, 4, 9, 1, 6, 7],
[9, 3, 7, 1, 2, 6, 5, 8, 4],
[6, 1, 4, 8, 7, 5, 9, 3, 2]],
[[9, 2, 1, 6, 3, 5, 7, 4, 8],
[3, 5, 4, 8, 7, 2, 1, 9, 6],
[7, 6, 8, 1, 4, 9, 3, 2, 5],
[2, 7, 9, 4, 8, 1, 6, 5, 3],
[6, 8, 5, 3, 9, 7, 4, 1, 2],
[4, 1, 3, 2, 5, 6, 9, 8, 7],
[8, 3, 6, 5, 1, 4, 2, 7, 9],
[1, 9, 2, 7, 6, 8, 5, 3, 4],
[5, 4, 7, 9, 2, 3, 8, 6, 1]],
[[2, 3, 6, 8, 5, 1, 4, 7, 9],
[1, 5, 4, 2, 7, 9, 6, 3, 8],
[8, 7, 9, 6, 3, 4, 1, 5, 2],
[7, 9, 5, 3, 1, 8, 2, 4, 6],
[3, 8, 2, 4, 9, 6, 7, 1, 5],
[4, 6, 1, 5, 2, 7, 8, 9, 3],
[5, 4, 7, 9, 6, 2, 3, 8, 1],
[9, 2, 8, 1, 4, 3, 5, 6, 7],
[6, 1, 3, 7, 8, 5, 9, 2, 4]],
[[1, 4, 2, 3, 8, 9, 7, 6, 5],
[8, 3, 5, 4, 7, 6, 2, 9, 1],
[6, 7, 9, 2, 5, 1, 3, 4, 8],
[2, 9, 3, 7, 1, 4, 5, 8, 6],
[7, 6, 4, 5, 3, 8, 1, 2, 9],
[5, 1, 8, 6, 9, 2, 4, 7, 3],
[3, 8, 6, 1, 2, 7, 9, 5, 4],
[9, 5, 7, 8, 4, 3, 6, 1, 2],
[4, 2, 1, 9, 6, 5, 8, 3, 7]],
[[4, 8, 7, 5, 9, 1, 3, 6, 2],
[1, 2, 3, 7, 4, 6, 5, 9, 8],
[6, 5, 9, 3, 8, 2, 7, 4, 1],
[7, 9, 6, 8, 2, 3, 4, 1, 5],
[8, 4, 5, 6, 1, 7, 9, 2, 3],
[2, 3, 1, 4, 5, 9, 8, 7, 6],
[3, 1, 2, 9, 7, 5, 6, 8, 4],
[9, 6, 4, 1, 3, 8, 2, 5, 7],
[5, 7, 8, 2, 6, 4, 1, 3, 9]],
[[8, 6, 1, 3, 2, 9, 4, 7, 5],
[4, 9, 3, 5, 7, 6, 8, 1, 2],
[2, 5, 7, 1, 8, 4, 9, 3, 6],
[3, 4, 9, 8, 4, 2, 1, 6, 7],
[7, 1, 2, 6, 4, 3, 5, 9, 8],
[6, 8, 5, 7, 9, 1, 3, 2, 4],
[5, 3, 8, 2, 1, 7, 6, 4, 9],
[1, 2, 4, 9, 6, 5, 7, 8, 3],
[9, 7, 6, 4, 3, 8, 2, 5, 1]],
[[1, 5, 6, 4, 7, 3, 8, 9, 2],
[4, 9, 3, 8, 2, 6, 5, 1, 7],
[7, 8, 2, 5, 1, 9, 6, 4, 3],
[5, 7, 2, 6, 8, 1, 4, 3, 9],
[8, 3, 1, 7, 9, 4, 2, 5, 6],
[9, 6, 4, 2, 3, 5, 1, 7, 8],
[6, 8, 5, 9, 4, 7, 3, 2, 1],
[3, 4, 7, 1, 6, 2, 9, 8, 5],
[2, 1, 9, 3, 5, 8, 7, 6, 4]],
[[6, 5, 1, 8, 7, 3, 4, 2, 9],
 [7, 8, 9, 1, 4, 2, 5, 3, 6],
 [4, 3, 2, 5, 9, 6, 7, 8, 1],
 [8, 9, 6, 7, 5, 3, 2, 1, 4],
 [2, 1, 5, 4, 6, 9, 8, 7, 3],
 [3, 7, 4, 2, 8, 1, 6, 9, 5],
 [1, 6, 8, 9, 2, 5, 3, 4, 7],
 [5, 2, 7, 3, 1, 4, 9, 6, 8],
 [9, 4, 3, 6, 7, 8, 1, 5, 2]],
[[2, 9, 8, 7, 5, 1, 3, 4, 6],
 [3, 1, 4, 2, 6, 8, 7, 9, 5],
 [7, 5, 6, 4, 9, 3, 2, 8, 1],
 [8, 6, 1, 3, 2, 4, 9, 5, 7],
 [4, 7, 9, 6, 8, 5, 1, 2, 3],
 [5, 2, 3, 1, 7, 9, 8, 6, 4],
 [9, 3, 5, 8, 1, 6, 4, 7, 2],
 [1, 8, 2, 5, 4, 7, 6, 3, 9],
 [6, 4, 7, 9, 3, 2, 5, 1, 8]],
[[1, 7, 9, 3, 4, 5, 2, 6, 8],
  [8, 5, 6, 9, 2, 1, 4, 7, 3],
  [2, 4, 3, 8, 7, 6, 1, 9, 5],
  [4, 1, 8, 7, 6, 2, 5, 3, 9],
  [3, 9, 7, 5, 1, 8, 6, 2, 4],
  [6, 2, 5, 4, 9, 3, 7, 8, 1],
  [5, 8, 4, 2, 3, 7, 9, 1, 6],
  [7, 3, 1, 6, 5, 9, 8, 4, 2],
  [6, 9, 2, 1, 8, 4, 3, 5, 7]],
[[4, 5, 3, 8, 6, 9, 2, 1, 7],
 [6, 9, 7, 1, 3, 2, 5, 8, 4],
 [8, 2, 1, 5, 4, 7, 9, 3, 6],
 [2, 7, 4, 6, 8, 5, 3, 9, 1],
 [3, 8, 9, 7, 1, 4, 6, 2, 5],
 [5, 1, 6, 9, 2, 3, 4, 7, 8],
 [1, 3, 8, 4, 9, 6, 7, 5, 2],
 [7, 6, 2, 3, 5, 1, 8, 4, 9],
 [9, 4, 5, 2, 7, 8, 1, 6, 3]],
[[3, 9, 2, 4, 8, 5, 1, 7, 6],
 [1, 5, 6, 9, 7, 3, 2, 8, 4],
 [4, 7, 8, 2, 6, 1, 9, 3, 5],
 [6, 4, 7, 5, 1, 8, 3, 9, 2],
 [5, 1, 3, 7, 2, 9, 6, 4, 8],
 [8, 2, 9, 6, 3, 4, 5, 1, 7],
 [9, 8, 4, 1, 5, 2, 7, 6, 3],
 [7, 3, 5, 8, 9, 6, 4, 2, 1],
 [2, 6, 1, 3, 4, 7, 8, 5, 9]],
[[1, 4, 7, 3, 5, 6, 2, 8, 9],
 [3, 9, 5, 1, 2, 8, 7, 6, 4],
 [8, 2, 6, 7, 9, 4, 5, 1, 3],
 [6, 8, 4, 2, 7, 1, 9, 3, 5],
 [7, 5, 3, 6, 4, 9, 1, 2, 8],
 [2, 1, 9, 5, 8, 3, 6, 4, 7],
 [9, 6, 2, 8, 3, 7, 4, 5, 1],
 [5, 7, 8, 4, 1, 2, 3, 9, 6],
 [4, 3, 1, 9, 6, 5, 8, 7, 2]],
[[9, 5, 6, 2, 1, 7, 4, 8, 3],
 [7, 4, 1, 8, 5, 3, 6, 9, 2],
 [3, 2, 8, 6, 4, 9, 1, 7, 5],
 [8, 7, 2, 5, 9, 1, 3, 4, 6],
 [6, 9, 5, 3, 2, 4, 8, 1, 7],
 [1, 3, 4, 7, 6, 8, 5, 2, 9],
 [2, 6, 9, 1, 8, 5, 7, 3, 4],
 [4, 8, 3, 9, 7, 6, 2, 5, 1],
 [5, 1, 7, 4, 3, 2, 9, 6, 8]],
[[9, 1, 4, 8, 2, 6, 5, 3, 7],
 [2, 3, 5, 1, 4, 7, 6, 9, 8],
 [7, 8, 6, 3, 9, 5, 4, 2, 1],
 [5, 4, 3, 6, 8, 9, 7, 1, 2],
 [6, 2, 9, 7, 1, 4, 8, 5, 3],
 [1, 7, 8, 5, 3, 2, 9, 4, 6],
 [3, 6, 1, 4, 5, 8, 2, 7, 9],
 [8, 5, 2, 9, 7, 3, 1, 6, 4],
 [4, 9, 7, 2, 6, 1, 3, 8, 5]],
[[5, 1, 7, 2, 6, 4, 8, 9, 3],
 [9, 4, 6, 3, 8, 1, 5, 7, 2],
 [3, 2, 8, 9, 5, 7, 1, 4, 6],
 [6, 8, 1, 7, 2, 5, 4, 3, 9],
 [7, 5, 9, 1, 4, 3, 6, 2, 8],
 [4, 3, 2, 6, 9, 8, 7, 1, 5],
 [2, 9, 4, 5, 7, 6, 3, 8, 1],
 [8, 6, 3, 4, 1, 2, 9, 5, 7],
 [1, 7, 5, 8, 3, 9, 2, 6, 4]],
[[6, 2, 5, 3, 9, 8, 1, 7, 4],
 [3, 9, 4, 5, 1, 7, 8, 6, 2],
 [7, 8, 1, 4, 2, 6, 5, 3, 9],
 [1, 5, 2, 6, 7, 9, 3, 4, 8],
 [4, 3, 6, 8, 5, 1, 9, 2, 7],
 [8, 7, 9, 2, 4, 3, 6, 1, 5],
 [9, 6, 7, 1, 8, 2, 4, 5, 3],
 [5, 1, 8, 7, 3, 4, 2, 9, 6],
 [2, 4, 3, 9, 6, 5, 7, 8, 1]],
[[9, 1, 7, 4, 5, 3, 2, 6, 8],
 [3, 6, 8, 2, 1, 7, 4, 9, 5],
 [5, 4, 2, 6, 9, 8, 3, 1, 7],
 [4, 2, 6, 9, 7, 5, 8, 3, 1],
 [7, 3, 5, 8, 6, 1, 9, 4, 2],
 [1, 8, 9, 3, 2, 4, 5, 7, 6],
 [8, 7, 1, 5, 3, 9, 6, 2, 4],
 [6, 9, 4, 1, 8, 2, 7, 5, 3],
 [2, 5, 3, 7, 4, 6, 1, 8, 9]],
[[2, 8, 6, 3, 9, 7, 5, 4, 1],
 [3, 4, 9, 5, 6, 1, 8, 7, 2],
 [7, 1, 5, 4, 8, 2, 3, 6, 9],
 [4, 3, 7, 8, 1, 6, 2, 9, 5],
 [1, 6, 8, 2, 5, 9, 4, 3, 7],
 [9, 5, 2, 7, 4, 3, 1, 8, 6],
 [5, 7, 4, 9, 2, 8, 6, 1, 3],
 [8, 9, 1, 6, 3, 5, 7, 2, 4],
 [6, 2, 3, 1, 7, 4, 9, 5, 8]],
[[4, 3, 5, 7, 6, 2, 1, 9, 8],
 [1, 2, 7, 3, 8, 9, 5, 6, 4],
 [6, 8, 9, 1, 4, 5, 7, 3, 2],
 [7, 5, 8, 9, 2, 1, 3, 4, 6],
 [3, 6, 4, 5, 7, 8, 2, 1, 9],
 [2, 9, 1, 6, 3, 4, 8, 7, 5],
 [5, 4, 6, 8, 1, 7, 9, 2, 3],
 [9, 7, 2, 4, 5, 3, 6, 8, 1],
 [8, 1, 3, 2, 9, 6, 4, 5, 7]],
[[1, 4, 5, 6, 8, 7, 3, 2, 9],
 [3, 2, 6, 9, 1, 4, 5, 7, 8],
 [8, 9, 7, 3, 5, 2, 6, 4, 1],
 [7, 8, 1, 4, 3, 6, 2, 9, 5],
 [9, 5, 4, 7, 2, 8, 1, 3, 6],
 [6, 3, 2, 5, 9, 1, 4, 8, 7],
 [5, 6, 8, 2, 4, 9, 7, 1, 3],
 [4, 1, 3, 8, 7, 5, 9, 6, 2],
 [2, 7, 9, 1, 6, 3, 8, 5, 4]],
 [[3, 7, 9, 2, 8, 5, 6, 1, 4],
  [8, 1, 4, 9, 7, 6, 2, 5, 3],
  [6, 5, 2, 3, 4, 1, 7, 9, 8],
  [1, 8, 6, 4, 2, 3, 9, 7, 5],
  [4, 9, 5, 6, 1, 7, 8, 3, 2],
  [7, 2, 3, 8, 5, 9, 4, 6, 1],
  [9, 3, 8, 5, 6, 4, 1, 2, 7],
  [2, 6, 1, 7, 3, 8, 5, 4, 9],
  [5, 4, 7, 1, 9, 2, 3, 8, 6]],
[[3, 1, 5, 7, 8, 9, 4, 6, 2],
  [9, 2, 7, 6, 4, 3, 5, 8, 1],
  [4, 6, 8, 2, 1, 5, 7, 9, 3],
  [6, 9, 3, 8, 5, 7, 2, 1, 4],
  [1, 8, 4, 3, 6, 2, 9, 5, 7],
  [7, 5, 2, 4, 9, 1, 8, 3, 6],
  [8, 4, 9, 1, 7, 6, 3, 2, 5],
  [2, 7, 6, 5, 3, 8, 1, 4, 9],
  [5, 3, 1, 9, 2, 4, 6, 7, 8]],
[[8, 4, 3, 9, 1, 5, 6, 7, 2],
  [6, 7, 1, 8, 2, 3, 5, 4, 9],
  [9, 2, 5, 6, 4, 7, 1, 3, 8],
  [2, 6, 9, 7, 3, 1, 8, 5, 4],
  [4, 5, 7, 2, 8, 9, 3, 1, 6],
  [3, 1, 8, 5, 6, 4, 9, 2, 7],
  [7, 9, 4, 1, 5, 8, 2, 6, 3],
  [5, 8, 6, 3, 7, 2, 4, 9, 1],
  [1, 3, 2, 4, 9, 6, 7, 8, 5]],
[[8, 3, 1, 4, 2, 6, 7, 9, 5],
  [9, 6, 4, 7, 8, 5, 3, 1, 2],
  [5, 7, 2, 1, 9, 3, 4, 8, 6],
  [2, 5, 3, 8, 7, 1, 9, 6, 4],
  [1, 9, 8, 5, 6, 4, 2, 3, 7],
  [7, 4, 6, 9, 3, 2, 8, 5, 1],
  [6, 1, 7, 3, 4, 9, 5, 2, 8],
  [3, 8, 5, 2, 1, 7, 6, 4, 9],
  [4, 2, 9, 6, 5, 8, 1, 7, 3]],
[[7, 2, 8, 3, 6, 5, 9, 4, 1],
  [6, 1, 5, 9, 4, 8, 3, 7, 2],
  [3, 4, 9, 1, 7, 2, 8, 6, 5],
  [4, 5, 7, 8, 3, 1, 2, 9, 6],
  [8, 9, 1, 4, 2, 6, 5, 3, 7],
  [2, 3, 6, 7, 5, 9, 1, 8, 4],
  [9, 8, 2, 6, 1, 4, 7, 5, 3],
  [1, 7, 4, 5, 9, 3, 6, 2, 8],
  [5, 6, 3, 2, 8, 7, 4, 1, 9]],
[[5, 4, 9, 3, 1, 8, 7, 6, 2],
  [7, 1, 8, 2, 6, 5, 9, 4, 3],
  [2, 3, 6, 7, 4, 9, 1, 8, 5],
  [9, 6, 2, 1, 7, 4, 5, 3, 8],
  [4, 8, 3, 5, 9, 2, 6, 1, 7],
  [1, 5, 7, 8, 3, 6, 4, 2, 9],
  [3, 9, 1, 6, 8, 7, 2, 5, 4],
  [6, 7, 5, 4, 2, 3, 8, 9, 1],
  [8, 2, 4, 9, 5, 1, 3, 7, 6]],
[[5, 2, 7, 3, 4, 8, 9, 6, 1],
  [6, 8, 1, 9, 5, 2, 4, 7, 3],
  [4, 9, 3, 6, 1, 7, 2, 5, 8],
  [9, 1, 2, 5, 7, 3, 8, 4, 6],
  [7, 4, 5, 8, 6, 1, 3, 2, 9],
  [8, 3, 6, 2, 9, 4, 5, 1, 7],
  [1, 5, 8, 4, 3, 6, 7, 9, 2],
  [2, 6, 4, 7, 8, 9, 1, 3, 5],
  [3, 7, 9, 1, 2, 5, 6, 8, 4]],
[[9, 8, 6, 4, 2, 3, 7, 5, 1],
  [5, 3, 1, 6, 7, 9, 2, 8, 4],
  [2, 4, 7, 8, 5, 1, 3, 9, 6],
  [3, 5, 4, 7, 1, 8, 9, 6, 2],
  [6, 1, 8, 5, 9, 2, 4, 3, 7],
  [7, 9, 2, 3, 6, 4, 8, 1, 5],
  [4, 6, 9, 2, 3, 5, 1, 7, 8],
  [1, 2, 5, 9, 8, 7, 6, 4, 3],
  [8, 7, 3, 1, 4, 6, 5, 2, 9]],
[[5, 3, 8, 6, 4, 2, 1, 9, 7],
  [2, 9, 4, 5, 7, 1, 8, 3, 6],
  [6, 1, 7, 9, 8, 3, 4, 5, 2],
  [4, 2, 5, 8, 9, 7, 3, 6, 1],
  [1, 8, 9, 3, 2, 6, 5, 7, 4],
  [7, 6, 3, 4, 1, 5, 9, 2, 8],
  [8, 4, 6, 2, 3, 9, 7, 1, 5],
  [3, 5, 1, 7, 6, 8, 2, 4, 9],
  [9, 7, 2, 1, 5, 4, 6, 8, 3]],
[[7, 5, 6, 4, 8, 3, 1, 2, 9],
  [1, 2, 3, 9, 6, 7, 5, 4, 8],
  [8, 9, 4, 2, 5, 1, 6, 3, 7],
  [2, 7, 1, 3, 4, 8, 9, 6, 5],
  [4, 6, 5, 1, 7, 9, 3, 8, 2],
  [3, 8, 9, 6, 2, 5, 7, 1, 4],
  [6, 3, 8, 7, 9, 4, 2, 5, 1],
  [5, 1, 7, 8, 3, 2, 4, 9, 6],
  [9, 4, 2, 5, 1, 6, 8, 7, 3]],
[[1, 4, 6, 2, 8, 5, 7, 3, 9],
  [3, 5, 8, 9, 7, 6, 2, 4, 1],
  [7, 9, 2, 1, 3, 4, 8, 6, 5],
  [4, 6, 3, 8, 9, 2, 5, 1, 7],
  [5, 2, 7, 4, 1, 3, 9, 8, 6],
  [8, 1, 9, 6, 5, 7, 4, 2, 3],
  [6, 8, 5, 7, 4, 1, 3, 9, 2],
  [2, 7, 4, 3, 6, 9, 1, 5, 8],
  [9, 3, 1, 5, 2, 8, 6, 7, 4]],
[[2, 8, 9, 3, 6, 5, 1, 7, 4],
  [7, 3, 4, 2, 8, 1, 6, 9, 5],
  [5, 6, 1, 7, 4, 9, 3, 8, 2],
  [9, 1, 2, 8, 7, 3, 5, 4, 6],
  [3, 5, 8, 6, 1, 4, 7, 2, 9],
  [4, 7, 6, 9, 5, 2, 8, 1, 3],
  [1, 2, 5, 4, 3, 7, 9, 6, 8],
  [6, 9, 7, 5, 2, 8, 4, 3, 1],
  [8, 4, 3, 1, 9, 6, 2, 5, 7]],
[[5, 3, 1, 4, 9, 6, 8, 2, 7],
  [7, 6, 4, 8, 1, 2, 3, 9, 5],
  [2, 8, 9, 3, 5, 7, 1, 4, 6],
  [1, 9, 2, 5, 7, 4, 6, 8, 3],
  [3, 5, 6, 1, 8, 9, 2, 7, 4],
  [8, 4, 7, 6, 2, 3, 5, 1, 9],
  [4, 2, 3, 9, 6, 1, 7, 5, 8],
  [6, 1, 5, 7, 4, 8, 9, 3, 2],
  [9, 7, 8, 2, 3, 5, 4, 6, 1]],
[[2, 9, 4, 7, 1, 8, 5, 3, 6],
  [5, 7, 8, 2, 6, 3, 9, 4, 1],
  [6, 3, 1, 5, 4, 9, 7, 2, 8],
  [4, 1, 2, 6, 7, 5, 8, 9, 3],
  [7, 8, 6, 9, 3, 1, 4, 5, 2],
  [9, 5, 3, 8, 2, 4, 6, 1, 7],
  [1, 4, 7, 3, 5, 6, 2, 8, 9],
  [3, 6, 9, 4, 8, 2, 1, 7, 5],
  [8, 2, 5, 1, 9, 7, 3, 6, 4]],
[[5, 3, 6, 9, 7, 4, 8, 2, 1],
  [7, 2, 9, 8, 1, 6, 5, 3, 4],
  [1, 4, 8, 5, 3, 2, 7, 6, 9],
  [3, 6, 1, 7, 5, 8, 9, 4, 2],
  [9, 8, 2, 6, 4, 3, 1, 5, 7],
  [4, 5, 7, 1, 2, 9, 3, 8, 6],
  [2, 7, 3, 4, 9, 5, 6, 1, 8],
  [8, 9, 5, 2, 6, 1, 4, 7, 3],
  [6, 1, 4, 3, 8, 7, 2, 9, 5]],
[[9, 1, 4, 3, 5, 2, 6, 7, 8],
  [7, 2, 6, 1, 9, 8, 4, 3, 5],
  [5, 3, 8, 4, 6, 7, 9, 1, 2],
  [1, 7, 2, 6, 8, 3, 5, 9, 4],
  [8, 6, 9, 7, 4, 5, 1, 2, 3],
  [4, 5, 3, 9, 2, 1, 8, 6, 7],
  [6, 8, 5, 2, 3, 9, 7, 4, 1],
  [3, 9, 7, 8, 1, 4, 2, 5, 6],
  [2, 4, 1, 5, 7, 6, 3, 8, 9]],
[[4, 3, 7, 8, 9, 6, 1, 5, 2],
  [6, 5, 2, 1, 7, 4, 8, 3, 9],
  [8, 9, 1, 5, 2, 3, 6, 7, 4],
  [2, 1, 6, 3, 5, 9, 7, 4, 8],
  [5, 4, 3, 7, 1, 8, 9, 2, 6],
  [7, 8, 9, 6, 4, 2, 3, 1, 5],
  [1, 2, 4, 9, 6, 7, 5, 8, 3],
  [9, 7, 8, 4, 3, 5, 2, 6, 1],
  [3, 6, 5, 2, 8, 1, 4, 9, 7]],
[[4, 1, 3, 8, 7, 2, 9, 5, 6],
  [5, 6, 7, 1, 3, 9, 4, 8, 2],
  [2, 9, 8, 6, 5, 4, 3, 1, 7],
  [9, 2, 5, 3, 8, 6, 7, 4, 1],
  [6, 3, 1, 9, 4, 7, 5, 2, 8],
  [8, 7, 4, 5, 2, 1, 6, 9, 3],
  [1, 5, 2, 4, 6, 3, 8, 7, 9],
  [3, 8, 9, 7, 1, 5, 2, 6, 4],
  [7, 4, 6, 2, 9, 8, 1, 3, 5]],
[[2, 6, 8, 7, 5, 4, 9, 1, 3],
  [5, 9, 4, 3, 6, 1, 8, 7, 2],
  [3, 1, 7, 2, 9, 8, 5, 6, 4],
  [6, 4, 2, 1, 3, 5, 7, 8, 9],
  [1, 8, 9, 4, 7, 2, 3, 5, 6],
  [7, 5, 3, 6, 8, 9, 2, 4, 1],
  [8, 2, 5, 9, 1, 6, 4, 3, 7],
  [9, 3, 1, 8, 4, 7, 6, 2, 5],
  [4, 7, 6, 5, 2, 3, 1, 9, 8]],
[[5, 6, 2, 3, 4, 1, 9, 7, 8],
  [9, 1, 8, 5, 6, 7, 3, 4, 2],
  [4, 3, 7, 2, 9, 8, 5, 1, 6],
  [3, 4, 9, 7, 8, 2, 1, 6, 5],
  [1, 7, 5, 9, 3, 6, 2, 8, 4],
  [8, 2, 6, 1, 5, 4, 7, 3, 9],
  [7, 5, 4, 6, 1, 9, 8, 2, 3],
  [2, 8, 3, 4, 7, 5, 6, 9, 1],
  [6, 9, 1, 8, 2, 3, 4, 5, 7]],
[[4, 9, 2, 8, 1, 3, 7, 6, 5],
  [1, 7, 3, 9, 5, 6, 8, 4, 2],
  [8, 6, 5, 7, 2, 4, 3, 1, 9],
  [2, 4, 8, 3, 6, 5, 9, 7, 1],
  [6, 5, 7, 1, 4, 9, 2, 3, 8],
  [9, 3, 1, 2, 7, 8, 4, 5, 6],
  [5, 8, 9, 6, 3, 7, 1, 2, 4],
  [3, 1, 6, 4, 9, 2, 5, 8, 7],
  [7, 2, 4, 5, 8, 1, 6, 9, 3]],
[[9,8,4,5,7,6,2,1,3],
 [5,1,3,4,8,2,9,6,7],
 [7,2,6,1,3,9,5,4,8],
 [6,3,1,9,4,7,8,5,2],
 [4,9,5,2,6,8,3,7,1],
 [8,7,2,3,5,1,6,9,4],
 [2,5,7,6,1,3,4,8,9],
 [3,6,8,7,9,4,1,2,5],
 [1,4,9,8,2,5,7,3,6]],
[[7,5,8,1,6,4,9,2,3],
 [6,3,9,5,2,8,1,4,7],
 [4,1,2,3,7,9,5,6,8],
 [1,8,7,6,3,2,4,5,9],
 [2,4,3,8,9,5,7,1,6],
 [5,9,6,4,1,7,3,8,2],
 [8,7,1,9,4,6,2,3,5],
 [9,6,4,2,5,3,8,7,1],
 [3,2,5,7,8,1,6,9,4]],
[[7,2,4,6,9,8,5,3,1],
 [8,5,1,3,4,7,6,2,9],
 [6,3,9,1,2,5,8,4,7],
 [4,9,3,7,8,2,1,6,5],
 [1,7,5,9,6,3,2,8,4],
 [2,6,8,5,1,4,9,7,3],
 [3,4,6,8,5,9,7,1,2],
 [5,8,7,2,3,1,4,9,6],
 [9,1,2,4,7,6,3,5,8]],
[[5,7,2,3,1,8,4,6,9],
 [4,3,9,7,6,2,8,5,1],
 [8,6,1,5,9,4,3,7,2],
 [1,9,7,8,2,3,5,4,6],
 [3,2,5,6,4,1,9,8,7],
 [6,8,4,9,5,7,1,2,3],
 [2,1,6,4,3,5,7,9,8],
 [9,5,8,1,7,6,2,3,4],
 [7,4,3,2,8,9,6,1,5]],
[[2,9,3,6,1,5,4,8,7],
 [1,7,8,2,3,4,6,9,5],
 [4,5,6,9,7,8,2,1,3],
 [5,3,4,1,6,7,9,2,8],
 [6,2,7,8,4,9,5,3,1],
 [8,1,9,5,2,3,7,4,6],
 [9,4,5,3,8,6,1,7,2],
 [7,8,1,4,5,2,3,6,9],
 [3,6,2,7,9,1,8,5,4]],
[[2,5,1,4,8,7,9,3,6],
 [3,7,4,6,5,9,8,1,2],
 [8,6,9,3,2,1,7,5,4],
 [9,3,5,1,4,8,2,6,7],
 [1,2,8,7,6,5,4,9,3],
 [6,4,7,2,9,3,5,8,1],
 [7,9,3,8,1,4,6,2,5],
 [5,1,6,9,7,2,3,4,8],
 [4,8,2,5,3,6,1,7,9]],
[[5,1,8,4,2,7,3,9,6],
 [3,6,9,5,8,1,2,4,7],
 [7,2,4,6,3,9,5,8,1],
 [9,3,1,8,5,4,6,7,2],
 [8,4,2,7,1,6,9,5,3],
 [6,7,5,3,9,2,8,1,4],
 [1,8,7,9,6,3,4,2,5],
 [4,9,6,2,7,5,1,3,8],
 [2,5,3,1,4,8,7,6,9]],
[[5,9,6,4,7,2,1,8,3],
 [8,2,3,6,9,1,4,5,7],
 [4,1,7,5,8,3,2,9,6],
 [2,3,5,7,1,6,9,4,8],
 [7,8,1,9,3,4,6,2,5],
 [6,4,9,2,5,8,3,7,1],
 [3,7,8,1,2,9,5,6,4],
 [9,5,4,3,6,7,8,1,2],
 [1,6,2,8,4,5,7,3,9]],
[[9,7,5,2,6,8,3,1,4],
 [3,4,2,7,9,1,5,8,6],
 [1,6,8,4,3,5,7,9,2],
 [6,9,1,3,8,4,2,7,5],
 [5,2,3,6,1,7,9,4,8],
 [7,8,4,5,2,9,1,6,3],
 [4,3,6,9,7,2,8,5,1],
 [8,5,9,1,4,3,6,2,7],
 [2,1,7,8,5,6,4,3,9]],
[[9,7,4,5,2,1,6,3,8],
 [2,6,1,4,3,8,5,9,7],
 [8,5,3,6,7,9,1,4,2],
 [6,9,8,1,4,7,2,5,3],
 [3,4,5,2,9,6,7,8,1],
 [1,2,7,3,8,5,9,6,4],
 [4,8,6,7,5,2,3,1,9],
 [5,3,2,9,1,4,8,7,6],
 [7,1,9,8,6,3,4,2,5]],
[[5,3,7,1,9,6,4,2,8],
 [8,9,1,5,2,4,3,6,7],
 [4,6,2,8,3,7,5,1,9],
 [7,1,3,6,4,9,8,5,2],
 [9,5,4,2,1,8,6,7,3],
 [2,8,6,3,7,5,9,4,1],
 [3,7,5,9,6,1,2,8,4],
 [6,4,9,7,8,2,1,3,5],
 [1,2,8,4,5,3,7,9,6]],
[[9,5,4,3,7,2,8,6,1],
 [6,2,8,4,1,5,3,9,7],
 [7,3,1,8,6,9,2,4,5],
 [8,7,2,6,3,1,4,5,9],
 [1,4,5,2,9,8,7,3,6],
 [3,6,9,5,4,7,1,2,8],
 [5,1,6,7,2,3,9,8,4],
 [2,8,7,9,5,4,6,1,3],
 [4,9,3,1,8,6,5,7,2]],
[[7,3,8,5,9,6,2,4,1],
 [6,5,4,7,1,2,9,8,3],
 [2,9,1,4,8,3,5,7,6],
 [3,1,7,6,4,9,8,2,5],
 [4,6,5,3,2,8,7,1,9],
 [9,8,2,1,7,5,3,6,4],
 [5,7,1,8,6,1,4,9,2],
 [8,2,6,9,3,4,1,5,7],
 [1,4,9,2,5,7,6,3,8]],
[[2,5,4,1,7,6,8,9,3],
 [1,9,6,4,3,8,7,2,5],
 [9,7,8,9,2,5,1,6,4],
 [7,8,9,5,1,2,3,4,6],
 [5,4,1,3,6,9,2,7,8],
 [6,3,2,8,4,7,5,1,9],
 [8,6,3,7,9,1,4,5,2],
 [4,2,7,6,5,3,9,8,1],
 [9,1,5,2,8,4,6,3,7]],
[[7,5,4,3,9,6,2,8,1],
 [3,6,2,1,7,8,4,9,5],
 [8,9,1,4,2,5,3,6,7],
 [6,1,9,5,4,2,7,3,8],
 [2,4,7,8,1,3,6,5,9],
 [5,3,8,7,6,9,1,2,4],
 [4,8,5,2,3,7,9,1,6],
 [9,7,3,6,8,1,5,4,2],
 [1,2,6,9,5,4,8,7,3]],
[[4,8,2,6,9,1,5,7,3],
 [6,1,5,7,3,8,9,2,4],
 [3,9,7,5,4,2,8,6,1],
 [2,7,6,9,1,4,3,8,5],
 [8,4,9,3,7,5,2,1,6],
 [1,5,3,8,2,6,4,9,7],
 [9,6,8,1,5,3,7,4,2],
 [7,3,4,2,6,9,1,5,8],
 [5,2,1,4,8,7,6,3,9]],
[[8,4,3,5,2,7,1,6,9],
 [9,5,1,3,6,8,2,4,7],
 [7,2,6,4,1,9,8,5,3],
 [4,6,8,7,3,1,9,2,5],
 [5,1,2,8,9,6,3,7,4],
 [3,7,9,2,4,5,6,1,8],
 [1,9,5,6,8,4,7,3,2],
 [2,8,4,1,7,3,5,9,6],
 [6,3,7,9,5,2,4,8,1]],
[[6,3,2,7,5,8,1,9,4],
 [4,9,8,1,3,6,2,5,7],
 [1,5,7,4,2,9,8,3,6],
 [7,6,1,8,4,5,9,2,3],
 [3,8,4,2,9,7,5,6,1],
 [9,2,5,3,6,1,4,7,8],
 [8,1,9,5,7,3,6,4,2],
 [5,4,3,6,8,2,7,1,9],
 [2,7,6,9,1,4,3,8,5]],
[[7,3,6,5,9,4,8,2,1],
 [1,4,9,3,8,2,5,6,7],
 [5,8,2,6,1,7,4,3,9],
 [4,2,1,9,7,3,6,8,5],
 [6,7,5,4,2,8,9,1,3],
 [3,9,8,1,6,5,2,7,4],
 [2,1,3,8,4,9,7,5,6],
 [9,5,7,2,3,6,1,4,8],
 [8,6,4,7,5,1,3,9,1]],
[[9,7,4,2,6,8,1,3,5],
 [8,5,2,3,9,1,7,4,6],
 [6,1,3,7,5,4,9,8,2],
 [5,6,7,4,1,2,3,9,8],
 [4,3,9,5,8,7,2,6,1],
 [2,8,1,6,3,9,4,5,7],
 [3,2,6,1,4,5,8,7,9],
 [1,9,5,8,7,3,6,2,4],
 [7,4,8,9,2,6,5,1,3]],
[[5,1,3,8,7,4,2,9,6],
 [9,7,6,2,5,3,4,8,1],
 [4,8,2,9,1,6,7,5,3],
 [7,3,1,4,6,5,9,2,8],
 [8,9,5,7,2,1,6,3,4],
 [2,6,4,3,8,9,5,1,7],
 [3,4,7,5,9,8,1,6,2],
 [6,5,8,1,4,2,3,7,9],
 [1,2,9,6,3,7,8,4,5]],
[[1,6,3,4,2,5,8,7,9],
 [2,8,4,9,7,3,1,5,6],
 [9,7,5,6,8,1,4,3,2],
 [5,1,6,7,3,9,2,4,8],
 [7,4,2,5,1,8,6,9,3],
 [3,9,8,2,6,4,7,1,5],
 [4,3,1,8,5,6,9,2,7],
 [6,5,7,1,9,2,3,8,4],
 [8,2,9,3,4,7,5,6,1]],
[[1,9,8,4,5,3,7,2,6],
 [7,4,2,8,1,6,5,3,9],
 [3,5,6,7,2,9,1,8,4],
 [5,2,4,6,9,7,8,1,3],
 [8,6,3,5,4,1,9,7,2],
 [9,1,7,3,8,2,4,6,5],
 [4,8,1,2,6,5,3,9,7],
 [2,7,5,9,3,8,6,4,1],
 [6,3,9,1,7,4,2,5,8]],
[[1,3,4,2,6,7,5,8,9],
 [5,2,9,3,4,8,7,1,6],
 [6,8,7,5,1,9,2,4,3],
 [9,1,5,6,8,2,4,3,7],
 [2,4,3,7,9,5,1,6,8],
 [4,9,1,8,5,3,6,7,2],
 [4,7,6,9,2,1,3,5,4],
 [8,7,6,9,2,1,3,5,4],
 [3,5,2,4,7,6,8,9,1]]
]

sudokus4x4 = [
[[1, 2, 3, 4],
[3, 4, 1, 2],
[2, 3, 4, 1],
[4, 1, 2, 3]],
[[4, 3, 2, 1],
[2, 1, 4, 3],
[1, 2, 3, 4],
[3, 4, 1, 2]],
[[1, 2, 4, 3],
[4, 3, 1, 2],
[2, 1, 3, 4],
[3, 4, 2, 1]],
[[1, 4, 3, 2],
[3, 2, 4, 1],
[4, 1, 2, 3],
[2, 3, 1, 4]],
[[1, 2, 4, 3],
[4, 3, 1, 2],
[3, 1, 2, 4],
[2, 4, 3, 1]],
[[4, 3, 2, 1],
 [1, 2, 3, 4],
 [2, 1, 4, 3],
 [3, 4, 1, 2]],
[[2, 1, 4, 3],
 [3, 4, 1, 2],
 [4, 3, 2, 1],
 [1, 2, 3, 4]],
[[1, 2, 3, 4],
 [3, 4, 1, 2],
 [4, 3, 2, 1],
 [2, 1, 4, 3]],
[[2, 1, 4, 3],
 [4, 3, 2, 1],
 [3, 2, 1, 4],
 [1, 4, 3, 2]],
[[2, 4, 3, 1],
 [3, 1, 2, 4],
 [4, 3, 1, 2],
 [1, 2, 4, 3]]
]

#Variables globales
dicc_col = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
coordenadas_elegidas_glob = []
desp = 43 #Desplazamiento horizontal del cursor en la pantalla
errores = 0
#Limpiar pantalla
def clearScreen():
	os.system('cls')

#Función que valida si es posible insertar un valor e en la posición x,y de la matriz M
def valido(x, y, e, M):
    n = len(M)
    f = int(n**0.5) #cantidad de columnas o filas de un cuadrante
    fila = M[y] #lista con todos los valores que esten en la fila 'y'
    columna = [M[fil][x] for fil in range(n)] #lista con todos los valres en la columna 'x'
    n_cuad_x = x//f
    n_cuad_y = y//f
    cuad = []
    for j in range(n_cuad_y*f, f*(n_cuad_y+1)):
        for i in range(n_cuad_x*f, f*(n_cuad_x+1)):
            cuad.append(M[j][i])
    if (e in fila) or (e in columna) or (e in cuad):
        return False
    else:
        return True

#función principal
def main():
    dificultad = 4
    while True:
        op = menu()
        if op == '1':
            dificultad = elegirDificultad()
        elif op == '2':
            jugar(dificultad)
        elif op == "3":
            #print(Fore.YELLLOW)
            print(Cursor.FORWARD(desp) + "¿De qué tipo de juego desea ver la tabla?")
            print(Fore.GREEN)
            print(Cursor.FORWARD(desp) + "1) 4x4 - Fácil")
            print(Cursor.FORWARD(desp) + "2) 4x4 - Medio")
            print(Cursor.FORWARD(desp) + "3) 9x9 - Fácil")
            print(Cursor.FORWARD(desp) + "4) 9x9 - Medio")
            print(Cursor.FORWARD(desp) + "5) 9x9 - Difícil")
            #print(Fore.YELLLOW)
            while True:
                opcion = int(input("Ingrese su opción: "))
                if opcion in [1, 2, 3, 4, 5]:
                    break
                print(Fore.RED + "ERROR. Opción no válida." + Fore.YELLOW)
            if opcion == 1:
                ver_puntajes(4, 1)
            elif opcion == 2:
                ver_puntajes(4, 2)
            elif opcion == 3:
                ver_puntajes(9, 1)
            elif opcion == 4:
                ver_puntajes(9, 2)
            elif opcion == 5:
                ver_puntajes(9, 3)
            print(Fore.YELLOW + "Presione enter para continuar..." + Style.RESET_ALL)
            input()
        elif op == '4':
            nombre = input(Fore.YELLOW + "Ingrese su usuario, por favor: " + Style.RESET_ALL)
            cargarpartida(nombre)
        elif op == '5':
            exit()

## Menu de opciones ##
def menu():
    clearScreen()
    print("\n"*8)
    print(Cursor.FORWARD(desp) +  "-------------------------------")
    print(Cursor.FORWARD(desp) +  "|           SUDOKU            |")
    print(Cursor.FORWARD(desp) +  "-------------------------------")
    print(Fore.GREEN)
    print(Cursor.FORWARD(desp) + "1) Elegir dificultad")
    print(Cursor.FORWARD(desp) + "2) Jugar una partida")
    print(Cursor.FORWARD(desp) + "3) Ver récord de puntajes")
    print(Cursor.FORWARD(desp) + "4) Cargar una partida")
    print(Cursor.FORWARD(desp) + "5) Salir")
    while True:
        print(Cursor.FORWARD(desp) + Fore.YELLOW + "Eliga una opcion ( )" + Style.RESET_ALL)
        op = input(Cursor.UP(1) + Cursor.FORWARD(desp+18))
        if op in ["1", "2", "3", "4", "5"]:
            break
        else:
            print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Opción no válida" + Style.RESET_ALL)
    print(Style.RESET_ALL)
    clearScreen()
    return op

#Función para elegir dificultad
def elegirDificultad():
    clearScreen()
    print("\n"*7)
    print(Fore.GREEN)
    print(Cursor.FORWARD(desp) + "1) 4x4")
    print(Cursor.FORWARD(desp) + "2) 9x9")
    while True:
        print(Cursor.FORWARD(desp) + Fore.YELLOW + "Ingrese el tamaño del tablero ( )" + Style.RESET_ALL)
        n = input(Cursor.UP(1) + Cursor.FORWARD(desp + 31))
        if n in ["1", "2"]:
            break
        else:
            print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Opción no válida" + Style.RESET_ALL)
    print(Style.RESET_ALL)
    if n == "1":
        return 4
    elif n == "2":
        return 9

def showMatrix(M):
    clearScreen()
    print()
    x = len(M)
    factor = int(x**0.5)
    if x == 4:
        print(Cursor.FORWARD(desp) + Fore.YELLOW +  "  A B   C D" + Style.RESET_ALL)
    elif x == 9:
        print(Cursor.FORWARD(desp) + Fore.YELLOW + "  A B C   D E F   G H I" + Style.RESET_ALL)
    for j in range(x):
        for i in range(x):
            numero = M[j][i]
            if [i, j] in coordenadas_elegidas_glob:
                numero = Fore.RED + str(M[j][i]) + Style.RESET_ALL
            if ((i+1)%(factor) == 0) and (i != x-1):
                print(f"{numero} |", end=" ")
            elif (i == 0):
                print(Cursor.FORWARD(desp) + Fore.YELLOW + f"{j+1}" + Style.RESET_ALL + f" {numero}", end=" ")
            else:
                print(f"{numero}", end=" ")
        if ((j+1)%(factor) == 0) and (j != x-1):
            print()
            if x ==4:
                print(Cursor.FORWARD(desp) + "  " + "-" * (2*(x+1) -1))
            elif x == 9:
                print(Cursor.FORWARD(desp) + " " +  "-" * (2*(x+1) +1))
        else:
            print()
    print()

def jugar(n):
    print("\n" * 7)
    print(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese la dificultad: ")
    print(Cursor.FORWARD(desp) + "Facil (1)")
    print(Cursor.FORWARD(desp) + "Medio (2)")
    print(Cursor.FORWARD(desp) + "Dificil (3) (solo disponible para tablero de 9x9)")
    while True:
        dificultad = int(input(Cursor.FORWARD(desp) + Fore.YELLOW + "Opción: " + Style.RESET_ALL))
        if n == 4:
            if dificultad in [1, 2]:
                break
        elif n == 9:
            if dificultad in [1, 2, 3]:
                break
        print(Fore.RED + "ERROR. Opción no válida." + Style.RESET_ALL)

    M = sudoku(n, dificultad)
    nivel = len(M)
    inicio = time.time()
    clearScreen()
    print("\n" * 9)
    nombre = input(Cursor.FORWARD(desp) + Fore.YELLOW + "Ingrese el nombre con el que se registrará, por favor: " + Style.RESET_ALL)
    while not completado(M):
        global errores
        clearScreen()
        showMatrix(M)
        print(Cursor.FORWARD(desp) + "Qué desea hacer a continuación?")
        print(Cursor.FORWARD(desp) + "1) Ingresar un valor")
        print(Cursor.FORWARD(desp) + "2) Borrar un valor")
        print(Cursor.FORWARD(desp) + "3) Guardar e ir al menú principal")

        while True:
            print(Cursor.FORWARD(desp) + Fore.YELLOW + "Opción: ( )" + Style.RESET_ALL)
            op1 = input(Cursor.UP(1) + Cursor.FORWARD(desp + 9))
            if op1 in ["1", "2", "3"]:
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Opción no válida" + Style.RESET_ALL)
        if op1 == "1":
            M = ingresar_valor(M)
        elif op1 == "2":
            M = borrar_valor(M)
        elif op1 == "3":
            guardarpartida(nombre, M)
            coordenadas_elegidas_glob = []
            main()
    showMatrix(M)
    final = time.time()
    print(Cursor.FORWARD(desp) + Fore.GREEN + "FELICIDADES!! Ganaste!!")
    tiempo = round((final - inicio), 2)
    print(Cursor.FORWARD(desp) + f"Tiempo utilizado: {tiempo} s.")

    if nivel == 4:
        if tiempo < 60:
            tiempo = 60
        ratio = 6000
    elif nivel == 9:
        if tiempo < 300:
            tiempo = 300
        ratio = 30000
    puntos = int(round(ratio / (tiempo * (errores + 1)) , 0))
    guardarpuntaje(nombre, puntos, n, dificultad)
    puntaje = Fore.YELLOW + str(puntos) + Fore.GREEN

    print(Cursor.FORWARD(desp) + f"Puntaje: {puntaje} de 1000 posibles")
    print(Cursor.FORWARD(desp) + "Presione ENTER para continuar" + Style.RESET_ALL)

    coordenadas_elegidas_glob = []
    errores = 0

    input()

def completado(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[j][i] == "_":
                return False
    return True

def ingresar_valor(M):
    global errores
    while True:
        while True:
            col_letra = input(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese la columna en la que quiere insertar un valor: " + Style.RESET_ALL).upper()
            if ((len(M) == 9) and (col_letra in ["A", "B", "C", "D", "E", "F", "G", "H", "I"])) or (len(M) == 4) and (col_letra in ["A", "B", "C", "D"]):
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. La columna {col_letra} no existe." + Style.RESET_ALL)
                errores += 1
        col = dicc_col[col_letra]
        while True:
            while True:
                try:
                    fil =int(input(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese la fila en la que quiere insertar un valor: " + Style.RESET_ALL)) - 1
                    break
                except:
                    print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Fila no válida")
                    errores += 1
            if ((fil in range(9)) and (len(M) == 9)) or ((fil in range(4)) and (len(M) == 4)):
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. La fila {fil +1} no existe." + Style.RESET_ALL)
                errores += 1
        if M[fil][col] == "_":
            break
        else:
            print(Cursor.FORWARD(desp) + Fore.RED + "Ya existe un valor en esa casilla, intente con otra posición." + Style.RESET_ALL)
            errores += 1
    while True:
        while True:
            try:
                valor = int(input(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese el valor a colocar: " + Style.RESET_ALL))
                break
            except:
                print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. Valor no válido" + Style.RESET_ALL)
                errores += 1
        if ((valor in range(1, 10)) and (len(M) == 9)) or ((valor in range(1, 5)) and (len(M) == 4)):
            break
        else:
            print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Valor no válido." + Style.RESET_ALL)
            errores += 1
    while not valido(col, fil, valor, M):
        print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. No es posible colocar {valor} en la posición {col_letra}{fil+1}" + Style.RESET_ALL)

        while True:
            col_letra = input(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese la columna en la que quiere insertar un valor: " + Style.RESET_ALL).upper()
            if ((len(M) == 9) and (col_letra in ["A", "B", "C", "D", "E", "F", "G", "H", "I"])) or (len(M) == 4) and (col_letra in ["A", "B", "C", "D"]):
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. La columna {col_letra} no existe." + Style.RESET_ALL)
                errores += 1
        col = dicc_col[col_letra]
        while True:
            while True:
                try:
                    fil =int(input(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese la fila en la que quiere insertar un valor: " + Style.RESET_ALL)) - 1
                    break
                except:
                    print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Fila no válida" + Style.RESET_ALL)
                    errores += 1
            if ((fil in range(9)) and (len(M) == 9)) or ((fil in range(4)) and (len(M) == 4)):
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. La columna {col_letra} no existe." + Style.RESET_ALL)
                errores += 1
        while True:
            while True:
                try:
                    valor = int(input(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese el valor a colocar: " + Style.RESET_ALL))
                    break
                except:
                    print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. Valor no válido" + Style.RESET_ALL)
                    errores += 1
            if ((valor in range(1, 10)) and (len(M) == 9)) or ((valor in range(1, 5)) and (len(M) == 4)):
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Valor no válido." + Style.RESET_ALL)
                errores += 1
    M[fil][col] = valor
    return M

def borrar_valor(M):
    global errores
    while True:
        while True:
            col_letra = input(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese la columna en la que quiere borra el valor: " + Style.RESET_ALL).upper()
            if ((len(M) == 9) and (col_letra in ["A", "B", "C", "D", "E", "F", "G", "H", "I"])) or (len(M) == 4) and (col_letra in ["A", "B", "C", "D"]):
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. La columna {col_letra} no existe." + Style.RESET_ALL)
                errores += 1
        col = dicc_col[col_letra]
        while True:
            while True:
                try:
                    fil =int(input(Cursor.FORWARD(desp) + Fore.GREEN + "Ingrese la fila en la que quiere borrar el valor: " + Style.RESET_ALL)) - 1
                    break
                except:
                    print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Fila no válida" + Style.RESET_ALL)
                    errores += 1
            if ((fil in range(9)) and (len(M) == 9)) or ((fil in range(4)) and (len(M) == 4)):
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. La fila {fil+1} no existe." + Style.RESET_ALL)
                errores += 1
        if [col, fil] not in coordenadas_elegidas_glob:
            break
        else:
            print(Cursor.FORWARD(desp) + Fore.RED + f"ERROR. No es posible borrar el valor en la posición {col_letra}{fil+1}." + Style.RESET_ALL)
            errores += 1
    M[fil][col] = "_"
    return M

def sudoku(n, dificultad):
    global coordenadas_elegidas_glob
    coordenadas_elegidas_glob = []
    cant_mostrar = 0
    if n == 4:
        if dificultad == 1:
            cant_mostrar = 2 #muestra cierta cantidad de números por cuadrante
        elif dificultad == 2:
            cant_mostrar == 1
        M2 = choice(sudokus4x4) #seleccionar un sudoku aleatorio de la lista sudokus4x4
    elif n == 9:
        if dificultad == 1:
            cant_mostrar = 4 #muestra 3 valores por cuadrante si es un sudoku de 9x9
        elif dificultad == 2:
            cant_mostrar = 3
        elif dificultad == 3:
            cant_mostrar = 2
        M2 = choice(sudokus9x9) #seleccionar un sudoku aleatorio de la lista sudokus9x9

    factor = int(n**0.5)

    M = [["_" for _ in range(n)] for _ in range(n)] #Una matriz de dimensiones n x n donde todos los elementos son "_"

    for j in range(factor):
        for i in range(factor):
            posible_x = [num for num in range(i*factor, factor*(i+1))] #Posibles coordenadas x en el cuadrante
            posible_y = [num for num in range(j*factor, factor*(j+1))] #posibles coordenadas y en el cuadrante
            coordenadas_elegidas = []
            x_elegido = choice(posible_x)
            y_elegido = choice(posible_y)
            coordenadas_elegidas.append([x_elegido, y_elegido])
            while len(coordenadas_elegidas)<cant_mostrar:
                x_elegido = choice(posible_x)
                y_elegido = choice(posible_y)
                if [x_elegido, y_elegido] not in coordenadas_elegidas:
                    coordenadas_elegidas.append([x_elegido, y_elegido])
            for coordenada in coordenadas_elegidas:
                M[coordenada[1]][coordenada[0]] = M2[coordenada[1]][coordenada[0]]
                coordenadas_elegidas_glob.append(coordenada)
    return M

####FUNCIONES PARA LA PARTE 2 DEL PROYECTO#####

def ver_puntajes(tamaño, dificultad):
    filename = ""
    if tamaño == 4:
        if dificultad == 1:
            filename = "4x4facil.json"
        elif dificultad == 2:
            filename = "4x4medio.json"
    elif tamaño == 9:
        if dificultad == 1:
            filename = "9x9facil.json"
        elif dificultad == 2:
            filename = "9x9medio.json"
        elif dificultad == 3:
            filename = "9x9dificil.json"

    with open(filename) as file:
        data = json.load(file)
        matriz = []
        for key in data:
            matriz.append([key, data[key]])
        matriz= sorted(matriz, key = lambda matriz: matriz[1], reverse = True)

    datos = {"Usuario": [x[0] for x in matriz], "Puntaje":[x[1] for x in matriz]}

    dataframe = pd.DataFrame(data=datos, index = [i for i in range(1, len(matriz) + 1)])
    print(Fore.GREEN)
    print(dataframe)
    print(Style.RESET_ALL)

def guardarpuntaje(nombre, puntaje, tamaño, dificultad):
    filename = ""
    if tamaño == 4:
        if dificultad == 1:
            filename = "4x4facil.json"
        elif dificultad == 2:
            filename = "4x4medio.json"
    elif tamaño == 9:
        if dificultad == 1:
            filename = "9x9facil.json"
        elif dificultad == 2:
            filename = "9x9medio.json"
        elif dificultad == 3:
            filename = "9x9dificil.json"

    new_data = OrderedDict({nombre: puntaje})
    new_data.update(json.load(open(filename), object_pairs_hook=OrderedDict))
    json.dump(new_data, open(filename, "w"))

    with open(filename, 'r') as file:
        dic = json.load(file)

        dic2 = {}

        for key in dic:
            if key == nombre:
                dic2[nombre] = puntaje
            else:
                dic2[key] = dic[key]

    with open(filename, 'w') as file:
        json.dump(dic2, file, indent=4)

def guardarpartida(nombre, partida):
    filename = "partidas_guardadas.json"
    new_data = OrderedDict({nombre: partida})
    new_data.update(json.load(open(filename), object_pairs_hook=OrderedDict))
    json.dump(new_data, open(filename, "w"))

    with open(filename, 'r') as file:
        dic = json.load(file)
        dic2 = {}
        for key in dic:
            if key == nombre:
                dic2[nombre] = partida
            else:
                dic2[key] = dic[key]

    with open(filename, 'w') as file:
        json.dump(dic2, file)

def cargarpartida(nombre):
    with open("partidas_guardadas.json", "r") as file:
        datos = json.load(file)
        M = datos[nombre]
    while not completado(M):
        global errores
        clearScreen()
        showMatrix(M)
        print(Cursor.FORWARD(desp) + "Qué desea hacer a continuación?")
        print(Cursor.FORWARD(desp) + "1) Ingresar un valor")
        print(Cursor.FORWARD(desp) + "2) Borrar un valor")
        print(Cursor.FORWARD(desp) + "3) Guardar e ir al menú principal")

        while True:
            print(Cursor.FORWARD(desp) + Fore.YELLOW + "Opción: ( )" + Style.RESET_ALL)
            op1 = input(Cursor.UP(1) + Cursor.FORWARD(desp + 9))
            if op1 in ["1", "2", "3"]:
                break
            else:
                print(Cursor.FORWARD(desp) + Fore.RED + "ERROR. Opción no válida" + Style.RESET_ALL)
        if op1 == "1":
            M = ingresar_valor(M)
        elif op1 == "2":
            M = borrar_valor(M)
        elif op1 == "3":
            guardarpartida(nombre, M)
            coordenadas_elegidas_glob = []
            main()
    print(Cursor.FORWARD(desp) + Fore.YELLOW + "¡FELICIDADES! Ganaste!!" + Style.RESET_ALL)

main()
