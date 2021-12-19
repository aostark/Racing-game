import pygame


def scale_img(img, factor):
    # round needed to get an integer not a float number
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


# take an image, return a rotated image based on an angle
def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, 1, (0, 255, 255))
    win.blit(render, (win.get_width() / 2 - render.get_width() / 2, win.get_height() / 2 - render.get_height() / 2))
