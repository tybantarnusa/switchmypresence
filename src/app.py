from logic.discord import Discord

def main():

    game = "Bravely Default II"
    image = "bd2"

    discord = Discord(game, image)
    discord.present()

if __name__ == '__main__':
    main()