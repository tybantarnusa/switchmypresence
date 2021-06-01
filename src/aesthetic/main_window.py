from PIL import Image, ImageTk
from tkinter import Button, Entry, Frame, Label, LabelFrame, Listbox, messagebox, Radiobutton, Scrollbar, IntVar, StringVar
from logic import games
from logic.discord import Discord
import os.path

class MainWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Instance variables
        self.launched = False
        self.game_data = games.instance.get_list()
        self.selected_game = None

        # Build GUI
        Frame.__init__(self, master)

        self.master.title('SwitchMyPresence')
        self.master.minsize(width=600, height=100)
        self.master.resizable(False, False)

        self.create_header()
        self.create_content()

        self.pack(fill='both')

    def create_header(self):
        frame = Frame(self, borderwidth=0)
        frame.pack(fill='x', side='top')

        banner_path = os.path.join(os.path.dirname(__file__), '../assets/banner.jpg')
        img = Image.open(banner_path)
        img.thumbnail((600,600), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(img)

        banner = Label(frame, image=render, borderwidth=0)
        banner.image = render
        banner.place(x=0, y=0)
        banner.pack(fill='x')

    def create_content(self):
        frame = Frame(self)
        frame.pack(side='top', fill='both')

        self.create_game_selector(frame)
        self.create_menu_control(frame)

    def create_game_selector(self, root):
        frame = Frame(root, padx=5, pady=5)
        frame.pack(fill='y', side='left')

        label_frame = LabelFrame(frame, text='Game List', padx=10, pady=10)
        label_frame.pack(fill='both')

        self.gamelist = Listbox(label_frame, activestyle='none', width=50)
        
        i = 1
        for game in self.game_data:
            self.gamelist.insert(i, game['title'])
            i += 1

        self.gamelist.pack(side='left', fill='both')

        scrollbar = Scrollbar(label_frame, orient='vertical', command=self.gamelist.yview)
        scrollbar.pack(side='right', fill='y')

        self.gamelist.config(yscrollcommand=scrollbar.set)
        self.gamelist.bind("<<ListboxSelect>>", self.handle_select_game)

    def create_menu_control(self, root):
        frame = Frame(root, padx=5, pady=5)
        frame.pack(fill='both', side='right', expand=True)

        self.create_name_control(frame)
        self.create_menu_button(frame)
        self.create_status_indicator(frame)

    def create_name_control(self, root):
        label_frame = LabelFrame(root, text='Game Title', padx=10, pady=5)
        label_frame.pack(fill='x', side='top', expand=True)
        label_frame.columnconfigure(0, weight=1, uniform='name_radio')
        label_frame.columnconfigure(1, weight=1, uniform='name_radio')

        self.custom_game_title = StringVar()
        self.name_input = Entry(label_frame, state='disabled', textvariable=self.custom_game_title)
        self.name_input.grid(row=0, column=0, columnspan=2, sticky='nesw')

        self.name_method = IntVar()
        radio_from_list = Radiobutton(label_frame, text='From List', variable=self.name_method, value=1, command=self.handle_name_method_selection)
        radio_from_list.grid(row=1, column=0, sticky='w')
        radio_from_list.select()

        radio_custom = Radiobutton(label_frame, text='Custom', variable=self.name_method, value=2, command=self.handle_name_method_selection)
        radio_custom.grid(row=1, column=1, sticky='w')

    def create_menu_button(self, root):
        label_frame = LabelFrame(root, text='Presence Launcher', padx=10, pady=10)
        label_frame.pack(fill='x', side='top',  expand=True)
        label_frame.columnconfigure(0, weight=1, uniform='menu_button')
        label_frame.columnconfigure(1, weight=1, uniform='menu_button')

        self.launch_button = Button(label_frame, text='Launch', command=self.handle_launch)
        self.launch_button.grid(row=0, column=0, sticky='nesw')

        stop_button = Button(label_frame, text='Stop', command=self.handle_stop)
        stop_button.grid(row=0, column=1, sticky='nesw')

    def create_status_indicator(self, root):
        label_frame = LabelFrame(root, text='Status', pady=5)
        label_frame.pack(fill='x', side='top',  expand=True)

        self.status_message = Label(label_frame, text='⬤ Inactive', foreground='red', highlightbackground='black', highlightthickness=2)
        self.status_message.pack(fill='x', side='bottom', expand=True)

    def handle_select_game(self, event):
        name_method = self.name_method.get()
        if name_method == 2:
            return
        selected_game = event.widget.curselection()[0]
        self.selected_game = self.game_data[selected_game]
        self.custom_game_title.set(self.selected_game['title'])

    def handle_name_method_selection(self):
        name_method = self.name_method.get()

        if name_method == 1:
            self.gamelist.config(state='normal')
            self.name_input.config(state='disabled')
        if name_method == 2:
            self.selected_game = None
            self.gamelist.config(state='disabled')
            self.name_input.config(state='normal')

    def handle_launch(self):
        if self.name_method.get() == 1 and self.selected_game == None:
            messagebox.showerror("Error", "Please select a game.")
            return

        if self.name_method.get() == 2 and self.custom_game_title.get() == '':
            messagebox.showerror("Error", "Please input the game name.")
            return

        self.status_message.config(text='⬤ Launching...', foreground='yellow')
        self.status_message.after(500, self.handle_launch_exec)

    def handle_launch_exec(self):
        name_method = self.name_method.get()

        if self.launched:
            self.discord.stop()

        title = self.custom_game_title.get()
        image = 'default'
        if name_method == 1:
            image = self.selected_game['image']

        self.discord = Discord(title, image)
        self.discord.present()
        self.status_message.config(text='⬤ Active', foreground='green')

        self.launched = True

    def handle_stop(self):
        if not self.launched:
            return
            
        messagebox.showinfo("Stopping...", "Your presence is being stopped. It might take a little time to actually disappear from your Discord.")
        self.discord.stop()
        self.launched = False
        self.status_message.config(text='⬤ Inactive', foreground='red')