#cell1
import ipywidgets.widgets as widgets

controller = widgets.Controller(index=0)  # replace with index of your controller

display(controller)





#cell2
from jetbot import Robot
import traitlets

robot = Robot()


left_link = traitlets.dlink((controller.axes[1], 'value'), (robot.left_motor, 'value'), transform=lambda x: -x*0.25)
right_link = traitlets.dlink((controller.axes[3], 'value'), (robot.right_motor, 'value'), transform=lambda x: -x*0.25)