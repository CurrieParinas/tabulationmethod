from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('kivy', 'keyboard_mode', 'system')
from kivy.core.window import Window

from random import sample

import kivy
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen

kivy.require('1.9.0')
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager


import tabular
import globalVariables

screen_helper = '''
#:import utils kivy.utils

ScreenManager:
    MainMenu:
        name: 'MainMenu'
    UserInput:
        name: 'Input'
    Results:
        name: 'Results'
    FollowingScreen:
        name: 'FollowingScreen'
    NextTables:
        name: 'NextTables'
    Final:
        name: 'Final'
    

<MainMenu>:
    Widget:
        canvas:
            Color:
                rgba: 220/255, 174/255, 150/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        #title
        Image:
            source: 'mickeyanddonald.png'
            pos_hint: {'center_x': .50, 'center_y': .46}
            size_hint: (.60,.60)

        Label:
            text: "The Quine-McCluskey Technique"
            pos_hint: {'center_x': .505, 'center_y': .84} 
            size_hint: 1, 0.1
            font_size: self.width/20
            font_name:"Minnie"
            color: '#000000'
        Label:
            text: "Tabular Method"
            pos_hint: {'center_x': .52, 'center_y': .775} 
            size_hint: 1, 0.1
            font_size: self.width/40
            font_name:"Minnie"
            color: '#000000'
            
        Button:
            text: "START"
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            pos_hint: {'center_x': .35, 'center_y': .13}
            background_normal: ""

            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Input'

        Button:
            text: "QUIT"
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            pos_hint: {'center_x': .65, 'center_y': .13}
            background_normal: ""

            on_press:
                quit()

<UserInput>:
    Widget:
        canvas:
            Color:
                rgba: 220/255, 174/255, 150/255, 1
            Rectangle:
                size: self.size
                pos: self.pos   
    FloatLayout:
        Image:
            source: 'mickeyandfriends.png'
            pos_hint: {'center_x': .50, 'center_y': .15}
            size_hint: (.35,.35)
        Button:
            text: "Enter minterms:"
            background_color :'#000000'
            size_hint: (.50,.07)
            font_size: self.width/10
            font_name:"Mouse"
            pos_hint: {'center_x': .50, 'center_y': .88}
            background_normal: ""
        Button:
            size_hint: (.50,.07)
            pos_hint: {'center_x': .50, 'center_y': .77}
            background_color :'#FFFFFF'
            background_normal: ""   

        Label:
            text: "Starting variable: "
            size_hint: (.50,.07)
            font_size: self.width/15
            color: '#000000'
            font_name:"Mouse"
            pos_hint: {'center_x': .35, 'center_y': .70}
        Button:
            size_hint: (.24,.07)
            pos_hint: {'center_x': .35, 'center_y': .62}
            background_color :'#FFFFFF'
            background_normal: ""
      
        Label:
            text: "Don't care terms (Optional): "
            size_hint: (.50,.07)
            font_size: self.width/15
            font_name:"Mouse"
            color: '#000000'
            pos_hint: {'center_x': .35, 'center_y': .52}
        Button:
            size_hint: (.24,.07)
            pos_hint: {'center_x': .35, 'center_y': .44}
            background_color :'#FFFFFF'
            background_normal: ""

        Label:
            text: "Number of variables: "
            size_hint: (.50,.07)
            font_size: self.width/15
            font_name:"Mouse"
            color: '#000000'
            pos_hint: {'center_x': .35, 'center_y': .35}
        Button:
            size_hint: (.24,.07)
            pos_hint: {'center_x': .35, 'center_y': .27}
            background_color :'#FFFFFF'
            background_normal: ""
        
        Button:
            text: "SEE RESULTS"
            background_color :'#000000'
            background_normal: ""
            size_hint: (.25,.15)
            font_size: self.width/5
            font_name:"Mouse"
            pos_hint: {'center_x': .75, 'center_y': .55}
            
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Results'
                root.manager.get_screen('Results').ids.final_output.text = root.inputs(variableChoice.text, mintermInput.text, dontCare.text, sizing.text)
                root.manager.get_screen('FollowingScreen').ids.final_output1.text = root.input1(variableChoice.text, mintermInput.text, dontCare.text, sizing.text)
                root.manager.get_screen('NextTables').ids.middle_table.text = root.inputMid(variableChoice.text, mintermInput.text, dontCare.text, sizing.text)
                root.manager.get_screen('Final').ids.final_output2.text = root.input2(variableChoice.text, mintermInput.text, dontCare.text,sizing.text)
        Button:
            text: "RETURN"
            background_color :'#000000'
            background_normal: ""
            font_size: self.width/5
            size_hint: (.25,.15)
            font_name:"Mouse"
            pos_hint: {'center_x': .75, 'center_y': .35}

            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'MainMenu'
                
    
        MDTextField: #Input Minterms text line
            id: mintermInput
            font_size: self.width/13
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            font_name:"Mouse"
            pos_hint:{'center_x': 0.5, 'center_y': 0.77}
            size_hint_x:None
            width:375

        MDTextField: #Starting Var text line
            id: variableChoice
            font_size: self.width/5
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            font_name:"Mouse"
            pos_hint: {'center_x': .35, 'center_y': .62}
            size_hint_x:None
            width:150

        MDTextField: #Don't care
            id: dontCare
            font_size: self.width/5
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            font_name:"Mouse"
            pos_hint: {'center_x': .35, 'center_y': .44}
            size_hint_x:None
            width:150
        
        MDTextField: #Num of var
            id: sizing
            font_size: self.width/5
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            font_name:"Mouse"
            pos_hint: {'center_x': .35, 'center_y': .27}
            size_hint_x:None
            width:150
        
        
             
<Results>:
    Widget:
        canvas:
            Color:
                rgba: 220/255, 174/255, 150/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        Label:
            id: final_output
            text: ""
            multiline: True
            color:'#000000'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"lemon"
            size_hint: (.15,.10)
            pos_hint: {'center_x': .40, 'center_y': .55} 
            font_size: self.width/13
        Label:
            text: 
                """
                FIRST
                TABLE:
                """
            color:'#000000'
            font_name:"Mouse"
            font_size: self.width/15
            size_hint: (.80,.07)
            pos_hint: {'center_x': .15, 'center_y': .50} 
            
        Button:
            text: "Back"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .70} 
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Input'

        Button:
            text: "Next"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .50}
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'FollowingScreen'

        Button:
            text: "Quit"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .30}
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            on_press:
                quit()
        
<FollowingScreen>:
    Widget:
        canvas:
            Color:
                rgba: 220/255, 174/255, 150/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        Label:
            id: final_output1
            text: ""
            multiline: True
            color:'#000000'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"lemon"
            size_hint: (.25,.10)
            pos_hint: {'center_x': .41, 'center_y': .53} 
            font_size: self.width/20
        Label:
            text:
                """
                NEXT
                TABLES:
                """
            color:'#000000'
            font_name:"Mouse"
            font_size: self.width/15
            size_hint: (.80,.07)
            pos_hint: {'center_x': .13, 'center_y': .50} 
                
        Button:
            text: "Back"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .70} 
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Results'
        
        Button:
            text: "Next"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .50} 
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: "" 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'NextTables'

        Button:
            text: "Quit"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .30} 
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            on_press:
                quit()

<NextTables>:
    Widget:
        canvas:
            Color:
                rgba: 220/255, 174/255, 150/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        Label:
            id: middle_table
            text: ""
            multiline: True
            color:'#000000'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"lemon"
            size_hint: (.25,.10)
            pos_hint: {'center_x': .40, 'center_y': .53} 
            font_size: self.width/20
        Label:
            text:
                """
                NEXT
                TABLES:
                """
            color:'#000000'
            font_name:"Mouse"
            font_size: self.width/15
            size_hint: (.80,.07)
            pos_hint: {'center_x': .12, 'center_y': .50} 
                
        Button:
            text: "Back"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .70} 
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'FollowingScreen'
        
        Button:
            text: "Next"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .50} 
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: "" 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Final'

        Button:
            text: "Quit"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .80, 'center_y': .30} 
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            on_press:
                quit()

<Final>:
    Widget:
        canvas:
            Color:
                rgba: 220/255, 174/255, 150/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        Label:
            id: final_output2
            text: ""
            multiline: True
            color:'#000000'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"lemon"
            size_hint: (.25,.10)
            pos_hint: {'center_x': .38, 'center_y': .53} 
            font_size: self.width/15
        Label:
            text: 
                """
                FINAL TABLE:
                """
            color:'#000000'
            font_name:"Mouse"
            font_size: self.width/15
            size_hint: (.80,.07)
            pos_hint: {'center_x': .15, 'center_y': .90} 
            
        Button:
            text: "Back"
            size_hint: (.20,.20)
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            pos_hint: {'center_x': .80, 'center_y': .60} 
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'NextTables'

        Button:
            text: "Quit"
            size_hint: (.20,.20)
            background_color :'#000000'
            font_size: self.width/5
            size_hint: (.25,.10)
            font_name:"Mouse"
            background_normal: ""
            pos_hint: {'center_x': .80, 'center_y': .40}
            on_press:
                quit()

'''
#fonts
LabelBase.register(name='Mouse',
                   fn_regular='Mouse.ttf')
LabelBase.register(name='Mickey', 
                   fn_regular='MICKEY.TTF')
LabelBase.register(name='Minnie', 
                   fn_regular='Minnie.TTF')
LabelBase.register(name='lemon', 
                   fn_regular='lemon.otf')


class MainMenu(Screen):
    pass
  
class UserInput(Screen):
    def __init__(self, **kwargs):
        super(UserInput, self).__init__(**kwargs)

    def inputs(self, variable, minterms, dontCare, sizing):
        globalVariables.initialize() 
        tabular.driver(variable, minterms, dontCare,sizing)
        ntext = globalVariables.var4.replace(u'\t', u' ' * 8)
        return ntext
        
    def input1(self, variable, minterms, dontCare, sizing):
        globalVariables.initialize() 
        tabular.driver(variable, minterms, dontCare, sizing)
        ntext = globalVariables.var5.replace(u'\t', u' ' * 8)
        return ntext
    
    def inputMid(self, variable, minterms, dontCare, sizing):
        globalVariables.initialize() 
        tabular.driver(variable, minterms, dontCare, sizing)
        ntext = globalVariables.var6.replace(u'\t', u' ' * 8)
        return ntext
    
    def input2(self, variable, minterms, dontCare, sizing):
        globalVariables.initialize() 
        tabular.driver(variable, minterms, dontCare, sizing)
        ntext = globalVariables.chart.replace(u'\t', u' ' * 8)
        variable2 = globalVariables.txt
        return variable2 + ntext + globalVariables.error
    
class Results(Screen):
    pass

class FollowingScreen(Screen):
    pass

class NextTables(Screen):
    pass

class Final(Screen):
    pass

screen_manager = ScreenManager()


# Add the screens to the manager and then supply a name
# that is used to switch screens

screen_manager.add_widget(MainMenu(name ="MainMenu"))
screen_manager.add_widget(UserInput(name ="Input"))
screen_manager.add_widget(Results(name ="Results"))
screen_manager.add_widget(FollowingScreen(name ="FollowingScreen"))
screen_manager.add_widget(NextTables(name ="NextTables"))
screen_manager.add_widget(Final(name ="Final"))

class TabulationMethod(MDApp):
    def build(self): 
        screen = FloatLayout()
        Window.size = (1400, 1000)
        Window.clearcolor = (1,0,0,1)
        self.theme_cls.primary_palette = "Indigo"
        self.screen = Builder.load_string(screen_helper)
        screen.add_widget(self.screen)       
        return screen


# run the app
if __name__ == "__main__":
    app = TabulationMethod()
    app.run()