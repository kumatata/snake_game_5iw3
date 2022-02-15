import pygame
import time
import random
import os


pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
medium_blue = (0, 0, 255)

dis_width = 900
dis_height = 400
game_width = 900
game_height = 350

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Jeu du python | 5IW3')

clock = pygame.time.Clock()

snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, game_height])



def show_last_score():
    if(os.path.isfile("score_file.txt") == True):
        all_score = []
        with open("score_file.txt", "r") as read_file:

            for score in read_file:
                all_score.append(score.rstrip())
            last_score = all_score[-1]


            output = score_font.render("Last score: " +   last_score , True, green)

            dis.blit(output, [game_width/2, game_height])





def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1
    snake_speed = 8

    food_x = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0
    speed_x = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    speed_y = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0
    slow_x = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    slow_y = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0


    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message(
                "Vous avez perdu! Faites 'c' pour recommencer ou 'q' pour quitter ", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        with open("score_file.txt", "a", newline='') as file_score:
                            score = str(length_of_snake - 1)
                            file_score.write(score + os.linesep)
                        game_loop()

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

        if x1 >= game_width or x1 < 0 or y1 >= game_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [speed_x, speed_y, snake_block, snake_block])
        pygame.draw.rect(dis, medium_blue, [slow_x, slow_y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        your_score(length_of_snake - 1)
        show_last_score()

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(
                0, game_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(
                0, game_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        if x1 == speed_x and y1 == speed_y:
            speed_x = round(random.randrange(
                0, game_width - snake_block) / 10.0) * 10.0
            speed_y = round(random.randrange(
                0, game_height - snake_block) / 10.0) * 10.0
            snake_speed += 1
        if x1 == slow_x and y1 == slow_y:
            slow_x = round(random.randrange(
                0, game_width - snake_block) / 10.0) * 10.0
            slow_y = round(random.randrange(
                0, game_height - snake_block) / 10.0) * 10.0
            if snake_speed > 2:
                snake_speed -= 1

        clock.tick(snake_speed)

    with open("score_file.txt", "a", newline='') as file_score:
        score = str(length_of_snake - 1)
        file_score.write(score + os.linesep)
    show_last_score()
    pygame.quit()


    quit()


game_loop()
