import pygame
import random
import math
class Astroid: 
    def __init__(self, radius = 100, 
                    color='BLACK', label_text = str(random.randint(0,100)), font_size=48, 
                    font_color=(0, 0, 0), position=(100, 100), outline_width=0, 
                    outline_color=(0, 0, 0)):
        self.speed = 8
        self.direction = (random.uniform(-.5,.5),random.uniform(.1,.5))
        self.velocity = (self.speed * self.direction[0], self.speed * self.direction[1])
        self.radius = radius
        self.setColor() #self.color = color
        self.position = position
        self.outline_width = outline_width
        self.outline_color = outline_color
        self.points = self.getPoints()
        # --- Label Properties ---
        self.label_text = label_text
        self.font_color = font_color
        self.font_background_color = (255,255,255)
        self.font = pygame.font.Font(None, font_size)  # Use default Pygame font
        self._render_text()

        # --- Center Calculation ---
        self._calculate_centroid()
        
        #to detect clicks
        self.collitionRect = pygame.Rect(self.position[0], self.position[1], self.radius, self.radius)
        
        
    
    def getPoints(self):
        n_points = random.randint(3,10)
        p = []
        dangle = 2*math.pi/n_points
        for i in range(n_points):
            angle = i * dangle
            x = self.radius * math.cos(angle) + self.radius
            y = self.radius * math.sin(angle) + self.radius
            p.append((x, y))
        return p
        
    def setColor(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color = (r,g,b)
        
    def _render_text(self):
        #Renders the text surface for the label.
        self.text_surface = self.font.render(self.label_text, True, self.font_color)
        self.text_surface_background = self.font.render(self.label_text, True, self.font_background_color)

    def _calculate_centroid(self):
        """
        Calculates the geometric center (centroid) of the polygon's points.
        This provides a good approximation for the visual center for convex polygons.
        """
        x_coords = [p[0] for p in self.points]
        y_coords = [p[1] for p in self.points]
        num_points = len(self.points)
        
        centroid_x = sum(x_coords) / num_points
        centroid_y = sum(y_coords) / num_points
        
        # The centroid is relative to the polygon's points,
        # so we add the main position offset.
        self.centroid = (centroid_x + self.position[0], centroid_y + self.position[1])
    def updateRect(self):
        self.collitionRect.update(self.position[0], self.position[1], self.radius*2, self.radius*2)
    
    def containts(self, point):
        return self.collitionRect.collidepoint(point)
            
    
    def draw(self, surface):
        """
        Draws the polygon and its label onto the given surface.

        Args:
            surface (pygame.Surface): The Pygame surface to draw on.
        """
        self._calculate_centroid()
        self.updateRect()
        
        # Adjust all points by the polygon's main position
        absolute_points = [(p[0] + self.position[0], p[1] + self.position[1]) for p in self.points]

        # Draw the outline first (if it exists)
        if self.outline_width > 0:
            pygame.draw.polygon(surface, self.outline_color, absolute_points, self.outline_width)
        
        # Draw the filled polygon
        pygame.draw.polygon(surface, self.color, absolute_points)

        # Draw label
        text_rect_background = self.text_surface_background.get_rect(center=(self.centroid[0]+2, self.centroid[1]))
        surface.blit(self.text_surface_background, text_rect_background)
        
        text_rect = self.text_surface.get_rect(center=self.centroid)
        surface.blit(self.text_surface, text_rect)
        
    def set_position(self, x, y):
        """Updates the position of the polygon and recalculates its center."""
        self.position = (x, y)
        self._calculate_centroid()