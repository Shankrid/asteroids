import pygame

def draw_game_over(screen, player_score):
    screen.fill((0, 0, 0))

    font_big = pygame.font.Font(None, 72)
    font_small = pygame.font.Font(None, 36)

    text_game_over = font_big.render("-GAME OVER-", True, (255, 0, 0))
    text_score = font_small.render(f"Final Score: {player_score}", True, (255, 255, 255))
    text_restart = font_small.render(F"Press R to restart", True, (200, 200, 200))

    screen.blit(text_game_over, center_text(screen, text_game_over))
    screen.blit(text_score, (screen.get_width() // 2 - text_score.get_width() // 2, 300))
    screen.blit(text_restart, (screen.get_width() // 2 - text_restart.get_width() // 2, 350))

def center_text(screen, surface):
    return (
        screen.get_width() // 2 - surface.get_width() // 2, 
        200
    )