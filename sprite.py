import pygame
import os
from enum import Enum


class SpriteType(Enum):
    Sprite = 0
    AnimatedSprite = 1


class SpriteSheet:
    def __init__(self, file_path, frames_x, frames_y):
        sheet = load_image(file_path)
        self.images = []
        sheet_width = sheet.get_width()
        sheet_height = sheet.get_height()
        self.frame_width = sheet_width / frames_x
        self.frame_height = sheet_height / frames_y
        for y in range(frames_y):
            for x in range(frames_x):
                "Loads image from x,y,x+offset,y+offset"
                rect = pygame.Rect(x * self.frame_width, y * self.frame_height, self.frame_width, self.frame_height)
                image = pygame.Surface(rect.size).convert()
                image.blit(sheet, (0, 0), rect)
                self.images.append(image)
                pass

    def get_frame(self, index):
        return self.images[index]
        pass


class Sprite:
    def __init__(self):
        pass

    def update(self, dt):
        pass

    def draw(self, position_x, position_y):
        pass


class AnimatedSprite(Sprite):
    def __init__(self, sprite_sheet, frame_indices, frame_durations):
        self.frame_indices = frame_indices
        self.frame_durations = frame_durations
        self.sprite_sheet = sprite_sheet
        self.current_frame_idx = 0
        self.current_frame_duration = 0
        pass

    def update(self, dt):
        self.current_frame_duration += dt
        if self.current_frame_duration > self.frame_durations[self.current_frame_idx]:
            self.current_frame_idx += 1
            self.current_frame_duration = 0
            if self.current_frame_idx >= len(self.frame_indices):
                self.current_frame_idx = 0
        pass

    def draw(self, display, position_x, position_y):
        frame_to_draw = self.sprite_sheet.get_frame(self.frame_indices[self.current_frame_idx])
        display.blit(
            frame_to_draw,
            pygame.Rect(
                position_x,
                position_y,
                self.sprite_sheet.frame_width,
                self.sprite_sheet.frame_height))
        pass


def load_image(file_path):
    if os.path.isfile(file_path):
        image = pygame.image.load(file_path)
        image = image.convert_alpha()

        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + file_path + " - Check filename and path?")
