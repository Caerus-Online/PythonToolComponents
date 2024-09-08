import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from styles import apply_modern_style  # Import the function


class ModernGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        apply_modern_style(self)

        self.configure(bg="#363739")
        self.title("Tool Name")

        # Create menu bar
        self.create_menu_bar()

        # Create two frames for the columns
        left_frame = tk.Frame(self, bg="#363739")
        right_frame = tk.Frame(self, bg="#363739")
        left_frame.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.BOTH)
        right_frame.pack(side=tk.RIGHT, padx=10, expand=True, fill=tk.BOTH)

        # Button Example
        self.create_section(left_frame, "Button Example", self.create_button)

        # Radial Button Examples
        self.create_section(
            left_frame, "Radial Button Examples", self.create_radial_buttons
        )

        # Dropdown Example
        self.create_section(left_frame, "Dropdown Example", self.create_dropdown)

        # Slider Example
        self.create_section(right_frame, "Slider Example", self.create_slider)

        # Progress Bar Example
        self.create_section(
            right_frame, "Progress Bar Example", self.create_progress_bar
        )

        # Checkbox Example
        self.create_section(right_frame, "Checkbox Example", self.create_checkbox)

        # Entry Field Example
        self.create_section(right_frame, "Entry Field Example", self.create_entry_field)

        # Text Widget with Scrollbar Example
        self.create_section(right_frame, "Text Widget Example", self.create_text_widget)

        copyright_label = tk.Label(
            self, text="© Caerus Online 2024", bg="#363739", fg="white"
        )
        copyright_label.pack(side="bottom")

    def create_menu_bar(self):
        menu_bar = tk.Frame(self, bg="#363739")
        menu_bar.pack(side=tk.TOP, fill=tk.X)

        menu_buttons = ["File", "Edit", "View", "Help"]
        for button_text in menu_buttons:
            button = ttk.Button(
                menu_bar,
                text=button_text,
                style="Modern.MenuBar.TButton",
                command=lambda t=button_text: print(f"{t} clicked!"),
            )
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def create_section(self, parent, title, content_func):
        section_frame = tk.Frame(parent, bg="#363739")
        section_frame.pack(pady=10, fill=tk.X)

        section_label = tk.Label(
            section_frame,
            text=title,
            bg="#363739",
            fg="white",
            font=("Roboto", 14, "bold"),
        )
        section_label.pack(pady=(10, 5))

        content_func(section_frame)

    def create_button(self, parent):
        self.sample_button = ttk.Button(
            parent,
            text="Click Me",
            style="Modern.TButton",
            command=self.button_clicked,
            cursor="hand2",
        )
        self.sample_button.pack()

    def create_radial_buttons(self, parent):
        self.radio_var = tk.StringVar(value="option1")
        for val, text in [("option1", "Option 1"), ("option2", "Option 2")]:
            rb = ttk.Radiobutton(
                parent,
                text=text,
                variable=self.radio_var,
                value=val,
                style="Modern.TRadiobutton",
                command=self.update_radial_buttons,
            )
            rb.pack(pady=5)

            circle = tk.Canvas(
                rb, width=20, height=20, bg="#363739", highlightthickness=0
            )
            circle.create_oval(
                2, 2, 18, 18, fill="#F69728", outline=""
            )  # Outer circle filled initially
            circle.create_oval(6, 6, 14, 14, fill="#363739", outline="")
            circle.place(in_=rb, relx=0, rely=0.5, anchor="w")
            rb.circle = circle

    def create_dropdown(self, parent):
        options = ["Choice 1", "Choice 2", "Choice 3"]
        self.dropdown_var = tk.StringVar(value=options[0])
        dropdown = ttk.Combobox(
            parent,
            textvariable=self.dropdown_var,
            values=options,
            style="Modern.TCombobox",
        )
        dropdown.pack()

        dropdown_button = ttk.Button(
            parent,
            text="▼",
            style="Modern.TButton",
            command=lambda: dropdown.event_generate("<Button-1>"),
            width=2,
            padding=(0, 0),
        )
        dropdown_button.place(
            in_=dropdown,
            relx=1.0,
            rely=0.0,
            anchor="ne",
            height=dropdown.winfo_reqheight(),
        )

        bold_font = tkfont.Font(font=dropdown["font"])
        bold_font.configure(weight="bold")
        dropdown.configure(font=bold_font)

        self.option_add("*TCombobox*Listbox*Background", "white")
        self.option_add("*TCombobox*Listbox*Foreground", "#363739")
        self.option_add("*TCombobox*Listbox*selectBackground", "#F69728")
        self.option_add("*TCombobox*Listbox*selectForeground", "white")

    def create_slider(self, parent):
        self.slider = ttk.Scale(
            parent,
            from_=0,
            to=100,
            orient="horizontal",
            style="Modern.Horizontal.TScale",
            length=200,
        )
        self.slider.pack()

    def create_progress_bar(self, parent):
        self.progress = ttk.Progressbar(
            parent,
            style="Modern.Horizontal.TProgressbar",
            length=200,
            mode="determinate",
        )
        self.progress.pack()
        self.progress["value"] = 50

    def create_checkbox(self, parent):
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(
            parent,
            text="Check me",
            style="Modern.TCheckbutton",
            variable=self.checkbox_var,
        )
        self.checkbox.pack()

    def create_entry_field(self, parent):
        self.entry = ttk.Entry(parent, style="Modern.TEntry", width=30)
        self.entry.pack()

    def create_text_widget(self, parent):
        text_frame = tk.Frame(parent, bg="#363739")
        text_frame.pack(pady=10)

        self.text_widget = tk.Text(
            text_frame,
            wrap=tk.WORD,
            width=30,
            height=5,
            font=("Roboto", 10),
            bg="white",
            fg="#363739",
            insertbackground="#F69728",
        )
        self.text_widget.pack(side=tk.LEFT)

        scrollbar = ttk.Scrollbar(
            text_frame,
            orient="vertical",
            command=self.text_widget.yview,
            style="Modern.Vertical.TScrollbar",
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_widget.config(yscrollcommand=scrollbar.set)

    def button_clicked(self):
        print("Button clicked!")

    def update_radial_buttons(self):
        for child in self.winfo_children():
            if isinstance(child, ttk.Radiobutton):
                if child.cget("value") == self.radio_var.get():
                    child.circle.itemconfig(2, fill="white")
                else:
                    child.circle.itemconfig(2, fill="#363739")


if __name__ == "__main__":
    app = ModernGUI()
    app.mainloop()
