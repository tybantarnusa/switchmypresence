from logic.discord import Discord

def main():

    publisher = "Square Enix"
    game = "Bravely Default II"
    image = "bd2"

    discord = Discord(publisher, game, image)
    discord.present()

if __name__ == '__main__':
    main()