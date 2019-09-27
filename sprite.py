import pygame
import os
from enum import Enum


class SpriteType(Enum):
    Sprite = 0
    AnimatedSprite = 1


class SpriteSheet:
    def __init__(self, file_path, frames_x, frames_y, frame_width=50, frame_height=50):
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
                image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
                image.blit(sheet, (0, 0), rect)
                scaled_image = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA, 32)
                scaled_image.blit(pygame.transform.scale(
                    image, (frame_width, frame_height)), (0, 0), pygame.Rect(0, 0, frame_width * 2, frame_height * 2))
                self.images.append(scaled_image)
                pass

    def get_frame(self, index):
        return self.images[index]
        pass


class Sprite:
    def __init__(self, sprite_sheet, frame_index, sprite_rotation=0):
        self.sprite_sheet = sprite_sheet
        self.frame_index = frame_index
        self.sprite_rotation = sprite_rotation
        pass

    def update(self, dt):
        pass

    def draw(self, display, position_x, position_y):
        frame_to_draw = self.sprite_sheet.get_frame(self.frame_index)
        display.blit(
            Sprite.rot_center(frame_to_draw, self.sprite_rotation),
            pygame.Rect(
                position_x,
                position_y,
                self.sprite_sheet.frame_width,
                self.sprite_sheet.frame_height))
        pass

    @staticmethod
    def rot_center(image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image


class AnimatedSprite(Sprite):
    def __init__(self, sprite_sheet, frame_indices, frame_durations, sprite_rotation=0):
        self.frame_indices = frame_indices
        self.frame_durations = frame_durations
        self.sprite_sheet = sprite_sheet
        self.current_frame_idx = 0
        self.current_frame_duration = 0
        self.sprite_rotation = sprite_rotation
        self.is_playing = False
        self.loop = False
        pass

    def play(self):
        # Reset play
        self.current_frame_duration = 0
        self.current_frame_idx = 0
        self.is_playing = True
        pass

    def update(self, dt):
        if self.is_playing:
            self.current_frame_duration += dt
            if self.current_frame_duration > self.frame_durations[self.current_frame_idx]:
                self.current_frame_idx += 1
                self.current_frame_duration = 0
                if self.current_frame_idx >= len(self.frame_indices):
                    self.current_frame_idx = 0
                    self.current_frame_duration = 0
                    if not self.loop:
                        self.is_playing = False
            pass

    def draw(self, display, position_x, position_y):
        frame_to_draw = self.sprite_sheet.get_frame(self.frame_indices[self.current_frame_idx])
        display.blit(
            Sprite.rot_center(frame_to_draw, self.sprite_rotation),
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
