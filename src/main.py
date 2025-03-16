from gamestate import *
# import faulthandler

if __name__ == "__main__":
    # faulthandler.enable() # trace error
    game_manage = GameManager()
    game_manage.run()
    pygame.quit()

    

