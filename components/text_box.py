import pygame


class TextBox():
    def __init__(self, screen, box_size, box_color, text, font, font_color, speed):
        margin = 10
        self.margin = margin
        self.last_word_pos = [self.margin, screen.get_height() - box_size[1] + margin]
        self.screen = screen
        self.box_pos = [0, screen.get_height() - box_size[1]]
        self.box_size = box_size
        self.box_color = box_color
        self.font = font
        self.font_color = font_color
        self.speed = speed
        
        self.words = text.split(" ")
        self.rendered_lines = []
        self.space_width = font.size(' ')[0]
        self.word_index = -1
        self.used_words = ""

    def render_previous_lines(self):
        for line in self.rendered_lines:
            self.screen.blit(line[0], line[1])
        word_surface = self.font.render(self.used_words, True, self.font_color)
        self.screen.blit(word_surface, (self.box_pos[0] + 10, self.last_word_pos[1]))

    def render_word(self):
        box_border_radius = 30
        rect = pygame.Rect(self.box_pos,self.box_size)
        pygame.draw.rect(self.screen, self.box_color, rect, False, box_border_radius)
        word_surface = self.font.render(self.used_words, True, self.font_color)
        self.screen.blit(word_surface, (self.box_pos[0] + 10, self.last_word_pos[1]))

        if int(self.word_index + self.speed) >= len(self.words):
            self.render_previous_lines()
            return "finish"
        
        if int(self.word_index + self.speed) == int(self.word_index):
            self.word_index += self.speed
            self.render_previous_lines()
            return
        
        current_word = self.words[int(self.word_index + self.speed)]
        word_surface = self.font.render(current_word, True, self.font_color)
        word_width , word_height = word_surface.get_size()

        if self.last_word_pos[0] + word_width >= self.box_size[0] - self.margin:
            self.rendered_lines.append([self.font.render(self.used_words, True, self.font_color), (self.box_pos[0] + 10, self.last_word_pos[1])])
            self.used_words = current_word + " "
            self.last_word_pos[0] = self.box_pos[0] + self.margin
            self.last_word_pos[1] += word_height
        else: self.used_words += current_word + " "

        self.render_previous_lines()
        self.last_word_pos[0] += word_width + self.space_width
        self.word_index += self.speed