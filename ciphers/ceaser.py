from tkinter import *
class Application(Frame):
	
	def __init__(self,master):
		super(Application,self).__init__(master)
		self.grid()
		self.create_widgets()
		self.typing = ''

	def create_widgets(self):
		
		self.pw_lbl = Label(self,text = "Phrase: ")
		self.pw_lbl.grid(row=1,column=0,sticky=W)
		self.pw_ent = Entry(self)
		self.pw_ent.grid(row=1,column=1,sticky=W)

		self.pw_key_lbl = Label(self,text='Key:')
		self.pw_key_lbl.grid(row=2,column=0,sticky=W)
		self.pw_key = Entry(self)
		self.pw_key.grid(row=2,column=1,sticky=W)
		self.submit_btn=Button(self, text="GO", command=self.reveal)
		self.submit_btn.grid(row = 5, column=0, sticky=W)
		self.type_of_encrypt=StringVar()
		self.type_of_encrypt.set(None)
		Radiobutton(self,
			text="Decrypt",
			variable=self.type_of_encrypt,
			value="decrypt",
			command=self.update_text
			).grid(row=3,column=0,sticky=W)
		Radiobutton(self,
			text="Encrypt",
			variable=self.type_of_encrypt,
			value="encrypt",
			command=self.update_text
			).grid(row=4,column=0,sticky=W)
		

		self.secret_txt = Text(self, width=34, height=15,wrap = WORD)
		self.secret_txt.grid(row=6,column=0,columnspan=2,sticky=W)

	def update_text(self):
		self.typing = self.type_of_encrypt.get()

	def reveal(self):
		alphabet = []
		for i in range(256):
			alphabet.append(chr(i))
		contents = self.pw_ent.get()
		key = int(self.pw_key.get())
		result = ''
		if self.typing == 'encrypt':
			for b in contents:
				for a in alphabet:
					if a==b:
						result+=(chr(ord(a)+key))
		elif self.typing == 'decrypt':
			for b in contents:
				for a in alphabet:
					if a==b:
						result+=(chr(ord(a)-key))
		
		
		self.secret_txt.delete(0.0,END)
		self.secret_txt.insert(0.0, result)

			

root = Tk()
root.title('Дешифратор')
root.geometry('250x350')

app = Application(root)
root.mainloop()