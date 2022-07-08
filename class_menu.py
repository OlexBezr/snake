
class Menu:
	TRANSPERENT_BG_MENU = (0,0,0,40)
	def draw_menu(self, pg, screen) :
		pg.draw.rect(screen, self.TRANSPERENT_BG_MENU, (0,0, screen.get_size()[0], screen.get_size()[1]))