# Alarm Clock

<p align="center">
  <img src="https://user-images.githubusercontent.com/66780299/90952913-a63cfa80-e467-11ea-84a6-655f6826958e.PNG" alt="Alarm Clock interface image"/>
</p>

For the GUI, I use Tkinter library. The next libraries are used to work with the time of the computer and thus be able to configure the alarm.

```
from tkinter import *
from tkinter import ttk

import datetime
import time
import winsound
```

To initialize tkinter, we have to create a Tk root widget, which is a window with a title bar and other decoration provided by the window manager:
* .title(): set the title of the window.
* .geometry(): set the size of the window.
* .resizable(): this function has two parameters, which has boolean values, we can allow resizing the window vertically or horizontally.
* .iconphoto(): set the icon of the window.

"Label" widget can containg text and images (in this case, only text). "Entry" widget can collect information from the user. And "Button" widget set buttons for the aplication.

There are three options to put on widgets in Tkinter. I have preferred use .place() since it allows to put elements indicating the position. Its a good option for static interfaces.

There are some functions inside the class:
* set_time(): save the time using f-string formatting.
* alarm(): show the time comes the alarman will wake you up.
* stop_music(): as its name suggests, it stops the music.

If you are reading this and find an error (code or readme), please notify me :)
