import pynput
import os
import keyboard

mouse=pynput.mouse.Controller()
mouse.position=(5,5)
mouse.position=(1600,900)
tem=mouse.position[0]
mouse.click(pynput.mouse.Button.left,1)
print(mouse.position)


"""
def func(self, x):
    global keynames, keytype, ls
    ls = self.getinfos(self.filename)
    for item in ls:
        item[6] = item[6].split("+")
        item[6].sort()
        item[6] = "+".join(item[6])
    dict1 = {item[6]: (item[3], item[4]) for item in ls}
    keynames.append(x.name)
    keytype.append(x.event_type)
    dn = keytype.count("down")
    un = keytype.count("up")
    if un == 1 and dn > 0:
        keys = list(set(keynames))
        keys.sort()
        keys = "+".join(keys)
        if keys in dict1.keys():
            position = dict1[keys]
            mouse = pynput.mouse.Controller()
            position1 = mouse.position
            mouse.click(int(position[0]), int(position[1]))
            mouse.move(position1[0], position1[1])
        keynames = []
        keytype = []
    if dn == 0 and un > 0:
        keynames = []
        keytype = []
"""