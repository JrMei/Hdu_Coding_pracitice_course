import pygame
import time
import random

pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dark_gray = (169, 169, 169)

# 设置屏幕宽高
window_width = 800
window_height = 600

# 设置游戏窗口
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game1.0beta')

# 设置时钟
clock = pygame.time.Clock()

# 设置蛇的尺寸和速度
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# 读取最高分
def read_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except:
        return 0

# 写入最高分
def write_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

# 显示分数
def show_score(score, high_score, steps):
    value = score_font.render("Your Score: " + str(score), True, black)
    game_window.blit(value, [0, 0])
    value = score_font.render("High Score: " + str(high_score), True, black)
    game_window.blit(value, [0, 35])
    value = score_font.render("Steps: " + str(steps), True, black)
    game_window.blit(value, [0, 70])

# 显示信息
def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [x, y])

# 绘制蛇
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_block, snake_block])

# 选择地图
def select_map():
    map_selected = False
    map_type = "easy"
    map_number = 1

    while not map_selected:
        game_window.fill(white)
        message("Select Map Difficulty:", blue, window_width / 3, window_height / 4)
        message("1. Easy", black, window_width / 3, window_height / 3)
        message("2. Medium", black, window_width / 3, window_height / 3 + 30)
        message("3. Hard", black, window_width / 3, window_height / 3 + 60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    map_type = "easy"
                    map_selected = True
                elif event.key == pygame.K_2:
                    map_type = "medium"
                    map_selected = True
                elif event.key == pygame.K_3:
                    map_type = "hard"
                    map_selected = True

    map_number_selected = False
    while not map_number_selected:
        game_window.fill(white)
        message("Select Map Number:", blue, window_width / 3, window_height / 4)
        message("1. Map 1", black, window_width / 3, window_height / 3)
        message("2. Map 2", black, window_width / 3, window_height / 3 + 30)
        message("3. Map 3", black, window_width / 3, window_height / 3 + 60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    map_number = 1
                    map_number_selected = True
                elif event.key == pygame.K_2:
                    map_number = 2
                    map_number_selected = True
                elif event.key == pygame.K_3:
                    map_number = 3
                    map_number_selected = True

    start_game(map_type, map_number)

# 开始游戏
def start_game(map_type, map_number):
    global snake_block, snake_speed
    obstacles = []

    if map_type == "easy":
        snake_speed = 10
        snake_block = 20
        if map_number == 1:
            # 简单地图1，无障碍物
            target_score = 10
            obstacles = []
        elif map_number == 2:
            # 简单地图2，少量障碍物
            target_score = 15
            obstacles = [
                (300, 200, 200, 20),
                (300, 500, 200, 20)
            ]
        elif map_number == 3:
            # 简单地图3，更多障碍物
            target_score = 20
            obstacles = [
                (200, 150, 200, 20),
                (400, 450, 200, 20),
                (100, 200, 600, 20)
            ]
    elif map_type == "medium":
        snake_speed = 15
        snake_block = 10
        if map_number == 1:
            # 中等地图1，少量障碍物
            target_score = 25
            obstacles = [
                (200, 200, 200, 20),
                (400, 400, 200, 20)
            ]
        elif map_number == 2:
            # 中等地图2，多些障碍物
            target_score = 30
            obstacles = [
                (100, 100, 200, 20),
                (600, 100, 100, 20),
                (300, 400, 100, 20)
            ]
        elif map_number == 3:
            # 中等地图3，更多障碍物
            target_score = 35
            obstacles = [
                (50, 50, 300, 20),
                (450, 50, 200, 20),
                (200, 300, 200, 20),
                (500, 450, 100, 20)
            ]
    elif map_type == "hard":
        snake_speed = 20
        snake_block = 10
        if map_number == 1:
            # 困难地图1，围成一圈的障碍
            target_score = 40
            obstacles = [
                (0, 0, window_width, 20),  # 上边界
                (0, window_height - 20, window_width, 20),  # 下边界
                (0, 0, 20, window_height),  # 左边界
                (window_width - 20, 0, 20, window_height)  # 右边界
            ]
        elif map_number == 2:
            # 困难地图2，复杂障碍物
            target_score = 45
            obstacles = [
                (100, 100, 600, 20),
                (100, 200, 600, 20),

                (100, 400, 600, 20),
                (100, 500, 600, 20)
            ]
        elif map_number == 3:
            # 困难地图3，更多复杂障碍物
            target_score = 50
            obstacles = [
                (50, 50, 700, 20),
                (50, 100, 20, 500),
                (100, 550, 700, 20),
                (750, 100, 20, 450),
                (200, 200, 400, 20),
                (200, 400, 400, 20)
            ]
    
    game_loop(map_type, target_score, obstacles)

# 游戏主循环
def game_loop(map_type, target_score, obstacles):
    game_over = False
    game_close = False 

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, window_height - snake_block) / snake_block) * snake_block

    high_score = read_high_score()
    steps = 0

    while not game_over:

        while game_close:
            game_window.fill(white)
            message("You Lost! Press C to Play Again or Q to Quit", red, window_width / 6, window_height / 3)
            show_score(Length_of_snake - 1, high_score, steps)
            pygame.display.update()
    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        if Length_of_snake - 1 > high_score:
                            high_score = Length_of_snake - 1
                            write_high_score(high_score)
                        select_map()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        steps += 1
        game_window.fill(white)

        # 绘制障碍物
        for obs in obstacles:
            pygame.draw.rect(game_window, dark_gray, obs)

        pygame.draw.rect(game_window, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        show_score(Length_of_snake - 1, high_score, steps)

        pygame.display.update()

        # 判断蛇是否吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, window_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

            if Length_of_snake - 1 >= target_score:
                game_close = True

        # 检查蛇是否碰到障碍物
        for obs in obstacles:
            if obs[0] <= x1 < obs[0] + obs[2] and obs[1] <= y1 < obs[1] + obs[3]:
                game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# 显示说明页面
def show_instructions():
    instructions_displayed = True
    while instructions_displayed:
        game_window.fill(white)
        message("Instructions:", blue, window_width / 3, window_height / 6)
        message("1. Use arrow keys to move the snake.", black, window_width / 6, window_height / 3)
        message("2. Eat the green food blocks to grow.", black, window_width / 6, window_height / 3 + 30)
        message("3. Avoid obstacles and the edges of the screen.", black, window_width / 6, window_height / 3 + 60)
        message("4. Reach the target score to win the game.", black, window_width / 6, window_height / 3 + 90)
        message("Press B to go back to the main menu.", red, window_width / 6, window_height / 3 + 150)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    instructions_displayed = False

# 显示主菜单
def main_menu():
    menu = True
    while menu:
        game_window.fill(white)
        message("Welcome to Snake Game", blue, window_width / 3, window_height / 6)
        message("1. Play Game", black, window_width / 3, window_height / 3)
        message("2. Instructions", black, window_width / 3, window_height / 3 + 30)
        message("3. Clear High Score", black, window_width / 3, window_height / 3 + 60)
        message("4. Quit", black, window_width / 3, window_height / 3 + 90)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    select_map()
                elif event.key == pygame.K_2:
                    show_instructions()
                elif event.key == pygame.K_3:
                    write_high_score(0)
                    high_score = 0
                elif event.key == pygame.K_4:
                    pygame.quit()
                    quit()

if __name__ == "__main__":
    main_menu()
    
#中文显示会显示乱码，因此使用英文界面