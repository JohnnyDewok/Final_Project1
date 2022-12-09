from controller import *

def main():
    window = Tk()
    window.title('TV')
    window.geometry('350x250')
    window.resizable(True, True)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()