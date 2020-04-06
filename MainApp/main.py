# Screemanager can contain any number of child screen widgets
import kivy
kivy.require('1.11.1')
import support as mn
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, NumericProperty, StringProperty

from kivy.uix.scrollview import ScrollView

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time, random


# The 1,2,c screens are Screens, which are not boxlayout
# subsequently add boxlayout to screens


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    # Promoter Screen
    name_list = ListProperty()
    sequence_list = ListProperty()
    strength_list = ListProperty()

    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)

        name_list_input = []
        sequence_list_input = []
        strength_list_input = []
        object_list_input = mn.File_Promoters
        for i in range(0, len(object_list_input)):
            name_list_input.append(object_list_input[i].name)
            sequence_list_input.append(object_list_input[i].sequence)
            strength_list_input.append(object_list_input[i].strength)

        self.name_list = name_list_input
        self.sequence_list = sequence_list_input
        self.strength_list = strength_list_input

    def updating_text_box(self):

        spinner = self.ids.promoterspinner
        label_box = self.ids.promoterInfo

        name_index = self.name_list.index(spinner.text)
        print(name_index)
        corresponding_name = self.name_list[name_index]
        corresponding_sequence = self.sequence_list[name_index]
        print(corresponding_sequence)
        corresponding_strength = self.strength_list[name_index]
        print(corresponding_strength)

        updated_text = 'The {} is defined by the following sequence: {}.' \
                       ' The measured strenght is' \
                       ' {} units. <AdditionalDescriptions>'.format(corresponding_name, corresponding_sequence, corresponding_strength)
        label_box.text = updated_text


class FourthScreen(Screen):
    # Gene Screen

    name_list = ListProperty()
    sequence_list = ListProperty()

    def __init__(self, **kwargs):
        super(FourthScreen, self).__init__(**kwargs)

        name_list_input = []
        sequence_list_input = []
        object_list_input = mn.File_Genes
        for i in range(0, len(object_list_input)):
            name_list_input.append(object_list_input[i].name)
            sequence_list_input.append(object_list_input[i].sequence)

        self.name_list = name_list_input
        self.sequence_list = sequence_list_input

    def updating_text_box(self):

        spinner = self.ids.genespinner
        label_box = self.ids.geneInfo

        name_index = self.name_list.index(spinner.text)
        print(name_index)
        corresponding_name = self.name_list[name_index]
        corresponding_sequence = self.sequence_list[name_index]
        print(corresponding_sequence)

        updated_text = 'The {} gene is defined by the following sequence: {}.' \
                       '<AdditionalDescriptions>'.format(corresponding_name, corresponding_sequence)
        label_box.text = updated_text


class FifthScreen(Screen):
    # 5UTR Screen

    def __init__(self, **kwargs):
        super(FifthScreen, self).__init__(**kwargs)

        name_list_input = []
        sequence_list_input = []
        object_list_input = mn.File_FiveUtrs
        for i in range(0, len(object_list_input)):
            name_list_input.append(object_list_input[i].name)
            sequence_list_input.append(object_list_input[i].sequence)

        self.name_list = name_list_input
        self.sequence_list = sequence_list_input

    def updating_text_box(self):

        spinner = self.ids.utrSpinner
        label_box = self.ids.utrInfo

        name_index = self.name_list.index(spinner.text)
        print(name_index)
        corresponding_name = self.name_list[name_index]
        corresponding_sequence = self.sequence_list[name_index]
        print(corresponding_sequence)

        updated_text = 'The {} untranslated region is defined by the following sequence: {}.' \
                       '<AdditionalDescriptions>'.format(corresponding_name, corresponding_sequence)
        label_box.text = updated_text


class SixthScreen(Screen):
    # 5UTR Screen

    def __init__(self, **kwargs):
        super(SixthScreen, self).__init__(**kwargs)

        name_list_input = []
        sequence_list_input = []
        object_list_input = mn.File_FiveUtrs
        for i in range(0, len(object_list_input)):
            name_list_input.append(object_list_input[i].name)
            sequence_list_input.append(object_list_input[i].sequence)

        self.name_list = name_list_input
        self.sequence_list = sequence_list_input



    def updating_text_box(self):

        spinner = self.ids.utrSpinner
        label_box = self.ids.utrInfo

        name_index = self.name_list.index(spinner.text)
        print(name_index)
        corresponding_name = self.name_list[name_index]
        corresponding_sequence = self.sequence_list[name_index]
        print(corresponding_sequence)

        updated_text = 'The {} untranslated region is defined by the following sequence: {}.' \
                       '<AdditionalDescriptions>'.format(corresponding_name, corresponding_sequence)
        label_box.text = updated_text



class ColourScreen(Screen):
    colour = ListProperty([1, 0, 0, 1])


# Also need ScreenManager class:

class MyScreenManager(ScreenManager):

    # def __init__(self, **kwargs):
    # self.build_lists()
    # super(MyScreenManager, self).__init__(**kwargs)

    # the method creates a new colour screen and adds it to the screen manager
    # and changes the current property to the new screen
    def new_colour_screen(self):
        name = str(time.time())

        # make screen widget
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        # adding the made screen widget
        self.add_widget(s)
        self.current = name




# root is screenmanager
root_widget = Builder.load_file(filename = 'screenmanager.kv')


class AlgalsequenceanalysisApp(App):
    def build(self):
        return root_widget


AlgalsequenceanalysisApp().run()


