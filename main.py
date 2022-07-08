import pygame as pg
import sys 

from class_snake import Snake
from class_menu import Menu


pg.init()
pg.mixer.init()
pg.display.set_caption("snake 54")

pixels_in_row = 40

temp_screen_size = (800,600)
screen = pg.display.set_mode(temp_screen_size)

clock = pg.time.Clock()

_snake = Snake()
_menu = Menu()



def floor_by_pixel_param( num, pixel_param) :
	if num % pixel_param < pixel_param/2 :
		return num - (num % pixel_param)
	elif num % pixel_param > pixel_param/2 :
		# temp 
		# while num % self.pixel_param != 0:
		return num - (num % pixel_param) + pixel_param
	else: 
		return num

_snake.pixel_param = floor_by_pixel_param(temp_screen_size[0] / pixels_in_row, 5)

game_on_pause = False

snake_work = 1

event_do_in_tick = 0 # что бы можно было совершить только одно действие за тик

while snake_work:
	clock.tick(10)
	event_do_in_tick = 0
	for event in pg.event.get():
		if event.type == pg.QUIT : 
			sys.exit()
		if event.type == pg.KEYDOWN : 

			if event.key == pg.K_SPACE:
				if game_on_pause : 
					game_on_pause = False
				else: game_on_pause = True
   
		# if event.type == pg.WINDOWRESIZED :
		# 	_snake.pixel_param = floor_by_pixel_param(int(event.x / pixels_in_row), 5)
		# 	screen = pg.display.set_mode((floor_by_pixel_param(event.x, _snake.pixel_param),floor_by_pixel_param(event.y, _snake.pixel_param)), pg.RESIZABLE)
		if not event_do_in_tick:
			event_do_in_tick = _snake.events(pg, event)

	if not game_on_pause :
		_snake.draw_background(pg, screen)
		_snake.draw_mini_menu(pg, screen)
		_snake.check_fruits(pg, screen)
		_snake.draw_snake(pg, screen)
		_snake.move_snake(screen)
		# _snake.check_snake_arr()
  
		snake_work = _snake.game_over()
  
  
	elif game_on_pause:
		_snake.draw_background(pg, screen)
		_snake.draw_mini_menu(pg, screen)
		_snake.draw_snake(pg, screen)
  
		_menu.draw_menu(pg, screen)
  
		score_font_size = 30
		font_score = pg.font.Font(None, 60)
		text_score = font_score.render( 'PAUSE', True, (0,0,0) )
		screen.blit( text_score, ( screen.get_size()[0] /2, screen.get_size()[1] /2) )

	pg.display.flip()
