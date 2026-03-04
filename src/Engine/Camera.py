import pygame
import src.Engine.GameObject as GameObject

class Camera():
    def __init__(self, target:GameObject.GameObject) -> None:
        """Cameras are used for specific object focus, entity culling, and scenes. They connect directly with the screen to know what is visible and not."""

        self.target = target

        self.fov_width = 400
        self.fov_height = 400

        self.visible_rect = pygame.Rect(0, 0, self.fov_width, self.fov_height)

    
    def update(self) -> None:
        self.visible_rect.centerx = self.target.rect.centerx
        self.visible_rect.centery = self.target.rect.centery


    def get_visible(self, *layers:pygame.sprite.Group) -> pygame.sprite.Group:
        visible_group = pygame.sprite.Group()
        
        for group in layers:
            for obj in group.sprites():
                if obj.rect.colliderect(self.visible_rect):
                    visible_group.add(obj)
        return visible_group

