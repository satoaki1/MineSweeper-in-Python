import pygame

from constants import WIDTH, HEIGHT


def display_message(screen, message):
    font = pygame.font.SysFont(None, 55)
    text = font.render(message, True, (255, 0, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()


def game_over_popup(screen):
    btn_width = 100
    btn_height = 50
    btn_x = WIDTH // 2 - btn_width // 2
    btn_y = HEIGHT // 2 + 30

    run_popup = True
    redraw = True  # Initially set to True to draw the screen at the start

    while run_popup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btn_x <= mouse_x <= btn_x + btn_width and btn_y <= mouse_y <= btn_y + btn_height:
                    run_popup = False
                    redraw = True  # Need to redraw after closing the popup

            if event.type == pygame.MOUSEMOTION:  # Detect mouse movement to decide when to redraw
                redraw = True

        if redraw:
            screen.fill((255, 255, 255))
            display_message(screen, "Game Over")

            # Draw 'OK' button
            pygame.draw.rect(screen, (255, 0, 0), (btn_x, btn_y, btn_width, btn_height))
            font = pygame.font.SysFont(None, 35)
            text = font.render('OK', True, (0, 0, 0))
            screen.blit(text, (btn_x + btn_width // 2 - text.get_width() // 2, btn_y + btn_height // 2 - text.get_height() // 2))

            pygame.display.flip()
            redraw = False  # Reset the flag after redrawing



def win_popup(screen):
    btn_width = 100
    btn_height = 50
    btn_x = WIDTH // 2 - btn_width // 2
    btn_y = HEIGHT // 2 + 30

    run_popup = True
    while run_popup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btn_x <= mouse_x <= btn_x + btn_width and btn_y <= mouse_y <= btn_y + btn_height:
                    run_popup = False

        screen.fill((255, 255, 255))
        display_message(screen, "You Won!", (0, 255, 0))

        # Draw 'OK' button
        pygame.draw.rect(screen, (0, 255, 0), (btn_x, btn_y, btn_width, btn_height))
        font = pygame.font.SysFont(None, 35)
        text = font.render('OK', True, (0, 0, 0))
        screen.blit(text,
                    (btn_x + btn_width // 2 - text.get_width() // 2, btn_y + btn_height // 2 - text.get_height() // 2))

        pygame.display.flip()
