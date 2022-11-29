from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Empire_Class import EmpireFinder
from IMBb_Class import ImbFinder
from Netflix_Class import NetflixFinder

LB_FONT = ("Helvetica", 15, "bold")
CT_FONT = ("Helvetica", 12, "bold")
QUANTITY = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
CATEGORY = ("Netflix", "IMBb", "EMPIRE")


class FavouriteFilm:
    def __init__(self, window):
        self.window = window
        self.window.title("Film Finder App")
        self.window.geometry("465x650")
        self.window.configure(bg="khaki")
        # extra:
        self.empire_tool = EmpireFinder()
        self.imb_tool = ImbFinder()
        self.netflix_tool = NetflixFinder()
        self.movies = None
        self.number = StringVar()
        self.source = StringVar()

        # ============== image label ================== #
        self.head_label = Label(self.window, text="Find Your Favourite Movie", font=LB_FONT, justify="center",
                                bg="khaki", bd=2, highlightthickness=2, relief=RIDGE)
        self.head_label.place(x=6, y=5, width=453, height=40)

        used_image = Image.open("IMG/film.png")
        used_photo = ImageTk.PhotoImage(used_image)
        self.image_label = Label(self.window, image=used_photo)
        self.image_label.image = used_photo
        self.image_label.place(x=5, y=50)

        # =============== main frame =======================#
        self.main_frame = Frame(self.window, bd=2, highlightthickness=2, relief=RIDGE)
        self.main_frame.place(x=3, y=340, width=457, height=300)

        # ============ list widget on the left ============= #
        self.film_label = Label(self.main_frame, text="Movie List", font=("Helvetica", 12, "bold"), justify="center",
                                bd=1, highlightthickness=1, relief=RIDGE)
        self.film_label.place(x=5, y=5, width=215, height=40)

        self.movie_list = Listbox(self.main_frame, bd=1, highlightthickness=1, relief=RIDGE, activestyle='dotbox',
                                  font=CT_FONT)
        self.movie_list.place(x=5, y=50, width=215, height=238)

        # ============ specification section on the right ============= #
        self.feature_label = Label(self.main_frame, text="Specifications", font=("Helvetica", 12, "bold"),
                                   justify="center", bd=1, highlightthickness=1, relief=RIDGE)
        self.feature_label.place(x=225, y=5, width=220, height=40)

        self.source_label = Label(self.main_frame, text="Source", font=("Helvetica", 12, "bold"), justify="center",
                                  bd=1, highlightthickness=1, relief=RIDGE, fg="navy")
        self.source_label.place(x=225, y=50, width=95, height=30)

        self.source_box = ttk.Combobox(self.main_frame, justify="center", font=CT_FONT, textvariable=self.source)
        self.source_box["values"] = CATEGORY
        self.source_box.current(0)
        self.source_box.place(x=330, y=50, width=115, height=30)

        self.number_label = Label(self.main_frame, text="Top", font=CT_FONT, justify="center", fg="navy",
                                  bd=1, highlightthickness=1, relief=RIDGE)
        self.number_label.place(x=225, y=85, width=95, height=30)

        self.number_box = ttk.Combobox(self.main_frame, justify="center", font=CT_FONT, textvariable=self.number)
        self.number_box["values"] = QUANTITY
        self.number_box.current(9)
        self.number_box.place(x=330, y=85, width=115, height=30)

        find_image = Image.open("IMG/find.png")
        find_photo = ImageTk.PhotoImage(find_image)
        self.search_button = Button(self.main_frame, image=find_photo, bg="light cyan", command=self.search_method)
        self.search_button.image = find_photo
        self.search_button.place(x=250, y=136, width=150, height=80)

        exit_image = Image.open("IMG/exit.png")
        exit_photo = ImageTk.PhotoImage(exit_image)
        self.close_button = Button(self.main_frame, image=exit_photo, bg="moccasin", command=self.close_method)
        self.close_button.image = exit_photo
        self.close_button.place(x=225, y=237, width=220, height=50)

    # ============================ FUNCTIONALITY ============================== #
    def close_method(self):
        confirm = messagebox.askyesno(title="Favourite Movie Finder", message="Do You Want To Close The Program?")
        if confirm > 0:
            self.window.destroy()
            return
        else:
            pass

    def search_method(self):
        # always executes:
        self.movie_list.delete(0, END)

        # if-else conditional:
        if self.source.get() == "EMPIRE":
            self.movies = self.empire_tool.get_data(self.number.get())
            self.movie_list.config(fg="dark green")
        elif self.source.get() == "IMBb":
            self.movies = self.imb_tool.get_data(self.number.get())
            self.movie_list.config(fg="dark slate blue")
        elif self.source.get() == "Netflix":
            self.movies = self.netflix_tool.get_data(self.number.get())
            self.movie_list.config(fg="firebrick")

        # always executes:
        number = 1
        for film in self.movies:
            self.movie_list.insert(number, f"{number}) {film}")
            number += 1


def launch_app():
    app = Tk()
    FavouriteFilm(app)
    app.mainloop()


if __name__ == "__main__":
    launch_app()
