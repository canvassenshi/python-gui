import tkinter as tk
import requests
import shutil
import os
from PIL import ImageTk, Image


''' GUI '''

root = tk.Tk()
root.title('Shiba Inu')


canvas = tk.Canvas(height=800, width=1200)
canvas.pack()

top_frame = tk.Frame(root, bg='#FA8072', bd=5)
top_frame.place(relx=0.2, rely=0.1, relheight=0.2, relwidth=0.6)

top_label = tk.Label(top_frame, bg='#FA8072', text='You like shiba inu???', font=('Arial Italic', 32))
top_label.place(relx=0.5, rely=0.02, relheight=0.6, relwidth=1, anchor='n')

image_frame = tk.Frame(root, bg='#FA8072', bd=10)
image_frame.place(relx=0.1, rely=0.35, relheight=0.55, relwidth=0.8)


def show_image(frame, root):

	url_api = 'http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true'
	response = requests.get(url_api)
	data = response.json()

	url_img = data[0]

	r = requests.get(url_img, stream = True)
	if r.status_code == 200:
	    r.raw.decode_content = True
	    with open('./shibaimg/shiba.png','wb') as f:
	        shutil.copyfileobj(r.raw, f)

	shiba_image = ImageTk.PhotoImage(Image.open('./shibaimg/shiba.png'))
	shiba_label = tk.Label(frame, image=shiba_image)
	shiba_label.photo = shiba_image 
	shiba_label.place(relwidth=1, relheight=1)

	os.remove('./shibaimg/shiba.png')


top_button = tk.Button(top_frame, text='GIVE ME DOGGO', font=('Arial Bold', 12), command=lambda: show_image(image_frame, root))
top_button.place(relx=0.5, rely=0.65, relheight=0.3, relwidth=1, anchor='n')


root.mainloop()







