from game.classes.game import Game


if __name__ == '__main__':
    game = Game()

    game.introduction_to_get_players_name()

    game.introduction_and_goals()

    play_again = True
    while play_again:
        game.reset_game()

        game.get_players_special_ability()

        game.set_all_items_in_game()

        game.play()

        game.check_and_display_boat_end()
        game.check_and_display_kraken_end()
        game.check_and_display_ocean_death_end()
        game.check_and_display_land_death_end()
        game.check_and_display_quit_end()

        play_again = game.check_play_again()

    game.exit_game()
