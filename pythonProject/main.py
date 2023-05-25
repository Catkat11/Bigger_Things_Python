from menu import main_multi, main_single_normal, main_single_easy
import pygame
import sys
from button import Button
from checking import Checking

pygame.init()

SCREEN = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.png")


def get_font(size):
    return pygame.font.Font("font.ttf", size)

def saving():
    user_text = ''
    input_rect = pygame.Rect(150, 125, 140, 32)
    color = pygame.Color("White")

    while True:
        SCREEN.fill("black")
        SAVING_MOUSE_POS = pygame.mouse.get_pos()
        SAVING_TEXT = get_font(20).render("Enter your mail:", True, "White")
        SAVING_RECT = SAVING_TEXT.get_rect(center=(350, 60))
        SCREEN.blit(SAVING_TEXT, SAVING_RECT)

        SAVING_ENTER = Button(image=None, pos=(350, 250),
                              text_input="CONTINUE", font=get_font(30), base_color="White", hovering_color="Green")
        SAVING_ENTER.changeColor(SAVING_MOUSE_POS)
        SAVING_ENTER.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SAVING_ENTER.checkForInput(SAVING_MOUSE_POS):
                    if Checking.check(user_text, user_text):
                        main_menu()
                    else:
                        pass



        pygame.draw.rect(SCREEN, color, input_rect)

        text_surface = get_font(20).render(user_text, True, "Black")

        SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(400, text_surface.get_width() + 10)
        pygame.display.flip()


def play():
    while True:
        SCREEN.fill("black")

        if main_single_normal():
            pass
        else:
            while True:
                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                SCREEN.fill("black")

                PLAY_TEXT = get_font(20).render("Do you want to save?", True, "White")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(350, 60))
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)

                PLAY_YES = Button(image=None, pos=(350, 150),
                                  text_input="YES", font=get_font(30), base_color="White", hovering_color="Green")
                PLAY_NO = Button(image=None, pos=(350, 250),
                                  text_input="NO", font=get_font(30), base_color="White", hovering_color="Green")

                PLAY_YES.changeColor(PLAY_MOUSE_POS)
                PLAY_YES.update(SCREEN)
                PLAY_NO.changeColor(PLAY_MOUSE_POS)
                PLAY_NO.update(SCREEN)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_YES.checkForInput(PLAY_MOUSE_POS):
                            saving()
                        elif PLAY_NO.checkForInput(PLAY_MOUSE_POS):
                            main_menu()

                pygame.display.update()


def scores():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(20).render("This is the SCORES screen.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(350, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        with open("data.txt", mode="r") as file:

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 140))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 160))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 180))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 200))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 220))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 240))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 260))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 280))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 300))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

            SCORES_TEXT = get_font(20).render(file.readline(), True, "White")
            SCORES_RECT = OPTIONS_TEXT.get_rect(center=(350, 320))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)


        OPTIONS_BACK = Button(image=None, pos=(350, 400),
                              text_input="BACK", font=get_font(30), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(350, 60))

        PLAY_BUTTON = Button(image=None, pos=(350, 200),
                             text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        SCORES_BUTTON = Button(image=None, pos=(350, 300),
                                text_input="SCORES", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(350, 400),
                             text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SCORES_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if SCORES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    scores()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()