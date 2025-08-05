from flask import Blueprint, render_template
import os

views = Blueprint('views', __name__)

@views.route("/")
def home():
    image_folder = os.path.join('static', 'images')
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg')
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)]
    titles = [  
            "t1",
            "t2",
            "t3",
            "t4",
            "t5",
            "t6",
            "t7",
            "t8",
            "t9",
            "t10",
            "t11",
            "t12",
            "t13",
            "t14",
            "t15",
            "t16",
            "t17",
            "t18",
            "t19",
            "t20",
            "t21",
            "t22",
            "t23",
            "t24",
            "t25",
            "t26",
            "t27",
            "t28",
            "t29",
            "t30",
            "t31",
            "t32",
            "t33",
            "t34",
            "t35",
            "t36",
            "t37",
            "t38",
            "t39",
            "t40",
            "t41",
            "t42",
            "t43",
            "t44",
            "t45"
        ]
    prices = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "40",
            "41",
            "42",
            "43",
            "44",
            "45",
        ]       

    return render_template("index.html", name="Alan", image_filenames=images, titles=titles, prices=prices )  # Pass images to template

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")