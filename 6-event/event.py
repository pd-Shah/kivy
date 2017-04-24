'''
No doubt that fixed coordinates are the most flexible way of organizing elements in
an n-dimensional space; however, it is very time-consuming. Instead, Kivy provides a
good set of layouts instead, which facilitate the work of organizing widgets. A Layout
is a Widget subclass that implements different strategies to organize embedded
widgets. For example, one strategy could be organizing widgets in a grid ( GridLayout ).
Let's start with a simple FloatLayout example. It works very similar to the way
we organize widgets directly inside another Widget , except that now we can use
proportional coordinates (proportions of the total size of the window) rather than
fixed coordinates (exact pixels). This means that we don't need the calculations we
did in the previous section with self and root . The following is the Python code:
FloatLayout
    This layout organizes the widgets with proportional coordinates with
the size_hint and pos_hint properties. The values are numbers
between 0 and 1 indicating a proportion to the window size.
Relative Layout:
    This layout operates in the same way as FloatLayout does, but the
positioning properties (pos, x, center_x, right, y, center_y, and
top) are relative to the Layout size and not the window size.
GridLayout:
    This layout organizes widgets in a grid. You have to specify at least one
of the two properties: cols (for columns) or rows (for rows).
BoxLayout:
    This layout organizes widgets in one row or one column depending
whether the value of property orientation is horizontal or vertical.
StackLayout:
    This layout is similar to BoxLayout but it goes to the next row or column
when it runs out of space. In this layout, there is more flexibility to set
the orientation. For example, 'rl-bt' organizes the widgets in right-
to-left and bottom-to-top order. Any combination of lr (left to right), rl
(right to left), tb (top to bottom), and bt (bottom to top) is allowed.
Anchor Layout:
    This layout organizes the widgets to a border or to the center. The
anchor_x property indicates the x position (left, center or right),
whereas anchor_y indicates the y position (top, center or bottom)
ScatterLayout:
    works similar to RelativeLayout
but it allows multitouch gesturing for rotating, scaling, and translating. It is
slightly different in its implementation so we will review it later. The Kivy API
( http://kivy.org/docs/api-kivy.html ) offers a detailed explanation and good
examples on each of them.
If we are using a Layout instance, can we force the use of fixed values? Yes, but
there can be conflicts if we are not careful with the properties we use. If we use any
Layout , then pos_hint and size_hint will have the priority.
If we want to use fixed positioning properties ( pos , x , center_x , right , y , center_y , and top ), we have to
ensure that we are not using the pos_hint property.
Secondly, if we want to use the size , height , or width properties, we need to give a None value to the size_hint
axis we want to use with the absolute values.
For example, size_hint: (None,.10) allows using the height property, but it keeps the width as 10 percent of the
windows size.
'''

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
class EventApp(App):
    pass

class EventForm(AnchorLayout):

    def Print(self):
        print("event")

if __name__=="__main__":
    EventApp().run()
