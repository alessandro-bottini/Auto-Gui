
# Libraries
import os
import customtkinter
import tkinter
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk

# CustomTkinter Settings
customtkinter.set_appearance_mode('dark')

# Define Class
class Gui(customtkinter.CTk):
    def __init__(self):

        # Initiaize class
        super().__init__()
        self.title('Auto-Gui  v 1.0')
        self.resizable(False, False)
        self.geometry('750x450')

        # Current Background
        self.background_color = '#2A2D2E'

        # List Of Widgets' Name And Functions
        self.text_function_widgets = [
            ['Background', self.change_background],
            ['Frame', self.create_frame],
            ['Button', self.change_background],
            ['Label', self.change_background], 
            ['Entry', self.change_background],
            ['Option Menu', self.change_background], 
            ['Check Box', self.change_background], 
            ['Switch', self.change_background]
        ]

        # List Of Default Colors To Change The Background
        self.default_colors = [
            ['Black (#2A2D2E)', '2A2D2E'],
            ['White (#F4F4F4)', 'F4F4F4'],
            ['Blue (#364A95)', '364A95'],
            ['Green (#0A4019)', '0A4019'],
            ['Purple (#5F43B2)', '5F43B2'],
            ['Orange (#A06A22)', 'A06A22']
        ]

        # List Of Labels Used To Customize Every Widget
        self.labels = [
            ['Size', 0], ['Color', 2], ['Border Color', 4], ['Padx And Pady', 6], ['Position', 8]
        ]

        # Path To Add Images
        self.PATH = os.path.dirname(os.path.realpath(__file__))
        # Realod.png
        self.reload_image = self.load_image("/img/reload.png", 30)
        # Home.png
        self.home_image = self.load_image("/img/home.png", 24)

        # Initialize Window
        self.landing_page()


    #   Function To Add Images
    def load_image(self, path, image_size):
        return ImageTk.PhotoImage(Image.open(self.PATH + path).resize((image_size, image_size)))


    # Landing Page Made To Choose The Widgets To Add And Check The GUI's Preview
    def landing_page(self): 

        for i in self.winfo_children(): i.destroy()

        self.widgets_list_frame = customtkinter.CTkFrame(self, border_color='#7329A7', border_width=3, fg_color='#A964DB')
        self.widgets_list_frame.pack(side='left', fill='y')
        self.background_frame = customtkinter.CTkFrame(self, border_color='#7329A7', fg_color=self.background_color, border_width=3, corner_radius=25)
        self.background_frame.pack(side='right', expand=True, fill='both', padx=20, pady=20)
        self.background_frame.grid_rowconfigure(0, weight=1)
        self.background_frame.grid_columnconfigure(0, weight=1)

        # Function To Reset Preview Window And Data Saved
        def reset_window():
            for i in self.background_frame.winfo_children(): i.destroy()
            self.background_color = '#2A2D2E'
            self.background_frame.configure(fg_color=self.background_color)

        self.back_home_button = customtkinter.CTkButton(self.widgets_list_frame, text='Reset Window',image=self.reload_image, fg_color='#7329A7', hover_color='#863FB9', corner_radius=0, text_font=(None, 13), width=210, height=42, command=reset_window)
        self.back_home_button.pack(pady=1, padx=2)
        self.spacer_widget_list = customtkinter.CTkLabel(self.widgets_list_frame, text='')
        self.spacer_widget_list.pack()
        self.wdigets_inside_list = customtkinter.CTkFrame(self.widgets_list_frame, fg_color='#A964DB')
        self.wdigets_inside_list.pack()

        # Widgets List
        for i in range(len(self.text_function_widgets)):
            self.widget = customtkinter.CTkButton(self.wdigets_inside_list, text=self.text_function_widgets[i][0], fg_color='#7329A7', hover_color='#863FB9', width=160, height=35, corner_radius=0, text_font=(None, 11), command=self.text_function_widgets[i][1])
            self.widget.pack()
        
        self.getcode = customtkinter.CTkButton(self.wdigets_inside_list, text='Finish', fg_color='#7329A7', hover_color='#863FB9', height=40, width=160, corner_radius=20, text_font=(None, 12))
        self.getcode.pack(pady=25)


    # Page To Change The Background Color
    def change_background(self):

        self.back_home_button.configure(text=' Back To Menu', command=self.landing_page, image=self.home_image)
        self.spacer_widget_list.configure(height=1)
        for i in self.wdigets_inside_list.winfo_children(): i.destroy()

        self.custom_background_label = customtkinter.CTkLabel(self.wdigets_inside_list, text='Custom Color', text_font=(None, 12))
        self.custom_background_label.pack(pady=4)
        self.custom_frame = customtkinter.CTkFrame(self.wdigets_inside_list, fg_color='#A964DB')
        self.custom_frame.pack(padx=5)
        self.custom_entry = customtkinter.CTkEntry(self.custom_frame, placeholder_text='Ex. F1F1F1', width=130, corner_radius=15, fg_color='#A964DB', border_color='#7329A7', placeholder_text_color='#D9D8D8', text_font=(None, 10))
        self.custom_entry.pack(side='left', padx=2)
        self.custom_apply = customtkinter.CTkButton(self.custom_frame, text='Done', width=40, fg_color='#7329A7', hover_color='#863FB9', corner_radius=12, command=lambda *args, **kwargs: set_new_backgroud(self.custom_entry.get()))
        self.custom_apply.pack(side='right')
        self.spacer_background_color = customtkinter.CTkLabel(self.wdigets_inside_list, text='', height=1)
        self.spacer_background_color.pack()
        self.default_background_label = customtkinter.CTkLabel(self.wdigets_inside_list, text='Default Colors', text_font=(None, 12))
        self.default_background_label.pack(pady=4)

        self.radiovar = tkinter.StringVar()

        # List Of Availables Colors
        for i in range(len(self.default_colors)):
            self.default_color = customtkinter.CTkRadioButton(self.wdigets_inside_list, text=self.default_colors[i][0], text_font=(None, 10), border_color='#BC7CEA', hover_color='#7329A7', fg_color='#7329A7', value=self.default_colors[i][1], variable=self.radiovar)
            self.default_color.pack(anchor='w', padx=30, pady=5)

        # Function To Update Background Color
        def set_new_backgroud(color):
            try: self.background_frame.configure(fg_color=f'#{color}')
            except: MessageBox.showerror("Warning!", f'Color #{color} doesn\'t exist!')
            else: self.background_color = f'#{color}'; self.landing_page()

        self.done_background = customtkinter.CTkButton(self.wdigets_inside_list, text='Done', corner_radius=25, fg_color='#7329A7', hover_color='#863FB9', text_font=(None, 12), width=130, height=36, command=lambda *args, **kwargs: set_new_backgroud(self.radiovar.get()))
        self.done_background.pack(pady=15)


    # Page To Create A New Frame
    def create_frame(self):

        self.back_home_button.configure(text=' Back To Menu', command=self.landing_page, image=self.home_image)
        self.spacer_widget_list.destroy()
        for i in self.wdigets_inside_list.winfo_children(): i.destroy()

        # List Of Options To Customize
        for i in range(len(self.labels)):
            self.frame_label = customtkinter.CTkLabel(self.wdigets_inside_list, text=self.labels[i][0], text_font=(None, 12))
            self.frame_label.grid(row=self.labels[i][1], column=0, pady=6)

        self.frame_size_entry = customtkinter.CTkEntry(self.wdigets_inside_list, placeholder_text='Ex. 100x80', width=150, corner_radius=16, fg_color='#A964DB', border_color='#7329A7', placeholder_text_color='#D9D8D8', text_font=(None, 10))
        self.frame_size_entry.grid(row=1)
        self.frame_color_entry = customtkinter.CTkEntry(self.wdigets_inside_list, placeholder_text='Ex. 2A2A2A', width=150, corner_radius=16, fg_color='#A964DB', border_color='#7329A7', placeholder_text_color='#D9D8D8', text_font=(None, 10))
        self.frame_color_entry.grid(row=3)
        self.frame_border_entry = customtkinter.CTkEntry(self.wdigets_inside_list, placeholder_text='Ex. #3D3D3D', width=150, corner_radius=16, fg_color='#A964DB', border_color='#7329A7', placeholder_text_color='#D9D8D8', text_font=(None, 10))
        self.frame_border_entry.grid(row=5)
        self.frame_pad_entry = customtkinter.CTkEntry(self.wdigets_inside_list, placeholder_text='Ex. 20:20', width=150, corner_radius=16, fg_color='#A964DB', border_color='#7329A7', placeholder_text_color='#D9D8D8', text_font=(None, 10))
        self.frame_pad_entry.grid(row=7)
        self.frame_position_entry = customtkinter.CTkEntry(self.wdigets_inside_list, placeholder_text='Ex. 0:1', width=150, corner_radius=16, fg_color='#A964DB', border_color='#7329A7', placeholder_text_color='#D9D8D8', text_font=(None, 10))
        self.frame_position_entry.grid(row=9)

        # Spawn Frame
        def spawn_frame(size, position, colorf, padding, border): 
            size, position, padding = size.split('x'), position.split(':'), padding.split(':')
            self.generated_frame = customtkinter.CTkFrame(self.background_frame, fg_color=colorf, corner_radius=18, border_color=border, width=int(size[0]), height=int(size[1]), border_width=2)
            try: self.generated_frame.grid(row=int(position[0]), column=int(position[1]), padx=padding[0], pady=padding[1])
            except: MessageBox.showerror('Warning!', 'Some error occured creating the frame!')

        self.done_background = customtkinter.CTkButton(self.wdigets_inside_list, text='Done', corner_radius=25, fg_color='#7329A7', hover_color='#863FB9', text_font=(None, 12), width=130, height=36, command=lambda *args, **kwargs: spawn_frame(self.frame_size_entry.get(), self.frame_position_entry.get(), self.frame_color_entry.get(), self.frame_pad_entry.get(), self.frame_border_entry.get()))
        self.done_background.grid(pady=13)


# Execute Code
if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()