import customtkinter as ctk
from PIL import Image

ctk.set_default_color_theme("./custom_theme.json")  # Make sure you have custom_theme.json file in current directory.

status_icons = {
    "info": ctk.CTkImage(
        light_image=Image.open("./icons/info_light.png"),
        dark_image=Image.open("./icons/info_dark.png"),
        size=(30, 30)
    ),
    "error": ctk.CTkImage(
        light_image=Image.open("./icons/error_light.png"),
        dark_image=Image.open("./icons/error_dark.png"),
        size=(30, 30)
    ),
    "warning": ctk.CTkImage(
        light_image=Image.open("./icons/warning_light.png"),
        dark_image=Image.open("./icons/warning_dark.png"),
        size=(30, 30)
    ),
    "success": ctk.CTkImage(
        light_image=Image.open("./icons/success_light.png"),
        dark_image=Image.open("./icons/success_dark.png"),
        size=(30, 30)
    )
}


class Alert(ctk.CTkFrame):
    def __init__(self, parent, title: str, message_text: str, status: str = "info"):
        super().__init__(
            parent,
            width=420,
            height=172,
            fg_color=("#f7f8fa", "#2b2d30"),
            border_color=("#d3d5db", "#43454a"),
            border_width=2
        )

        default_icon = status_icons["info"]

        title_label = ctk.CTkLabel(
            self,
            text=title,
            image=status_icons.get(status, default_icon),
            compound="left",
            width=360,
            anchor="nw",
            font=("Inter", 18, "bold")
        )
        title_label.grid(row=0, column=0, padx=20, pady=(20, 0))

        message_text = ctk.CTkLabel(
            self,
            text=message_text,
            width=300,
            height=80,
            anchor="nw",
            font=("Inter", 14)
        )
        message_text.grid(row=1, column=0, padx=20, pady=(20, 0))

        ok_btn = ctk.CTkButton(
            self,
            width=100,
            text="OK",
            command=self.hide_alert,
        )
        ok_btn.grid(row=2, column=1, padx=10, pady=10, sticky="se")

    def show_alert(self):
        self.pack(anchor="center", expand=True)

    def hide_alert(self):
        self.destroy()


# Usage
# alert = Alert(
#     parent=self,
#     title="This is title",
#     message_text="This is info alert. Available alerts: Warning, Error and Success",
#     status="info",
# )
# alert.show_alert()


close_icon = ctk.CTkImage(
    light_image=Image.open("./icons/close_light.png"),
    dark_image=Image.open("./icons/close_dark.png"),
    size=(26, 26)
)


class Notification(ctk.CTkFrame):
    def __init__(self, parent, title: str, message_text: str, status: str = "info"):
        super().__init__(
            parent,
            width=360,
            height=118,
            fg_color=("#f7f8fa", "#2b2d30"),
            border_color=("#d3d5db", "#43454a"),
            border_width=2
        )

        close_btn = ctk.CTkButton(
            self,
            width=35,
            height=35,
            text="",
            fg_color=("#f7f8fa", "#2b2d30"),
            hover=False,
            image=close_icon,
            command=self.hide_notification,
        )
        close_btn.grid(row=0, column=1, padx=10, pady=10, sticky="se")

        default_icon = status_icons["info"]

        title_label = ctk.CTkLabel(
            self,
            text=title,
            image=status_icons.get(status, default_icon),
            compound="left",
            width=360,
            anchor="nw",
            font=("Inter", 16, "bold")
        )
        title_label.grid(row=0, column=0, padx=20, pady=(20, 5))

        message_text = ctk.CTkLabel(
            self,
            text=message_text,
            width=300,
            anchor="nw",
            font=("Inter", 12)
        )
        message_text.grid(row=1, column=0, padx=20, pady=(5, 20))

    def show_notification(self):
        self.pack(anchor="se", expand=True, padx=10, pady=10)

    def hide_notification(self):
        self.destroy()

# Usage
# notification = Notification(
#     parent=self,
#     title="This is title",
#     message_text="This is info notification. Available notifications: Warning, Error and Success",
#     status="info",
# )
# notification.show_notification()
