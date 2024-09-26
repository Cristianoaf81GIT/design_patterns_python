from configs import GuiConfig, read_application_config_file
from factories import GuiFactory, WinFactory, LinuxFactory
from clients import ApplicationGui


def main():
    config: GuiConfig = read_application_config_file()
    factory: GuiFactory 

    if config.get("OS") == "windows":
        factory = WinFactory()
    elif config.get("OS") == "linux":
        factory = LinuxFactory()
    else:
        raise Exception("Unkown operating system")

    application = ApplicationGui(factory)
    application.create_ui()
    application.paint()



if __name__ == "__main__":
    main()
