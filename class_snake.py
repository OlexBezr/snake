import random

class Snake: 

	# ------- COLORS
	FRUIT_COLOR = (198,17,51)
	BIG_FRUIT_COLOR = (208,237,255)
	SNAKE_COLOR = (104,157,87)

	BG_MENU = (59,66,73)
	FONT_COLOR_MENU = (112,126,137)

	GAME_BG_COLOR = (36,39,45)
	# ------- COLORS

	def __init__(self):
		self.mini_menu_height = 100
		
		self.pixel_param = 20
		
		self.score = 0
  
		self.count_points_for_fruit = 10
		self.count_points_for_big_fruit = 110

		self.fruit_pos = None 
		self.big_fruit_pos = None

		self.movement_position = 'Right'
 
		self.arr_snake = self.new_snake()

	def check_snake_arr(self) :
		print('----')
		i = 0
		for snake_pixel in self.arr_snake:
			i+=1
			print(str(i)+'||x-'+str(snake_pixel['x'])+":::"+'y-'+str(snake_pixel['y']))
		print('----')
   
		
	def draw_background(self, pg, screen) :
		bg = pg.Surface(screen.get_size())
		bg.fill(self.GAME_BG_COLOR)
		screen.blit( bg, (0, 0) )
  

	def events(self, pg, event) :
		event_do = 0
  
		# event_id_do - совершено ли действие за тик
		if event.type == pg.KEYDOWN : 
			
			if self.movement_position != 'Left' :
				if event.key == pg.K_RIGHT :
					event_do = 1
					self.movement_position = 'Right'

			if self.movement_position != 'Up' :
				if event.key == pg.K_DOWN :
					event_do = 1
					self.movement_position = 'Down'
     

			if self.movement_position != 'Right' :
				if event.key == pg.K_LEFT :
					event_do = 1
					self.movement_position = 'Left'

			if self.movement_position != 'Down' :
				if event.key == pg.K_UP:
					event_do = 1
					self.movement_position = 'Up'
		
		return event_do

	def create_fruit(self, screen):
		pos = (random.randrange(0, screen.get_size()[0], self.pixel_param), random.randrange(self.mini_menu_height, screen.get_size()[1], self.pixel_param))
		for pixel_snake in self.arr_snake:
			if pos[0] == pixel_snake['x'] and  pos[1] == pixel_snake['y']:
				return self.create_fruit(screen)
		return pos

	def draw_fruit(self, pg, screen):
		pg.draw.rect(screen, self.FRUIT_COLOR, (self.fruit_pos[0], self.fruit_pos[1], self.pixel_param, self.pixel_param))

	
	def create_big_fruit(self, screen):
		# Большой фрукт будет занимать 4 инровых пикселей
		# поетому позиция будет хранить координаты сразу 4х фруктов, за который дается больше очков чем за обычный фрукт
		
		pos = (random.randrange(0, screen.get_size()[0], self.pixel_param), random.randrange(self.mini_menu_height, screen.get_size()[1], self.pixel_param))
		for pixel_snake in self.arr_snake:
			if pos[0] == pixel_snake['x'] and  pos[1] == pixel_snake['y']:
				return self.create_big_fruit(screen)

		four_pos = [
			pos , (pos[0] + self.pixel_param, pos[1]),
			(pos[0], pos[1] + self.pixel_param), (pos[0] + self.pixel_param, pos[1] + self.pixel_param)
		]
		return four_pos
	
	def draw_big_fruit(self, pg, screen):

		# большой фрукт должен находится не более 10 сек на поле
		# должен появлятся каждые 100 очков
		# дополнительно: нарисовать счетчик который заполняется, и показывает появление большого фрукта 

		for fruit_pos in self.big_fruit_pos :
			pg.draw.rect(screen, self.BIG_FRUIT_COLOR, (fruit_pos[0], fruit_pos[1], self.pixel_param, self.pixel_param))

	
	def eat_fruit(self) :
		
		
		if self.fruit_pos == None:
			return
		if self.arr_snake[-1]['x'] == self.fruit_pos[0] and self.arr_snake[-1]['y'] == self.fruit_pos[1]:
			self.fruit_pos = None

			self.arr_snake.insert(0, {
				'x': self.arr_snake[-1]['x'],
				'y': self.arr_snake[-1]['y'],
				'color': self.SNAKE_COLOR
			})

			self.score += self.count_points_for_fruit
	
	def eat_big_fruit(self) :
		if self.big_fruit_pos == None:
			return
		for fruit_pos in self.big_fruit_pos:
		
			if self.arr_snake[-1]['x'] == fruit_pos[0] and self.arr_snake[-1]['y'] == fruit_pos[1]:
				self.big_fruit_pos = None

				for i in range(0,3) :
		
					self.arr_snake.insert(0, {
						'x': self.arr_snake[-1]['x'],
						'y': self.arr_snake[-1]['y'],
						'color': self.SNAKE_COLOR
					})

				self.score += self.count_points_for_big_fruit
				return 
	def check_fruits(self, pg, screen) :
		self.eat_fruit()
		if self.fruit_pos == None :
			self.fruit_pos = self.create_fruit(screen)
			self.draw_fruit(pg, screen)
		else: 
			self.draw_fruit(pg, screen)
	
		self.eat_big_fruit()

		if self.big_fruit_pos == None and self.score % 100 == 0 and self.score != 0:
			self.big_fruit_pos = self.create_big_fruit(screen)
			self.draw_big_fruit(pg, screen)
		elif self.big_fruit_pos != None: 
			self.draw_big_fruit(pg, screen)
   
	def new_snake(self) :
		snake = []
		for i in range(0, 3):
			snake.append({
				'x':100,
				'y': self.mini_menu_height + self.pixel_param,
				'color': self.SNAKE_COLOR
			})
		return snake

		
	def draw_snake(self, pg, screen):
		for pixel_snake in self.arr_snake:
			pg.draw.rect(screen, pixel_snake["color"], (pixel_snake["x"], pixel_snake["y"], self.pixel_param, self.pixel_param))
		
	def move_snake(self, screen):
		
		temp_pixel_snake = self.arr_snake.pop(0)

		if self.movement_position == 'Right' :
			temp_pixel_snake['x'] = self.arr_snake[-1]['x'] + self.pixel_param
			temp_pixel_snake['y'] = self.arr_snake[-1]['y']
			if screen.get_size()[0] - self.pixel_param <= self.arr_snake[-1]['x']:
				temp_pixel_snake['x'] = 0
				
	
		if self.movement_position == 'Left' :
			temp_pixel_snake['x'] = self.arr_snake[-1]['x'] - self.pixel_param
			temp_pixel_snake['y'] = self.arr_snake[-1]['y']
			if 0 >= self.arr_snake[-1]['x']:
				temp_pixel_snake['x'] = screen.get_size()[0] - self.pixel_param
	
		if self.movement_position == 'Up' :
			temp_pixel_snake['y'] = self.arr_snake[-1]['y'] - self.pixel_param
			temp_pixel_snake['x'] = self.arr_snake[-1]['x']
			if self.mini_menu_height >= self.arr_snake[-1]['y']: 
				temp_pixel_snake['y'] = screen.get_size()[1] - self.pixel_param
	
		if self.movement_position == 'Down' :
			temp_pixel_snake['y'] = self.arr_snake[-1]['y'] + self.pixel_param
			temp_pixel_snake['x'] = self.arr_snake[-1]['x']
			if screen.get_size()[1] - self.pixel_param <= self.arr_snake[-1]['y']:
				temp_pixel_snake['y'] = self.mini_menu_height
	

		self.arr_snake.append(temp_pixel_snake)

	def draw_mini_menu(self, pg, screen): 
		pg.draw.rect(screen, self.BG_MENU, [0, 0 ,screen.get_size()[0], self.mini_menu_height])
	
		score_font_size = 30
		font_score = pg.font.Font(None, score_font_size)
		text_score = font_score.render( 'Score: ' + str(self.score), True, self.FONT_COLOR_MENU )

		screen.blit( text_score, ( 50, ( self.mini_menu_height -score_font_size ) / 2 ) )

	def new_game(self) :
		self.arr_snake = self.new_snake()
		self.movement_position = 'Right'
		self.fruit_pos = None
		self.big_fruit_pos = None
		self.score = 0
	
	def game_over(self):
		for pixel_snake in self.arr_snake :
			if len(self.arr_snake)-1 == self.arr_snake.index(pixel_snake):
				return 1
			if self.arr_snake[-1]['x'] == pixel_snake['x'] and self.arr_snake[-1]['y'] == pixel_snake['y']:
				self.new_game()
				return 0
		return 1

