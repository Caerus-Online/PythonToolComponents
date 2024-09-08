import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont


def apply_modern_style(root):
    style = ttk.Style(root)
    style.theme_use("default")

    style.configure(".", background="#363739", foreground="white", font=("Roboto", 10))

    style.configure(
        "Modern.TButton",
        background="#F69728",
        foreground="white",
        font=("Roboto", 12, "bold"),
        borderwidth=0,
        relief="raised",
        padding=10,
        highlightthickness=0,
    )
    style.map(
        "Modern.TButton",
        background=[("active", "#CC7C22")],
        foreground=[("active", "white")],
    )

    style.layout(
        "Modern.TRadiobutton",
        [
            (
                "Radiobutton.padding",
                {
                    "children": [
                        ("Radiobutton.indicator", {"side": "left", "sticky": ""}),
                        ("Radiobutton.label", {"sticky": "w"}),
                    ],
                    "sticky": "w",
                },
            )
        ],
    )
    style.configure(
        "Modern.TRadiobutton",
        background="#363739",
        foreground="white",
        font=("Roboto", 10, "bold"),
        indicatorcolor="#F69728",  # Initial indicator color
        padding=5,
    )
    style.map(
        "Modern.TRadiobutton",
        background=[
            ("active", "#363739"),
            ("selected", "#363739"),
            ("hover", "#363739"),
        ],
        foreground=[
            ("active", "#EF8619"),
            ("selected", "white"),
            ("hover", "#EF8619"),
        ],
        indicatorcolor=[
            ("selected", "white"),
            ("hover", "white"),
        ],
    )

    style.configure(
        "Modern.TCombobox",
        fieldbackground="white",
        foreground="#363739",
        selectbackground="#F69728",
        selectforeground="white",
        font=("Roboto", 10, "bold"),
        arrowsize=0,
    )
    style.map(
        "Modern.TCombobox",
        fieldbackground=[("readonly", "white")],
        foreground=[("readonly", "#363739")],
        selectbackground=[("readonly", "#F69728"), ("hover", "#F69728")],
        selectforeground=[("readonly", "white"), ("hover", "white")],
    )

    # Configure Modern.Horizontal.TScale
    style.configure(
        "Modern.Horizontal.TScale",
        troughcolor="#363739",
        slidercolor="#F69728",
        background="#F69728",
    )
    style.map(
        "Modern.Horizontal.TScale",
        slidercolor=[("active", "#CC7C22")],
    )

    # Configure Modern.Horizontal.TProgressbar
    style.configure(
        "Modern.Horizontal.TProgressbar",
        troughcolor="#363739",
        background="#F69728",
        bordercolor="#363739",
    )

    # Configure Modern.TCheckbutton
    style.configure(
        "Modern.TCheckbutton",
        background="#363739",
        foreground="white",
        font=("Roboto", 16, "bold"),
        indicatorcolor="#F69728",
        padding=6,
    )
    style.map(
        "Modern.TCheckbutton",
        background=[("active", "#363739"), ("selected", "#363739")],
        foreground=[("active", "#EF8619"), ("selected", "white")],
        indicatorcolor=[("selected", "white"), ("hover", "#F69728")],
    )

    # Configure Modern.TEntry
    style.configure(
        "Modern.TEntry",
        fieldbackground="white",
        foreground="#363739",
        insertcolor="#F69728",
        font=("Roboto", 10, "bold"),
        borderwidth=0,
        relief="flat",
    )

    # Configure Modern.Vertical.TScrollbar
    style.configure(
        "Modern.Vertical.TScrollbar",
        troughcolor="#363739",
        background="#F69728",
        bordercolor="#363739",
        arrowcolor="white",
    )
    style.map(
        "Modern.Vertical.TScrollbar",
        background=[("active", "#CC7C22")],
    )

    # Configure Modern.MenuBar
    style.configure(
        "Modern.MenuBar.TButton",
        background="#F69728",
        foreground="white",
        font=("Roboto", 12, "bold"),
        borderwidth=0,
        relief="flat",
        padding=(10, 5),
    )
    style.map(
        "Modern.MenuBar.TButton",
        background=[("active", "#CC7C22")],
        foreground=[("active", "white")],
    )
