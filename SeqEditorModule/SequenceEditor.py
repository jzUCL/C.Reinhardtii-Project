from random import sample
from string import ascii_lowercase

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.factory import Factory

import pandas

kv = """
#:import Factory kivy.factory.Factory

<Row@BoxLayout>:
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        Rectangle:
            size: self.size
            pos: self.pos
    value: ''
    Label:
        text: root.value
<MyPopup@Popup>:
    # id: popup
    title: 'Sequence Data'

    size_hint_y: 0.8
    
    TextInput:
        text: app.root.display_sequence
    
    #GridLayout:
     #   cols: 1
      #  rows: 2
       # size: self.size
        #height: self.height
        #size_hint_y: 0.8
        # height: dp(108)
        #padding: dp(8)
        #spacing: dp(16)
        #BoxLayout:
         #   pos_hint_y: 0.1
          #  size_hint_y: 0.2
           # padding: dp(8)
            #spacing: dp(16)
            
            #Spinner: 
             #   id: 'SequenceInspectorSpinner'
              #  size_hint_x: 0.1
               # text: 'Constructed Sequences'
                #values: app.root.constructed_identifiers
                #on_text: app.root.sequence_display()
                
            #Button:
             #   size_hint_x: 0.1
              #  text: 'Close me!'
               # on_release: root.dismiss()
            
        # TextInput:
           #  id: sequencedisplay
            # size_hint_y: 0.95
            # text: "app.root.sequence_display"
            # font_size: 25
            
<Test>:
    canvas:
        Color:
            rgba: 0.3, 0.3, 0.3, 1
        Rectangle:
            size: self.size
            pos: self.pos
    rv: rv
    orientation: 'vertical'
    GridLayout:
        cols: 1
        rows: 3
        size_hint_y: None
        height: dp(108)
        padding: dp(8)
        spacing: dp(16)
        # Button:
            # text: 'Populate list'
            # on_press: root.populate()
        # Button:
            # text: 'Sort list'
            # on_press: root.sort()
        # Button:
            # text: 'Clear list'
            # on_press: root.clear()
        
        BoxLayout: 
            
            Spinner:
                id: promoterspinner
                text: 'Promoters'
                values: root.promoter_spinner
            Spinner:
                id: utrspinner
                text: '5UTR'
                values: root.utr5_spinner
            Spinner:
                id: cdspinner
                text: 'CDS'
                values: root.cds_spinner
            Spinner:
                id: termspinner
                text: 'Terminators'
                values: root.term_spinner
            Spinner:
                id: vectorspinner
                text: 'Level 1 Vectors'
                values: root.vector_spinner
            
            Button:
                text: 'Construct Part'
                on_press: root.insert(promoterspinner.text, utrspinner.text, cdspinner.text, termspinner.text, vectorspinner.text)
        
     
        BoxLayout:
            Spinner:
                id: SequenceInspectorSpinner
                text: 'Constructs'
                values: root.constructed_identifiers
                on_text: root.sequence_display()
                
            Button:
                id: Popupseq
                text: 'Display'
                on_release: Factory.MyPopup().open()
            
            Button:
                text: 'Remove first item'
                on_press: root.remove()
                
            
        # Spinner:
            # id: sequencedisplay
            # text: 'Constructs Sequence'
           # values: root.constructed_identifiers
            # on_press: root.displaying_selections() 
        
        # BoxLayout:
            # spacing: dp(8)
            # Button:
                # text: 'Insert new item'
                # on_press: root.insert(promoterspinner.text)

            # TextInput:
                # id: new_item_input
                # size_hint_x: 0.6
                # hint_text: 'value'
                # padding: dp(10), dp(10), 0, 0
        # BoxLayout:
            # spacing: dp(8)
            # Button:
                # text: 'Update first item'
                # on_press: root.update(update_item_input.text)
            # TextInput:
                # id: update_item_input
                # size_hint_x: 0.6
                # hint_text: 'new value'
                # padding: dp(10), dp(10), 0, 0
        
            
    RecycleView:
        id: rv
        scroll_type: ['bars', 'content']
        scroll_wheel_distance: dp(116)
        bar_width: dp(15)
        viewclass: 'Row'
        RecycleBoxLayout:
            default_size: 0.8, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            width: self.minimum_width
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
"""

Builder.load_string(kv)


class Test(BoxLayout):
    # items_list = ObjectProperty(None)
    # column_headings = ObjectProperty(None)
    rv_data = ListProperty([])

    constructed_identifiers = ListProperty([])
    constructed_sequences = ListProperty([])

    display_sequence = StringProperty('')

    promoter_spinner = ListProperty([])
    promoter_sequences = ListProperty([])

    utr5_spinner = ListProperty([])
    utr5_sequences = ListProperty([])

    cds_spinner = ListProperty([])
    cds_sequences = ListProperty([])

    term_spinner = ListProperty([])
    term_sequences = ListProperty([])

    vector_spinner = ListProperty([])
    vector_sequences = ListProperty([])



    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

        df_promoters = pandas.read_excel('promoters_project.xlsx')
        df_5utr = pandas.read_excel('5utr_project.xlsx')
        df_cds = pandas.read_excel('cds_project.xlsx')
        df_term = pandas.read_excel('term_project.xlsx')
        df_vectorLv1 = pandas.read_excel('vectorsLv1_project.xlsx')

        # self.constructed_identifiers = ListProperty([])
        # self.constructed_sequences = ListProperty([])


        # Promoter Data Extraction
        promoter_names = []
        promoter_sequences = []
        for i in range(0, len(df_promoters)):
            promoter_names.append(df_promoters.Promoter[i])
            promoter_sequences.append(df_promoters.Insert[i])

        self.promoter_spinner = promoter_names
        self.promoter_sequences = promoter_sequences

        #5'UTR Data extraction
        utr5_names = []
        utr5_sequences = []
        for i in range(0, len(df_5utr)):
            utr5_names.append(df_5utr.UTR5[i])
            utr5_sequences.append(df_5utr.Insert[i])

        self.utr5_spinner = utr5_names
        self.utr5_sequences = utr5_sequences

        # CDS Data extraction
        cds_names = []
        cds_sequences = []
        for i in range(0, len(df_cds)):
            cds_names.append(df_cds.CDS[i])
            cds_sequences.append(df_cds.Insert[i])

        self.cds_spinner = cds_names
        self.cds_sequences = cds_sequences

        # Term Data extraction
        term_names = []
        term_sequences = []
        for i in range(0, len(df_term)):
            term_names.append(df_term.Term[i])
            term_sequences.append(df_term.Insert[i])

        self.term_spinner = term_names
        self.term_sequences = term_sequences

        # Lv1 Vector data extraction
        lv1vector_names = []
        lv1vector_sequences = []
        for i in range(0, len(df_vectorLv1)):
            lv1vector_names.append(df_vectorLv1.Vector[i])
            lv1vector_sequences.append(df_vectorLv1.Sequence[i])

        # In the file - vector sequences defined from e.g. B --> A (insert appended at front of string)
        self.vector_spinner = lv1vector_names
        self.vector_sequences = lv1vector_sequences


    def populate(self):
        self.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))}
                        for x in range(50)]

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])

    def clear(self):
        self.rv.data = []

    def insert(self, promoter, utr5, cds, term, lv1vector):
        # compiled_name = 'Part {}-{}:{}:{}:{}'.format(lv1vector+promoter+utr5+cds+term)
        # self.rv.data.insert(0, '{}/{}:{}:{}:{}'.format(lv1vector,promoter,utr5,cds,term))
        self.rv.data.insert(0, {'value': '{}/{}:{}:{}:{}'.format(lv1vector, promoter, utr5, cds, term)})
        # Names of constructs
        self.constructed_identifiers.append('{}/{}:{}:{}:{}'.format(lv1vector, promoter, utr5, cds, term))

        vector_index = self.vector_spinner.index(lv1vector)
        promoter_index = self.promoter_spinner.index(promoter)
        utr5_index = self.utr5_spinner.index(utr5)
        cds_index = self.cds_spinner.index(cds)
        term_index = self.term_spinner.index(term)

        # sequence associated with the construct
        self.constructed_sequences.append(
            '{}{}CCA{}ATG{}TAA{}'.format(self.vector_sequences[vector_index],
                                   self.promoter_sequences[promoter_index],
                                   self.utr5_sequences[utr5_index],
                                   self.cds_sequences[cds_index],
                                   self.term_sequences[term_index]
                                   ))


    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['value'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)

    # def displaying_selections(self):
        # print(self.rv.data)
        # print(type(self.rv.data))
        # promoter_info = self.ids.promoterspinner
        # label_box = self.ids.utrInfo

    def sequence_display(self):
        selected = self.ids.SequenceInspectorSpinner
        selection_index = self.constructed_identifiers.index(selected.text)
        corresponding_construct = self.constructed_identifiers[selection_index]
        corresponding_sequence = self.constructed_sequences[selection_index]

        updating_text = 'The {} Level 1 part is defined ' \
                        'by the following sequence: {}.'.format(corresponding_construct, corresponding_sequence)

        self.display_sequence = updating_text
        print(self.display_sequence)
        print(len(self.display_sequence))



class TestApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TestApp().run()