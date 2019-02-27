import tkinter
from tkinter import messagebox
from tkinter import ttk
import datetime
import time
import sys
import os
import csv
import re

color = '#F0F0F0'


def start():
    start_page = StartPage()
    start_page.first_screen()

class StartPage:
    def __init__(self):
        self.root = tkinter.Tk()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.root.attributes('-zoomed', True)
        self.root.configure(background=color)
        self.entries = [None]*8
        self.real_time = tkinter.StringVar()
        self.s_frame = ttk.Style()
        self.s_frame.configure('my.TFrame', background=color)

    def first_screen(self):
        fields = 'Block:', 'Participant Number:', 'Date + Time:', 'Handedness:', 'Age:', 'Gender:', \
                 'Native Language:', 'Second Language(s):'
        ents = self.make_form(fields)
        row = ttk.Frame(self.root, style='my.TFrame')
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 16), background=color)
        b1 = ttk.Button(row, text='Next', command=(lambda e=ents: self.add_entries(e)), style='my.TButton')
        b2 = ttk.Button(row, text='Quit', command=self.root.quit, style='my.TButton')
        row.pack(side='top', fill='none', pady=40)
        b1.pack(side='left', padx=50)
        b2.pack(side='right')
        self.root.mainloop()

    @staticmethod
    def create_a_csv(filename):
        header_list = ['Stimuli', 'Respond', 'Start_Time', 'Respond_Time', 'Block', 'Participant_Number', 'Date',
                       'Handedness', 'Age', 'Gender', 'Native_Language', 'Second_Languages']
        with open(output_data_path + filename, 'w', newline='', encoding='utf8') as create_the_csv:
            csv_writer = csv.writer(create_the_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(header_list)
        create_the_csv.close()
        return header_list

    def add_entries(self, new_entries):
        try:
            count = 0
            for entry in new_entries:
                if entry.get() == '':
                    raise IndexError
                else:
                    self.entries[count] = entry.get()
                    count += 1
            name = []
            for i, entry in enumerate(self.entries):
                if i < 3:
                    name.append(entry)
            filename = '_'.join(name)
            self.entries[7] = re.sub('\W+', '_', str(self.entries[7]))
            self.create_a_csv(filename+'.csv')
            self.root.destroy()
            trial_page = SecondPage(self.entries)
            trial_page.second_screen()
        except IndexError:
            tkinter.messagebox.showerror("Error", "There can not be empty entry!")

    def make_form(self, fields):
        entries = []
        s_label = ttk.Style()
        s_label.configure('my.TLabel', font=('Helvetica', 16), background=color)
        s_entry = ttk.Style()
        s_entry.configure('my.TEntry', backgroud='white')

        for field in fields:
            row = ttk.Frame(self.root, style='my.TFrame')
            lab = ttk.Label(row, width=20, text=field, anchor='w', style='my.TLabel')

            if field == 'Date + Time:':
                now = datetime.datetime.now()
                now = ('%d-%d-%d-%d:%d' % (now.year, now.month, now.day, now.hour, now.minute))
                self.real_time.set(now)
                ent = ttk.Entry(row, textvariable=self.real_time, style='my.TEntry', width='25', font=('Helvetica', 15))
            else:
                ent = ttk.Entry(row, style='my.TEntry', width='25', font=('Helvetica', 15))
            row.pack(side='top', fill='none', expand=True)
            lab.pack(side='left', padx=20)
            ent.pack(side='right', expand=True, fill='x')
            entries.append(ent)
        return entries


# Second page is training page
class SecondPage:
    def __init__(self, entries):
        self.info = entries
        self.root = tkinter.Tk()
        self.root.attributes('-zoomed', True)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.root.configure(background=color)
        self.stimuli_list = []
        self.count = 0
        self.text = None
        self.text2 = None
        self.text3 = None
        self.identifier = None
        self.s_frame = ttk.Style()
        self.s_frame.configure('my.TFrame', background=color)

    def second_screen(self):
        with open(test_path, 'r', encoding='utf8') as input_file:
            reader = csv.reader(input_file, delimiter=",")
            for line in reader:
                self.stimuli_list.append(line[0])
        self.make_form()
        self.root.mainloop()

    def tmp(self, event):
        self.root.unbind('<space>')
        self.root.after(1, self.play)

    def play(self):
        try:
            self.text.config(text='', font=('Arial', 17))
            self.text2.config(text=self.stimuli_list[self.count], font=('Arial', 17))
            self.text3.config(text='', font=('Arial', 17))
            self.count += 1
            self.root.bind('<Key>', self.fix)
            self.identifier = self.root.after(2000, self.fix_2)

        except IndexError:
            tkinter.messagebox.showerror("Info", "End of training, hit 'ok' to go on")
            self.root.destroy()
            third_screen = ThirdPage(self.info)
            third_screen.third_screen()


    def fix(self, event):
        self.root.unbind('<Key>')
        self.cancel()
        self.text.config(text='', font=('Arial', 100))
        self.text2.config(text='x', font=('Arial', 100))
        self.text3.config(text='', font=('Arial', 100))
        self.root.after(150, self.play)

    def fix_2(self):
        self.root.unbind('<Key>')
        self.text.config(text='', font=('Arial', 100))
        self.text2.config(text='x', font=('Arial', 100))
        self.text3.config(text='', font=('Arial', 100))
        self.root.after(150, self.play)

    def cancel(self):
        self.root.after_cancel(self.identifier)

    def make_form(self):
        instruction = 'You are about to see some words. '
        instruction2 = 'Please react by pressing keys on the keyboard.'
        instruction3 = 'Please press space bar to start a training round.'
        s_label = ttk.Style()
        s_label.configure('my.TLabel', font=('Helvetica', 16), background=color)
        row = ttk.Frame(self.root, style='my.TFrame')
        self.text = ttk.Label(row, text=instruction, anchor='w', style='my.TLabel')
        self.text2 = ttk.Label(row, text=instruction2, anchor='w', style='my.TLabel')
        self.text3 = ttk.Label(row, text=instruction3, anchor='w', style='my.TLabel')
        row.pack(fill='none', expand=True)
        self.text.pack()
        self.text2.pack()
        self.text3.pack()
        self.root.bind('<space>', self.tmp)


class ThirdPage:
    def __init__(self, entries):
        self.info = entries
        self.root = tkinter.Tk()
        self.root.attributes('-zoomed', True)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.root.configure(background=color)
        self.stimuli_list = []
        self.count = 0
        self.text = None
        self.text2 = None
        self.text3 = None
        self.start_time = 0
        self.respond_time = 0
        self.identifier = None
        self.s_frame = ttk.Style()
        self.s_frame.configure('my.TFrame', background=color)

    def third_screen(self):
        stimuli_file = None
        for each in os.listdir(input_csv_path):
            pattern = '_'+str(self.info[1])+'_'+str(self.info[0])+'.csv'
            if re.search(pattern, each) is not None:
                stimuli_file = input_csv_path + each
                break
        with open(stimuli_file, 'r', encoding='utf8') as input_file:
            reader = csv.reader(input_file, delimiter=",")
            for line in reader:
                self.stimuli_list.append(line[0])
        self.make_form()
        self.root.mainloop()

    def tmp(self, event):
        self.root.unbind('<space>')
        self.root.after(1, self.play)

    def play(self):

        try:
            self.start_time = time.time() - base_time
            self.text.config(text='', font=('Arial', 17))
            self.text2.config(text=self.stimuli_list[self.count], font=('Arial', 17))
            self.text3.config(text='', font=('Arial', 17))
            self.count += 1
            self.root.bind('<Key>', self.fix)
            self.identifier = self.root.after(2000, self.fix_2)

        except IndexError:
            tkinter.messagebox.showerror("Info", "End of experiment")
            self.root.destroy()

    def cancel(self):
        self.root.after_cancel(self.identifier)

    def fix(self, event):
        self.root.unbind('<Key>')
        self.cancel()
        key = event.keysym
        self.respond_time = time.time() - base_time
        self.write_csv(key)
        self.text.config(text='', font=('Arial', 100))
        self.text2.config(text='x', font=('Arial', 100))
        self.text3.config(text='', font=('Arial', 100))
        self.root.after(150, self.play)

    def fix_2(self):
        self.root.unbind('<Key>')
        self.respond_time = time.time() - base_time
        self.write_csv('None')
        self.text.config(text='', font=('Arial', 100))
        self.text2.config(text='x', font=('Arial', 100))
        self.text3.config(text='', font=('Arial', 100))
        self.root.after(150, self.play)

    def write_csv(self, respond):
        name = []
        for i, entry in enumerate(self.info):
            if i < 3:
                name.append(entry)
        filename = '_'.join(name)+'.csv'
        with open(output_data_path + filename, 'a', encoding='utf8')as out:
            csv_writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([self.stimuli_list[self.count-1][self.stimuli_list[self.count-1].find('/')+1:], respond,
                                 self.start_time, self.respond_time, self.info[0], self.info[1], self.info[2],
                                 self.info[3], self.info[4], self.info[5], self.info[6], self.info[7]])

    def make_form(self):
        instruction = ''
        instruction2 = 'You are now ready to begin. Please hit space bar when you are ready.'
        instruction3 = ''
        s_label = ttk.Style()
        s_label.configure('my.TLabel', font=('Helvetica', 16), background=color)
        row = ttk.Frame(self.root, style='my.TFrame')
        self.text = ttk.Label(row, text=instruction, anchor='w', style='my.TLabel')
        self.text2 = ttk.Label(row, text=instruction2, anchor='w', style='my.TLabel')
        self.text3 = ttk.Label(row, text=instruction3, anchor='w', style='my.TLabel')
        row.pack(fill='none', expand=True)
        self.text.pack()
        self.text2.pack()
        self.text3.pack()
        self.root.bind('<space>', self.tmp)


if __name__ == '__main__':
    home_path = sys.argv[1]
    #home_path = '/home/nianheng/Documents/hiwi/01januar/fabian/Tense_Identificantion_Test/' \
                # 'recording_morphology_experiment/00results/ui/collect_ui/'
    # recording_morphology_experiment/00results/'

    input_csv_path = home_path + 'stimuli/'
    test_path = home_path + 'training/'
    test_path = test_path + os.listdir(test_path)[0]
    output_data_path = home_path + 'result/'
    # output_data_path = '/home/nianheng/PycharmProjects/perception_experiment/'
    base_time = time.time()
    start()
