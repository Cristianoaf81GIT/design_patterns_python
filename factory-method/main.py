from creators import WebDialog
from creators import WindowsDialog


def main():
    machine_os = "windows"
    
    if machine_os == "windows":
        dialog = WindowsDialog()
        button = dialog.create_button()
        button.render()
        button.on_click("CLOSE")
    elif machine_os == "web":
        dialog = WebDialog()
        button = dialog.create_button()
        button.render()
        button.on_click("CLOSE")
    else:
        print("Unkown operating system")


if __name__ == "__main__":
    main()
