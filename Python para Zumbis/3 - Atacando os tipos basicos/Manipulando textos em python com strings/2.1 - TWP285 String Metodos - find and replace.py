Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> s = 'um tigre, dois tigres, tres tigres'
>>> s.find('tigre')
3
>>> s.find('tigre', 4)
15
>>> s.find('tigre', 16)
28
>>> s.replace('tigre', 'gato')
'um gato, dois gatos, tres gatos'
>>> s
'um tigre, dois tigres, tres tigres'
>>> s = s.replace('tigre', 'gato')
>>> s
'um gato, dois gatos, tres gatos'
>>> 
