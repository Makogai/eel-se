if score > get_highscore():
                    message_to_screen("This is your new highscore!", white, 300, 370)
                    hs_file.seek(0)
                    hs_file.write(str(score))
                    hs_file.truncate()