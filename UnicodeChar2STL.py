#!/usr/bin/env python
# coding=utf-8

import full_ddump
import os

if __name__ == '__main__':
    FONT = 'SimSun.ttf'
    MODULE = 'SimSun'

    # scad = full_ddump.ddump_char(FONT, MODULE, u'车')
    scad = full_ddump.ddump_string(FONT, MODULE, u'车库咖啡')
    open('test.scad', 'w').write(scad)

    # CMD_OPENSCAD = '/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD'
    # os.system(CMD_OPENSCAD + ' -o test.stl test.scad')
