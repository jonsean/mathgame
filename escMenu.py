# escMenu.py
import pygame

class EscMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.visible = False
        
        # Menu dimensions
        self.menu_width = 400
        self.menu_height = 500
        self.menu_x = (screen_width - self.menu_width) // 2
        self.menu_y = (screen_height - self.menu_height) // 2
        
        # Colors
        self.background_color = (50, 50, 50, 200)  # Semi-transparent
        self.border_color = (255, 255, 255)
        self.button_color = (100, 100, 100)
        self.button_hover_color = (150, 150, 150)
        self.text_color = (255, 255, 255)
        
        # Font
        self.font = pygame.font.SysFont(None, 36)
        self.title_font = pygame.font.SysFont(None, 48)
        
        # Load icons (with fallback if files don't exist)
        self.icons = {}
        icon_files = ['upArrow.png', 'downArrow.png', 'skey.png', 'esc.png']
        for icon_file in icon_files:
            try:
                self.icons[icon_file] = pygame.image.load(icon_file)
                self.icons[icon_file] = pygame.transform.scale(self.icons[icon_file], (32, 32))
            except pygame.error:
                # Create a simple colored rectangle as fallback
                self.icons[icon_file] = pygame.Surface((32, 32))
                self.icons[icon_file].fill((200, 200, 200))
        
        # Button definitions
        self.buttons = []
        self.setup_buttons()
        
        # Create menu surface
        self.menu_surface = pygame.Surface((self.menu_width, self.menu_height), pygame.SRCALPHA)
        
    def setup_buttons(self):
        """Setup button positions and properties"""
        button_width = 300
        button_height = 50
        button_x = (self.menu_width - button_width) // 2
        start_y = 80
        spacing = 60
        
        self.buttons = [
            {
                'rect': pygame.Rect(button_x, start_y, button_width, button_height),
                'text': 'Volume Up',
                'icon': 'upArrow.png',
                'action': 'volume_up',
                'hovered': False
            },
            {
                'rect': pygame.Rect(button_x, start_y + spacing, button_width, button_height),
                'text': 'Volume Down',
                'icon': 'downArrow.png',
                'action': 'volume_down',
                'hovered': False
            },
            {
                'rect': pygame.Rect(button_x, start_y + spacing * 2, button_width, button_height),
                'text': 'Mute/Unmute',
                'icon': 'skey.png',
                'action': 'toggle_mute',
                'hovered': False
            },
            {
                'rect': pygame.Rect(button_x, start_y + spacing * 3, button_width, button_height),
                'text': 'Reset Game',
                'icon': None,
                'action': 'reset_game',
                'hovered': False
            },
            {
                'rect': pygame.Rect(button_x, start_y + spacing * 4, button_width, button_height),
                'text': 'Resume',
                'icon': 'esc.png',
                'action': 'resume',
                'hovered': False
            }
        ]
    
    def show(self):
        """Show the menu"""
        self.visible = True
    
    def hide(self):
        """Hide the menu"""
        self.visible = False
    
    def update_screen_size(self, screen_width, screen_height):
        """Update menu position when screen size changes"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.menu_x = (screen_width - self.menu_width) // 2
        self.menu_y = (screen_height - self.menu_height) // 2
    
    def handle_mouse_motion(self, pos):
        """Handle mouse motion for button hover effects"""
        if not self.visible:
            return
        
        # Adjust position relative to menu
        menu_pos = (pos[0] - self.menu_x, pos[1] - self.menu_y)
        
        for button in self.buttons:
            button['hovered'] = button['rect'].collidepoint(menu_pos)
    
    def handle_click(self, pos):
        """Handle mouse clicks on menu buttons"""
        if not self.visible:
            return None
        
        # Adjust position relative to menu
        menu_pos = (pos[0] - self.menu_x, pos[1] - self.menu_y)
        
        for button in self.buttons:
            if button['rect'].collidepoint(menu_pos):
                return button['action']
        
        return None
    
    def draw(self, surface):
        """Draw the menu"""
        if not self.visible:
            return
        
        # Clear menu surface
        self.menu_surface.fill((0, 0, 0, 0))
        
        # Draw menu background
        pygame.draw.rect(self.menu_surface, self.background_color, 
                        (0, 0, self.menu_width, self.menu_height))
        pygame.draw.rect(self.menu_surface, self.border_color, 
                        (0, 0, self.menu_width, self.menu_height), 3)
        
        # Draw title
        title_text = self.title_font.render("GAME MENU", True, self.text_color)
        title_rect = title_text.get_rect(center=(self.menu_width // 2, 40))
        self.menu_surface.blit(title_text, title_rect)
        
        # Draw buttons
        for button in self.buttons:
            # Button background
            color = self.button_hover_color if button['hovered'] else self.button_color
            pygame.draw.rect(self.menu_surface, color, button['rect'])
            pygame.draw.rect(self.menu_surface, self.border_color, button['rect'], 2)
            
            # Button icon
            if button['icon'] and button['icon'] in self.icons:
                icon_x = button['rect'].x + 10
                icon_y = button['rect'].y + (button['rect'].height - 32) // 2
                self.menu_surface.blit(self.icons[button['icon']], (icon_x, icon_y))
                text_x_offset = 50
            else:
                text_x_offset = 0
            
            # Button text
            text_surface = self.font.render(button['text'], True, self.text_color)
            text_x = button['rect'].x + text_x_offset + (button['rect'].width - text_x_offset - text_surface.get_width()) // 2
            text_y = button['rect'].y + (button['rect'].height - text_surface.get_height()) // 2
            self.menu_surface.blit(text_surface, (text_x, text_y))
        
        # Blit menu to main surface
        surface.blit(self.menu_surface, (self.menu_x, self.menu_y))