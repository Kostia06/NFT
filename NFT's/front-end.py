
import pygame as pg 
import os,sys 
import random as r
from PIL import Image
import clipboard
import glob
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.display.set_caption("NFT Maker")
WIDTH, HEIGHT = 500, 500
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
font = 'fff-forward/FFFFORWA.TTF'
run = True
class Label():
    def __init__(self, text, pos, color = 'Black',shade=['Gray','Gray'], rotate = 0, size = 20, bg = 'White', outline='Black', side = 'center'):
        self.font = pg.font.Font(font,size)
        self.font_size = size
        self.display = self.font.render(str(text), True, color)
        self.rect_new = self.display.get_rect()
        self.side = 'self.rect_new.' + side + ' = (pos)'
        exec(self.side)
        self.rect_new.w += self.font_size
        self.rect_new.h += self.font_size
        self.display = pg.transform.rotate(self.display, rotate)
        if bg != None:
            if rotate == 90 or rotate == 270:
                if shade[1] != None:
                    pg.draw.rect(screen, (shade[1]), (self.rect_new.x - self.font_size/2+5, self.rect_new.y - self.font_size/2+5, self.rect_new.h, self.rect_new.w), 0, 10)
                pg.draw.rect(screen, (bg), (self.rect_new.x - self.font_size/2, self.rect_new.y - self.font_size/2, self.rect_new.h, self.rect_new.w), 0, 10)
                if outline != None:
                    pg.draw.rect(screen, (outline), (self.rect_new.x - self.font_size/2, self.rect_new.y - self.font_size/2, self.rect_new.h, self.rect_new.w), 3, 10)
            else:
                if shade[1] != None:
                    pg.draw.rect(screen, (shade[1]), (self.rect_new.x - self.font_size/2+5, self.rect_new.y - self.font_size/2+5, self.rect_new.w, self.rect_new.h), 0, 10)
                pg.draw.rect(screen, (bg), (self.rect_new.x - self.font_size/2, self.rect_new.y - self.font_size/2, self.rect_new.w, self.rect_new.h), 0, 10)
                if outline != None:
                    pg.draw.rect(screen, (outline), (self.rect_new.x - self.font_size/2, self.rect_new.y - self.font_size/2, self.rect_new.w, self.rect_new.h), 3, 10)
        if shade[0] != None:
            self.shade = self.font.render(str(text), True, shade[0])
            self.shade = pg.transform.rotate(self.shade, rotate)
            screen.blit(self.shade, (self.rect_new.x + 4, self.rect_new.y + 4))
        screen.blit(self.display, (self.rect_new))
        self.rect = pg.Rect(self.rect_new.x - self.font_size/2, self.rect_new.y - self.font_size/2, self.rect_new.w, self.rect_new.h)
class Switch():
    def __init__(self,text, pos, turn, color = 'Black', shade = ['Gray', 'Gray'], size = 20, bg = 'White', outline= 'Black', sides='center'):
        self.font_size = size 
        self.turn = turn
        self.size = size/2
        self.text = text
        self.pos = pos
        self.circle = pg.Vector2()
        self.clicked = False
        self.rect_new = pg.Rect(pos[0], pos[1], size * 5, size * 1.5)
        self.max = self.rect_new.right - 5
        self.least = self.rect_new.left + 5
        self.circle.x = self.least
        self.circle.y = self.rect_new.centery
        self.side = sides
        self.color = color
        self.bg = bg
        self.outline = outline
        self.shades = shade
    def draw(self):
        pos = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0] ==1 :
            if self.rect_new.collidepoint(pos) and  not self.clicked:
                self.clicked = True
                if self.turn:
                    self.turn= False
                elif not self.turn:
                    self.turn = True
        if pg.mouse.get_pressed()[0] == 0:
            self.size = self.font_size/1.5 + 2
        
        if pg.mouse.get_pressed()[0] == 0 and self.clicked:
            self.clicked = False
        elif pg.mouse.get_pressed()[0] == 0 and not self.rect_new.collidepoint(pos):
            self.size = self.font_size/1.5
        if self.turn:
            self.color_circle = 'Green'
            self.circle.x = self.max
        elif not self.turn: 
            self.color_circle = 'Red'
            self.circle.x = self.least
        pg.draw.rect(screen, ('White'), (self.rect_new), 0, 15)
        pg.draw.rect(screen, ('Gray'), (self.rect_new), 0, 15)
        pg.draw.rect(screen, (self.color_circle), (self.rect_new), 0, 15)
        pg.draw.rect(screen, ('Black'), (self.rect_new), 3, 15)
        pg.draw.circle(screen, ('white'), (self.circle.x, self.circle.y), self.size)
        pg.draw.circle(screen, ('Black'), (self.circle.x, self.circle.y), self.size, 2)
        Label(self.text, (self.rect_new.x, self.rect_new.centery - self.font_size - self.rect_new.w/10 - 5), size=self.font_size, side=self.side, shade=self.shades, outline=self.outline, bg=self.bg, color = self.color)
    def choice(self):
        if self.turn:
            return True
        else:
            return False
class Button():
    def __init__(self, text, pos,  size = 20, shade = ['Gray', 'Gray'], color='Black', bg='White', outline = 'Black', side = 'center'):
        self.clicked = False
        self.bg = bg
        self.outline = outline
        self.shade = shade
        self.side = side
        self.font = pg.font.Font(font,size)
        self.display = self.font.render(str(text), True, color)
        if shade[0] != None:
            self.shade_display = self.font.render(str(text), True, shade[0])
        self.font_size = size
        self.rect_new = self.display.get_rect()
        self.side = 'self.rect_new.' + side + ' = (pos)'
        exec(self.side)
        self.rect_new.w += self.font_size
        self.rect_new.h += self.font_size
        self.offset = 0
        self.rect = pg.Rect(-500, -500, 0, 0)
    def draw(self):
        if self.rect_new.collidepoint(pg.mouse.get_pos()):
            self.offset = 1.5
        if self.shade[1] != None:
            pg.draw.rect(screen,(self.shade[1]), (self.rect_new.x - self.font_size/2, self.rect_new.y-self.font_size/2, self.rect_new.w + 5, self.rect_new.h + 5), 0, 10)
        if self.bg != None:
            pg.draw.rect(screen,(self.bg), (self.rect_new.x - self.font_size/2 + self.offset , self.rect_new.y-self.font_size/2 + self.offset, self.rect_new.w, self.rect_new.h), 0, 10)
        if self.outline != None:
            pg.draw.rect(screen,(self.outline), (self.rect_new.x - self.font_size/2 + self.offset, self.rect_new.y-self.font_size/2 + self.offset, self.rect_new.w , self.rect_new.h), 3, 10)
        if self.shade[0] != None:
            screen.blit(self.shade_display, (self.rect_new.x + self.offset + 5, self.rect_new.y + self.offset + 5))
        screen.blit(self.display, (self.rect_new.x + self.offset , self.rect_new.y + self.offset))
        self.rect = pg.Rect(self.rect_new.x - self.font_size/2 + self.offset, self.rect_new.y-self.font_size/2 + self.offset, self.rect_new.w, self.rect_new.h)
    def choice(self):
        action = False
        if pg.mouse.get_pressed()[0] ==1:
            try:
                if self.rect_new.collidepoint(pg.mouse.get_pos()):
                    self.offset = 1.5
                    self.clicked = True
                    action = True
                    return action
            except:
                pass
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.offset = 0
class Bar():
    def __init__(self,pos, size, color=['green', 'yellow', 'red'], shade='Grey', outline='Black', time=5000):
        self.color = color
        self.color_choice = 1
        self.size = size
        self.pos = pos
        self.outline = outline
        self.shade = shade
        self.courent_time = 0
        self.press_time = 0
        self.time = time
        self.ratio = time/ self.size[0]
        self.show = False
        self.clicked = False
        self.work = True
    def draw(self, item):
        self.rect = pg.Rect(item.rect.centerx-self.pos[0] -self.size[0]/2, item.rect.centery -self.pos[1] - self.size[1]/2, self.size[0],self.size[1])

        if self.show and not self.courent_time - self.press_time>self.time:
            if self.shade != None:
                pg.draw.rect(screen, self.shade, (self.rect.x, self.rect.y, self.size[0] +5, self.rect.h + 5), 0, 5)
            try:
                pg.draw.rect(screen, (self.color[self.color_choice-1]), (self.rect.x, self.rect.y, (self.courent_time - self.press_time)/self.ratio, self.rect.h), 0, 5)
            except:
                pass
            if self.outline != None:
                pg.draw.rect(screen, (self.outline), self.rect, 3, 5)

        if not item.clicked or not self.work:
            self.press_time = pg.time.get_ticks()
            self.show = False
            self.clicked = False
            self.color_choice = 1
        else:
            self.show = True
        self.courent_time = pg.time.get_ticks()
        if self.courent_time - self.press_time>self.time and not self.clicked:
            self.color_choice = 1
            self.press_time = 0
            self.courent_time = 0
            self.show = False
            self.clicked = True
        if self.courent_time - self.press_time > self.time/len(self.color) * self.color_choice:
            self.color_choice += 1
    def choice(self):
        return self.clicked
class Scale():
    def __init__(self, text, pos, scale, set, size = 20, shade = 'Gray', color = 'Black', bg = True,bg_color = 'White', shades = True, outline = 'Black'):
        self.pos = pos
        self.text = text
        self.scale = scale
        self.font = pg.font.Font(font,size)
        self.scale = scale
        self.list = (bg, bg_color, color, shade, outline, size, shades)
        self.scale_pos = pg.Vector2()
        self.rect_new = pg.Rect(pos[0], pos[1],size * 5, size/2)
        self.scale_pos.x = pos[0] + set * size/100 * 5
        self.font_size = size
        self.scale_pos.y = self.rect_new.centery + self.rect_new.h
        self.rect_new.h += self.font_size
        self.num = 50
        self.font_size = size
        self.changed = False
        self.size =size/2
    def draw(self):
        pos = pg.mouse.get_pos()
        if self.rect_new.collidepoint(pos):
            self.size = self.font_size/2 + 1
        elif pg.mouse.get_pressed()[0] ==0 and not self.rect_new.collidepoint(pos):
            self.size = self.font_size/2
        if self.list[6]:
            pg.draw.rect(screen,(self.list[3]), (self.rect_new.x + 4, self.rect_new.y + 4, self.rect_new.w, self.rect_new.h), 0, 15)
        pg.draw.rect(screen,('White'), (self.rect_new), 0, 15)
        if self.list[4] != None:
            pg.draw.rect(screen,(self.list[4]), (self.rect_new), 2, 15)
        pg.draw.circle(screen, ('White'), (self.scale_pos),self.size)
        pg.draw.circle(screen, ('Black'), (self.scale_pos),self.size, 2)
        if pg.mouse.get_pressed()[0] ==1:
            if self.rect_new.collidepoint(pos):
                self.changed = True
                self.scale_pos.x = pg.mouse.get_pos()[0]
                self.num = (self.pos[0] - self.scale_pos.x)/((self.font_size * 5)/100)
                if abs(self.num) < 0:
                    self.num = 0.0
                self.size = self.font_size/2 + 2
                num_display = self.font.render(str(abs(int(self.num))), True, 'Black')
                num_rect = num_display.get_rect()
                screen.blit(num_display, (self.scale_pos +(-num_rect.w/2,self.font_size/2)))
        Label(self.text, (self.rect_new.centerx, self.rect_new.centery - self.font_size - self.rect_new.w/5), color = self.list[2],bg = self.list[0], bg_color =self.list[1], shade = self.list[3], outline=self.list[4], size = self.list[5], shades=self.list[6])
    def choice(self):
        return abs(self.num)
class Input():
    def __init__(self, text, pos, num, size = 20, color='Black',bg='White', shade=['Gray', "Gray"], type=str, sides=['center', 'center']):
        self.num = num + 1
        self.text = text[0]
        self.rect_new = pg.Rect(0,0,0,0)
        self.rect_new.center = (pos)
        self.clicked = False
        self.output = text[1]
        self.type = type       
        self.offset = 0
        self.size = size
        self.output_rect = None
        self.shade = shade
        self.bg = bg
        self.color = color
        self.sides = sides
    def draw(self,event, single = False):
        pos = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0] ==1 and self.output_rect != None:
            if self.output_rect.rect.collidepoint(pos):
                self.clicked = True
        if pg.mouse.get_pressed()[0] == 1 and self.clicked:
            if not self.output_rect.rect.collidepoint(pos):
                self.clicked = False
        if self.clicked:
            for event in event:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        self.output = self.output[:-1]
                    elif len(self.output) + 1 < self.num and not single:
                        if self.type == str:
                            self.output += event.unicode
                        elif event.key != 1073742051:
                            try:
                                send = event.unicode
                                send = int(send)
                                self.output += str(send)
                            except:
                                pass
                        if event.key == pg.K_v and pg.key.get_mods() & pg.KMOD_CTRL:
                            self.output = self.output[:-1]
                            text = clipboard.paste()
                            self.output += text
                    elif len(self.output) + 1 < self.num and single:
                        self.output = event.key
                    else:
                        self.clicked = False
        if self.text != '':
            Label(self.text, (self.rect_new.center),shade=self.shade, bg=self.bg, color=self.color, size = self.size, side=self.sides[0])
            if self.clicked:
                self.output_rect = Label(self.output + '|', (self.rect_new.centerx, self.rect_new.bottom +self.rect_new.h*2 + self.size*2 + 20),shade=self.shade, bg=self.bg, color=self.color, size = self.size, side=self.sides[1])
            else:
                self.output_rect = Label(self.output, (self.rect_new.centerx, self.rect_new.bottom + self.rect_new.h*2 + self.size*2 + 20),shade=self.shade, bg=self.bg, color=self.color, size = self.size, side=self.sides[1])
        else:
            if self.clicked:
                self.output_rect = Label(self.output + '|', (self.rect_new.center),shade=self.shade, bg=self.bg, color=self.color, size = self.size, side=self.sides[1])
            else:
                self.output_rect = Label(self.output, (self.rect_new.center),shade=self.shade, bg=self.bg, color=self.color, size = self.size, side=self.sides[1])
    def choice(self):
        if not self.clicked:
            return self.output

class NFT_Generator():
    def __init__(self):
        self.layers = None
        self.bg = None
        self.output_path = None
        self.DS = False
        self.rarities = []
        self.bg_color_list = []
        self.size = []
        self.error = False
        self.transparent = True
        self.random_color = True
        self.img_list = []
        self.img_path = None
    def load_img_layers(self, img_path):
        paths = sorted(os.listdir(img_path))
        if '.DS_Store' in paths:
            paths.remove('.DS_Store')
        layers = []
        for path in paths:
            layer_path = os.path.join(img_path, path)
            layer = Layer(layer_path)
            layers.append(layer)
        for i in range(len(self.rarities)):
            layers[i-1].rarity = self.rarities[i-1]
        return layers


    def render_img(self, img_list):
        global error_text
        if not self.transparent:
            img = Image.new('RGBA',(self.size), (self.bg))
        else:
            img = Image.new('RGBA',(self.size))
        self.DS = False
        for path in img_list:
            if not '/.DS_Store' in path:
                layer_img = Image.open(path)
                try:
                    img = Image.alpha_composite(img, layer_img)
                except ValueError:
                    error_text = 'Images dont mathc sizes'
                    self.error = True
            else: 
                self.DS = True
        if not self.DS and not self.error:
            self.img_list.append(img)
            return img



    def generate(self):
        img_path_list = []
        for layer in self.layers:
            if layer.generation():
                img_path = layer.random_img_path()
                img_path_list.append(img_path)
        return img_path_list



    def generate_img(self, num, img_path, dir, size):
        self.size = size
        self.img_path = img_path
        self.layers = self.load_img_layers(img_path)
        self.bg = None
        self.output_path = dir
        self.DS = False
        self.error = False
        os.makedirs(self.output_path, exist_ok=True)
        
        for i in range(num):
            if len(self.bg_color_list) == 0 or self.random_color:
                self.bg = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
            else:
                self.bg = self.bg_color_list[r.randrange(0,len(self.bg_color_list))]
            img_path_list = self.generate()
            img = self.render_img(img_path_list)
            if not self.DS:
                index = str(i).zfill(3)
                img_save_path = os.path.join(self.output_path, f'nft{index}.png')
                try:
                    img.save(img_save_path)
                except:
                    pass
        self.make_gif(self.output_path)
    def make_gif(self, frame_folder):
        frames = [Image.open(image) for image in sorted(glob.glob(f"{frame_folder}/*.png"))]
        frame_one = frames[0]
        frame_one.save(f"{self.output_path}/nft.gif", format="GIF", append_images=frames,
        save_all=True, duration=len(self.img_list)*20, loop=0)
class Layer():
    def __init__(self, path):
        self.path = path
        self.rarity = 1
    def random_img_path(self):
        img_paths = os.listdir(self.path)
        random_path = r.choice(img_paths)
        return os.path.join(self.path, random_path)
    def generation(self):
        return  r.random() < float(self.rarity)/100

num = Input(("How many of Nft's", '100'), (10, 100), 4, type=int, size=15, shade=[None,'#001682'], sides=['bottomleft', 'bottomleft'], bg='#F9F871', color='#FF9476')
dir = Input(('Pathway to image folder', './images'), (10, 200),200, size=15, shade=[None,'#001682'], sides=['bottomleft', 'bottomleft'], bg='#F9F871',color='#FF9476')
size_1 = Input(('Size', '24'), (10, 100),200,type=int ,size=15, shade=[None,'#001682'], sides=['bottomleft', 'bottomleft'], bg='#F9F871',color='#FF9476')
size_2 = Input(('', '24'), (80, 150),200,type=int ,size=15, shade=[None,'#001682'], sides=['bottomleft', 'bottomleft'], bg='#F9F871',color='#FF9476')
new_dir = Input(('Output directory', '/Users/kostia/desktop/output'), (10, 300),200, size=15, shade=[None,'#001682'], sides=['bottomleft', 'bottomleft'], bg='#F9F871',color='#FF9476')
start = Button('START', (250, 450), shade=[None, '#001682'], bg='#F9F871',color='#FF9476')
advanced = Button('Advanced', (55, 400), shade=[None, '#001682'], bg='#F9F871',color='#FF9476', size=15)
back = Button('Back', (40, 475), shade=[None, '#001682'], bg='#F9F871',color='#FF9476', size=15)
rarity = Button('Rarities', (25, 100), shade=[None, '#001682'], bg='#F9F871',color='#FF9476', size=15,  side='bottomleft')
img_setting = Button('Image settings', (25, 150), shade=[None, '#001682'], bg='#F9F871',color='#FF9476', size=15, side='bottomleft')
bar = Bar((0, 50), (200, 30), shade='#001682', time=2000)
bg_color = Input(("Background colors", ''), (10, 200), 8, size=15, shade=[None,'#001682'], sides=['bottomleft', 'bottomleft'], bg='#F9F871', color='#FF9476')
bg_color_button = Button('Add', (115, 250), shade=[None, '#001682'], bg='#F9F871',color='#FF9476', size=15, side='bottomleft')
random_color = Switch('Random Color', (10, 380), True, size=10, shade=[None,'#001682'], sides='bottomleft', bg='#F9F871', color='#FF9476')
transparent = Switch('Transparency', (10, 435), False, size=10, shade=[None,'#001682'], sides='bottomleft', bg='#F9F871', color='#FF9476')
size = 0.3
img_size = (24,24)
page = 0
sizes = [150, 100, 50, 0]
inputs = []
NFT = NFT_Generator()
error_text = ''
paths = sorted(os.listdir(dir.choice()))
if '.DS_Store' in paths:
    paths.remove('.DS_Store')
for i in range(len(paths)):
    NFT.rarities.append(1000)
NFT.transparent = transparent.choice()
NFT.random_color = random_color.choice()
def main_page(event):
    global page, img_size, error_text
    Label(('By: Kostia'), (50,25), shade=[None,'#001682'], size=10, bg='#F9F871', color='#FF9476')
    num.draw(event)
    dir.draw(event)
    new_dir.draw(event)
    start.draw()
    bar.draw(start)
    start.choice()
    advanced.draw()
    if advanced.choice():
        page = 1
    if start.choice():
        if dir.choice() == '' or  new_dir.choice() == '' or num.choice() == '':
            error_text = 'Please Fill Every Requiment'
            bar.work = False
    if start.choice() and dir.choice() != ''  and new_dir.choice() != '' and  num.choice() != '':
        bar.work = True
        error_text = ''
    if bar.choice():
        NFT.generate_img(int(num.choice()), dir.choice(), new_dir.choice(), img_size)
def advanced_page(event):
    global page 
    Label(('Advanced'), (50,25), shade=[None,'#001682'], size=10, bg='#F9F871', color='#FF9476')
    back.draw()
    rarity.draw()
    img_setting.draw()
    if img_setting.choice():
        page =3
    if rarity.choice():
        page = 2
    if back.choice():
        page = 0
def rarity_page(event):
    global page
    Label(('Rarity'), (50,25), shade=[None,'#001682'], size=10, bg='#F9F871', color='#FF9476')
    back.draw()
    NFT.rarities.clear()
    try:
        paths = sorted(os.listdir(dir.choice()))
        if '.DS_Store' in paths:
            paths.remove('.DS_Store')
        for i in range(len(paths)):
            if len(inputs) < len(paths):
                inputs.append(Input(('','1000'), (150,100 + (i * 35)), 4 ,type=int, size=10, shade=[None,'#001682'], sides=['bottomleft', 'bottomleft'], bg='#F9F871', color='#FF9476'))
            Label(str(paths[i]), (25, 100 + (i * 35)),shade=[None,'#001682'], size=10, bg='#F9F871', color='#FF9476', side='bottomleft')
        for i in inputs:
            i.draw(event)
            if len(NFT.rarities) < len(inputs):
                NFT.rarities.append(i.choice())
    except FileNotFoundError:
        Label('Please Fill Every Requiment', (250, 250),shade=[None,'#001682'], size=10, bg='#F9F871', color='#FF9476')
    if back.choice():
        page = 0
def img_page(event):
    global page, img_size, error_text
    Label(('Image settings'), (55,25), shade=[None,'#001682'], size=10, bg='#F9F871', color='#FF9476')
    back.draw()
    size_1.draw(event)
    size_2.draw(event)
    bg_color.draw(event)
    bg_color_button.draw()
    random_color.draw()
    transparent.draw()
    if transparent.clicked:
        random_color.turn = False
    if random_color.clicked:
        transparent.turn = False
    if bg_color_button.choice() and bg_color.output != '':
        try:
            pg.draw.rect(screen, (bg_color.choice()), (-10, -10, 0, 0))
            if not bg_color.choice() in NFT.bg_color_list:
                NFT.bg_color_list.append(bg_color.choice())
                bg_color.output = ''
        except:
            error_text ='Invalid color name'
    try:
        pg.draw.rect(screen, (bg_color.output), (10, 280, 150, 50), 0, 5)
    except:
        pass
    pg.draw.rect(screen, ('Black'), (10, 280, 150, 50), 3, 5)
    try:
        img_size = (int(size_1.choice()), int(size_2.choice()))
    except:
        pass
    if back.choice():
        page = 0
    
pages = [main_page, advanced_page, rarity_page, img_page]
def main():
    global run,size, page
    while run:
        clock.tick(60)
        event = pg.event.get()
        for i in event:
            if i.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
        screen.fill('#6D6FF0')
        pg.draw.circle(screen,'#E262D3', (500, 0), sizes[0])
        pg.draw.circle(screen,'#FF6BA3', (500, 0), sizes[1])
        pg.draw.circle(screen,'#FF9476', (500, 0), sizes[2])
        pg.draw.circle(screen,'#FFC85D', (500, 0), sizes[3])

        pg.draw.circle(screen,'#E262D3', (500, 250), sizes[0])
        pg.draw.circle(screen,'#FF6BA3', (500, 250), sizes[1])
        pg.draw.circle(screen,'#FF9476', (500, 250), sizes[2])
        pg.draw.circle(screen,'#FFC85D', (500, 250), sizes[3])

        pg.draw.circle(screen,'#E262D3', (500, 500), sizes[0])
        pg.draw.circle(screen,'#FF6BA3', (500, 500), sizes[1])
        pg.draw.circle(screen,'#FF9476', (500, 500), sizes[2])
        pg.draw.circle(screen,'#FFC85D', (500, 500), sizes[3])
        Label('NFT Maker', (250,30), shade=[None,'#001682'], size=20, bg='#F9F871', color='#FF9476')        
        if error_text != '':
            Label(error_text, (350, 135),shade=[None,'#001682'], size=10, bg='#F9F871', color='#FF9476')
        for i in range(len(sizes)):
            sizes[i] += size
        if sizes[0] > 200 or 150 > sizes[0]:
            size *= -1
        pages[page](event)
        pg.display.update()

main()




















