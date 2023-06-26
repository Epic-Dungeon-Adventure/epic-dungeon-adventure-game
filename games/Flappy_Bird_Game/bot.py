def bot_decision(bird_rect, pipe_list):
    if pipe_list:
        next_pipe = pipe_list[0]

        vertical_distance = next_pipe.centery - bird_rect.centery

        if vertical_distance > 0:
            return -5
        else:
            return 0

    return 0
