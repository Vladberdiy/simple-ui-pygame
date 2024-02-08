from pygame import *


class Button:
	def __init__(self, surf, text, pos, size_font=16, txt_font=None, color_bg=(255, 255, 255), color_txt=(0, 0, 0), hover_color=(169, 169, 169)):
		font.init()
		

		self.txt_font = txt_font
		self.text = text
		self.size_font = size_font
		self.surf = surf
		self.color_bg = color_bg
		self.color_txt = color_txt
		self.hover_color = hover_color
		self.pos = pos		
		self.font_create = font.Font(self.txt_font, self.size_font)
		self.font_rend = self.font_create.render(self.text, True, self.color_txt)
		self.text_width, self.text_height = self.font_rend.get_size()
		self.width_btn = self.text_width + 15
		self.height_btn = self.text_height + 10
		self.text_x = self.pos[0] + (self.width_btn - self.text_width) // 2
		self.text_y = self.pos[1] + (self.height_btn - self.text_height) // 2
		self.size = (self.width_btn, self.height_btn)
		self.rect = Rect(self.pos, self.size)
		self.txt_rect = Rect((self.text_x, self.text_y), (self.text_width, self.text_height))



	def draw(self):


		mouse_x, mouse_y = mouse.get_pos()
		is_hovered = self.rect.collidepoint(mouse_x, mouse_y)

		if is_hovered:
			draw.rect(self.surf, self.hover_color, self.rect)
			self.surf.blit(self.font_rend, self.txt_rect)
		else:
			draw.rect(self.surf, self.color_bg, self.rect)
			self.surf.blit(self.font_rend, self.txt_rect)


	def pressed(self, event, func=None):
		
		self.func = func

		
		mousePos = mouse.get_pos()
		if self.rect.collidepoint(mousePos):

			if mouse.get_pressed(num_buttons=3)[0]:
				if self.func != None:
					self.func()
					return True


class Img:
	def __init__(surf, src, pos):
		self.surf = surf
		self.src = src
		self.pos = pos
		self.img = image.load(self.src)
	
	def draw(self):
		self.surf.blit(self.img, self.pos)
	
	def scale(self, w, h):
		self.w = w
		self.h = h
		transform.scale(self.img, (self.w, self.h))
	
	def rotate(self, angle):
		self.angle = angle
		transform.rotate(self.img, self.angle)



class Label:
	def __init__(self, surf, text, pos, font_label=None, font_size=16, font_color=(0, 0, 0)):
		font.init()
		
		self.surf = surf
		self.text = text
		self.pos = pos
		self.font_label = font_label
		self.font_size = font_size
		self.font_color = font_color
		self.font_create = font.Font(self.font_label, self.font_size)
		self.font_rend = self.font_create.render(self.text, True, self.font_color)
		self.text_width, self.text_height = self.font_rend.get_size()
		self.rect = Rect(self.pos, (self.text_width, self.text_height))

	def draw(self):

		self.surf.blit(self.font_rend, self.rect)




