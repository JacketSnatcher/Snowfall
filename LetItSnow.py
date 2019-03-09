import pygame
import random


def main():
    # screen height and width (alterable)
    w, h = 1000, 800
    # number of snowflakes (alterable)
    snowflake_quant = 400
    # gravity strength (alterable)
    gravity = 2
    # size of snow (alterable)
    snowsize = [1, 5]
    # makes the snow move left and right
    wind_factor = [1, -1]
    # random choice for movement of snow particles
    wind = [0, 0, 0, 0, 0, 1]

    # setup
    snowflake_list = []
    is_running = True
    pygame.init()
    window = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Snowfall!')
    clock = pygame.time.Clock()

    # generate flakes
    for num in range(0, snowflake_quant):
        position = [random.randint(0, w), random.randint(0, h), random.randint(snowsize[0], snowsize[1])]
        snowflake_list.append(position)
    # print flake locations
    print(snowflake_list)

    # mainloop
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        window.fill((173, 216, 230))

        # build the flakes!
        for num in range(0, snowflake_quant):
            pygame.draw.circle(window, (255, 255, 255), [snowflake_list[num][0], snowflake_list[num][1]],
                               snowflake_list[num][2])

            # moves snowflakes
            snowflake_list[num][1] += int(gravity * (snowflake_list[num][2]/2))
            snowflake_list[num][0] += random.choice(wind_factor) * random.choice(wind)

            # regenerates snowflakes
            if snowflake_list[num][1] > h:
                snowflake_list[num][1] = 0
                snowflake_list[num][0] = random.randint(0, w)
                snowflake_list[num][2] = random.randint(snowsize[0], snowsize[1])

            # print flake locations
            print(snowflake_list)

        pygame.display.flip()
        clock.tick(40)


if __name__ == "__main__":
    # call the main function
    main()
