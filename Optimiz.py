import customtkinter as ctk
import requests
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def change_theme(theme):
    themes = {
        "Thème bleu": {"bg": "#1E90FF", "text": "white"},
        "Thème noir": {"bg": "#000000", "text": "white"},
        "Thème discord": {"bg": "#7289DA", "text": "white"},
        "Thème snapchat": {"bg": "#FFFC00", "text": "black"},
        "Thème instagram": {"bg": "#E1306C", "text": "white"},
        "Thème tiktok": {"bg": "#010101", "text": "white"},
        "Thème fortnite": {"bg": "#1B47FF", "text": "white"},
        "Thème five m": {"bg": "#F7931A", "text": "white"},
        "Thème hacker": {"bg": "#00FF00", "text": "black"},
        "Thème jaune": {"bg": "#FFD700", "text": "black"},
    }

    if theme in themes:
        selected_theme = themes[theme]
        root.configure(bg=selected_theme["bg"])

        for widget in root.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                widget.configure(bg_color=selected_theme["bg"], text_color=selected_theme["text"])
            elif isinstance(widget, ctk.CTkButton):
                widget.configure(fg_color=selected_theme["bg"], text_color=selected_theme["text"])
            elif isinstance(widget, ctk.CTkOptionMenu):
                widget.configure(fg_color=selected_theme["bg"], button_color=selected_theme["bg"], text_color=selected_theme["text"])

def send_discord_message(discord_id):
    # Message à envoyer
    message_content = f"<@{discord_id}> a utilisé l'optimisation"

    # Envoyer le message au webhook Discord
    response = requests.post(
        "https://discord.com/api/webhooks/1296163525441486922/f_yK3dNmrJIP2EeeDFL6tWka06MPbkH5xJXdT6DY8YHA4N0WtZa9q-0E8b7Wez71_kvI",
        json={"content": message_content}
    )

    # Vérification de la réponse
    if response.status_code == 200:
        print("Message envoyé avec succès!")
    else:
        print(f"Erreur lors de l'envoi : {response.status_code}, {response.text}")

def start_message_sending():
    discord_id = "YOUR_DISCORD_ID"  # Remplacez par l'ID Discord que vous souhaitez utiliser
    # Démarrer l'envoi dans un thread séparé
    threading.Thread(target=send_discord_message, args=(discord_id,)).start()

def create_gui():
    global root
    root = ctk.CTk()
    root.title("𝗦𝗸𝘆𝗱𝗲𝗿 𝗢𝗽𝘁𝗶𝗺𝗶𝘇")
    root.geometry("400x300")

    label = ctk.CTkLabel(root, text="𝗦𝗸𝘆𝗱𝗲𝗿 𝗢𝗽𝘁𝗶𝗺𝗶𝘇", font=ctk.CTkFont(size=25, weight="bold"))
    label.pack(pady=10)

    theme_label = ctk.CTkLabel(root, text="Choisir un thème:")
    theme_label.pack(pady=5)

    theme_var = ctk.StringVar(value="Thème bleu")
    theme_menu = ctk.CTkOptionMenu(root, variable=theme_var, values=["Thème bleu", "Thème noir", "Thème discord", "Thème snapchat", "Thème instagram", "Thème tiktok", "Thème fortnite", "Thème five m", "Thème hacker", "Thème jaune"], command=lambda choice: change_theme(choice))
    theme_menu.pack(pady=10)

    quality_label = ctk.CTkLabel(root, text="By 𝘽𝙚𝙡𝙡𝙖𝙢𝙮")
    quality_label.pack(pady=10)

    quality_var = ctk.StringVar(value="𝗟𝗼𝘄")
    quality_menu = ctk.CTkOptionMenu(root, variable=quality_var, values=["𝗟𝗼𝘄", "𝗠𝗲𝗱𝗶𝘂𝗺", "𝗛𝗶𝗴𝗵", "𝗨𝗹𝘁𝗿𝗮"])
    quality_menu.pack(pady=10)

    apply_button = ctk.CTkButton(root, text="𝗔𝗽𝗽𝗹𝗶𝗾𝘂𝗲𝗿 𝗹𝗲𝘀 𝗽𝗮𝗿𝗮𝗺𝗲𝘁𝗿𝗲𝘀", width=210, height=40, font=ctk.CTkFont(size=15))
    apply_button.pack(pady=10)

    launch_button = ctk.CTkButton(root, text="𝗘𝗻𝘁𝗿𝗲𝗿 𝗲𝘁 𝗲𝗻𝘃𝗼𝘆𝗲𝗿 𝗹'𝗼𝗽𝘁𝗶𝗺𝗶𝘇𝗮𝘁𝗶𝗼𝗻", width=210, height=40, font=ctk.CTkFont(size=15), command=start_message_sending)
    launch_button.pack(pady=10)

    change_theme("Thème bleu")

    root.mainloop()

create_gui()
