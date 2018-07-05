a_count = 0
q1_answer = input("Which artist produced this sticker? \n a) Eroel Cho \n b) KMK Studios \n c) Susilo \n d) Kun Widiarso \n e) BBM")
if q1_answer.lower() =='a':
    q2_answer = input("Select the type of sticker style you feel best reflects the sticker being deployed. \n a) Eroel Cho's Front Style Type? \n b) Eroel Cho's Japanese Style Type? \n c) Eroel Cho's All Actions Style Type? \n d) Eroel Cho's Romance Style Type? \n e) Eroel Cho's Sports Style Type? \n f) Eroel Cho's High Variety Style Type? \n g) Eroel Cho's Creative Style Type?")
    if q2_answer.lower() =='a':
            q11_answer = input("Is this a/an: \n a) Bobo Baby? \n b) Bobo Emoji? \n c) Cute Animal? \n d) Unattractive Animal? \n e) Unattractive Character? \n f) Food Character?")

            eroel_animated = {
            'a': 0.14283, 'b': 0.15143, 'c': 0.16104, 'd': 0.15143, 'e': 0.15143, 'f': 0.15143, 'g': 0.15143
                     }
            eroel_static = {
            'a': 0.17562, 'b': 0.22101, 'c': 0.25220, 'd': 0.22101, 'e': 0.22101, 'f': 0.22101, 'g': 0.22101
                        }
            front_style = {
            'a': 0.27100, 'b': 0.05206, 'c': 0.15311, 'd': 0.13803, 'e': 0.11882, 'f': 0.18237
                        }
#cut to q_answer if value
            if q11_answer.lower() =='a':
                a_count += (front_style.get('a'))
            elif q11_answer.lower() =='b':
                a_count += (front_style.get('b'))
            elif q11_answer.lower() =='c':
                a_count += (front_style.get('c'))
            elif q11_answer.lower() =='d':
                a_count += (front_style.get('d'))
            elif q11_answer.lower() =='e':
                a_count += (front_style.get('e'))
            elif q11_answer.lower() =='f':
                a_count += (front_style.get('f'))
            else: print("Sorry, I don't understand that response.")

            if q11_answer.lower() =='a' or 'b' or 'c' or 'd' or 'e' or 'f':
                    q301_answer = input("What is the second closest type of sticker pack? \n a) Bobo Baby? \n b) Bobo Emoji? \n c) Cute Animal? \n d) Unattractive Animal? \n e) Unattractive Character? \n f) Food Character?")

                    if q301_answer.lower() =='a':
                        a_count += (front_style.get('a'))
                    elif q301_answer.lower() =='b':
                        a_count += (front_style.get('b'))
                    elif q301_answer.lower() =='c':
                        a_count += (front_style.get('c'))
                    elif q301_answer.lower() =='d':
                        a_count += (front_style.get('d'))
                    elif q301_answer.lower() =='e':
                        a_count += (front_style.get('e'))
                    elif q301_answer.lower() =='f':
                        a_count += (front_style.get('f'))
                    else: print("Sorry, I don't understand that response.")

                    if q301_answer.lower() =='a' or 'b' or 'c' or 'd' or 'e' or 'f':
                        q401_answer = input("Is this pack animated? \n a) Yes \n b) No")

                    eroel_animated = {
                    'a': 0.14283, 'b': 0.15143, 'c': 0.16104, 'd': 0.15143, 'e': 0.15143, 'f': 0.15143, 'g': 0.15143
                        }
                    eroel_static = {
                    'a': 0.17562, 'b': 0.22101, 'c': 0.25220, 'd': 0.22101, 'e': 0.22101, 'f': 0.22101, 'g': 0.22101
                        }

                    if q401_answer.lower() == 'a':
                        a_count += (eroel_animated.get('a'))

                    if q401_answer.lower() == 'b':
                        a_count += (eroel_static.get('a'))

                    if q401_answer.lower() == 'a' or 'b':
                        q501_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                    eroel_text = {
                    'a': 0.11684, 'b': 0.18381, 'c': 0.19214, 'd': 0.51751, 'e': 0.18381, 'f': 0.18381, 'g': 0.18381
                    }
                    eroel_notext = {
                    'a': 0.17684, 'b': 0.18282, 'c': 0.18660, 'd': 0.24173, 'e': 0.18282, 'f': 0.18282, 'g': 0.18282
                    }

                    if q501_answer.lower() == 'a':
                                a_count += (eroel_text.get('a'))

                    if q501_answer.lower() == 'b':
                                a_count += (eroel_notext.get('a'))

                    if q501_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")
    if q2_answer.lower() =='b':
        q12_answer = input("Is this a/an: \n a) Anime Character? \n b) Something Else?")

#cut to q_answer if value
        japanese_eroel = {
        'a': 0.23045, 'b': 0.18627
            }
        if q12_answer.lower() =='a':
            a_count += (japanese_eroel.get('a'))
        elif q12_answer.lower() == 'b':
            a_count += (japanese_eroel.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q12_answer.lower() =='a' or 'b':
            q311_answer = input("What is the second closest type of sticker pack? \n a) Anime Character? \n b) Something Else?")

            if q311_answer.lower() =='a':
                a_count += (japanese_eroel.get('a'))
            elif q311_answer.lower() == 'b':
                a_count += (japanese_eroel.get('b'))
            else: print("Sorry, I don't understand that response.")

            if q311_answer.lower() == 'a' or 'b':
                q411_answer = input("Is this pack animated? \n a) Yes \n b) No")

                eroel_animated = {
                'a': 0.14283, 'b': 0.15143, 'c': 0.16104, 'd': 0.15143, 'e': 0.15143, 'f': 0.15143, 'g': 0.15143
                            }
                eroel_static = {
                'a': 0.17562, 'b': 0.22101, 'c': 0.25220, 'd': 0.22101, 'e': 0.22101, 'f': 0.22101, 'g': 0.22101
                            }

                if q411_answer.lower() == 'a':
                            a_count += (eroel_animated.get('b'))

                if q411_answer.lower() == 'b':
                            a_count += (eroel_static.get('b'))

                if q411_answer.lower() == 'a' or 'b':
                        q511_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        eroel_text = {
                        'a': 0.11684, 'b': 0.18381, 'c': 0.19214, 'd': 0.51751, 'e': 0.18381, 'f': 0.18381, 'g': 0.18381
                        }
                        eroel_notext = {
                        'a': 0.17684, 'b': 0.18282, 'c': 0.18660, 'd': 0.24173, 'e': 0.18282, 'f': 0.18282, 'g': 0.18282
                        }

                        if q511_answer.lower() == 'a':
                                a_count += (eroel_text.get('b'))

                        if q511_answer.lower() == 'b':
                                a_count += (eroel_notext.get('b'))

                                if q511_answer.lower() == 'a' or 'b':
                                    if a_count >= 0.91883:
                                        print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                    if 0.82224 <= a_count < 0.91883:
                                        print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                    if 0.66331 < a_count < 0.82224:
                                        print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                    if 0.59139 < a_count <= 0.66331:
                                        print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                    if a_count <= 0.59139:
                                        print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q2_answer.lower() =='c':
        q13_answer = input("Is this a/an: \n a) Bobo Ninja? \n b) Bobo Baby? \n c) Bobo in Love? \n d) Any other Type of Bobo Pack? \n e) Some sort of Weird Character? \n f) Indonesian Character for Natives? \n g) Indonesian Character for Non-Natives? \n h) Snow Character? \n i) Cute Character? \n j) Cute Animal? \n k) Unattractive Character?")
#cut to q_answer if value
        all_actions = {
        'a': 0.17721, 'b': 0.27957, 'c': 0.46689 , 'd': 0.13799, 'e': 0.17860, 'f': 0.22317, 'g': 0.10486,
        'h': 0.13113, 'i': 0.23240, 'j': 0.13806, 'k': 0.12175
                    }
        if q13_answer.lower() == 'a':
            a_count += (all_actions.get('a'))
        elif q13_answer.lower() =='b':
            a_count += (all_actions.get('b'))
        elif q13_answer.lower() =='c':
            a_count += (all_actions.get('c'))
        elif q13_answer.lower() =='d':
            a_count += (all_actions.get('d'))
        elif q13_answer.lower() =='e':
            a_count += (all_actions.get('e'))
        elif q13_answer.lower() =='f':
            a_count += (all_actions.get('f'))
        elif q13_answer.lower() =='g':
            a_count += (all_actions.get('g'))
        elif q13_answer.lower() =='h':
            a_count += (all_actions.get('h'))
        elif q13_answer.lower() =='i':
            a_count += (all_actions.get('i'))
        elif q13_answer.lower() =='j':
            a_count += (all_actions.get('j'))
        elif q13_answer.lower() =='k':
            a_count += (all_actions.get('k'))
        else: print("Sorry, I don't understand that response.")

        if q13_answer.lower() =='a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k':
            q321_answer = input("What is the second closest type of sticker pack? \n a) Bobo Ninja? \n b) Bobo Baby? \n c) Bobo in Love? \n d) Any other Type of Bobo Pack? \n e) Some sort of Weird Character? \n f) Indonesian Character for Natives? \n g) Indonesian Character for Non-Natives? \n h) Snow Character? \n i) Cute Character? \n j) Cute Animal? \n k) Unattractive Character?")

        if q321_answer.lower() == 'a':
            a_count += (all_actions.get('a'))
        elif q321_answer.lower() =='b':
            a_count += (all_actions.get('b'))
        elif q321_answer.lower() =='c':
            a_count += (all_actions.get('c'))
        elif q321_answer.lower() =='d':
            a_count += (all_actions.get('d'))
        elif q321_answer.lower() =='e':
            a_count += (all_actions.get('e'))
        elif q321_answer.lower() =='f':
            a_count += (all_actions.get('f'))
        elif q321_answer.lower() =='g':
            a_count += (all_actions.get('g'))
        elif q321_answer.lower() =='h':
            a_count += (all_actions.get('h'))
        elif q321_answer.lower() =='i':
            a_count += (all_actions.get('i'))
        elif q321_answer.lower() =='j':
            a_count += (all_actions.get('j'))
        elif q321_answer.lower() =='k':
            a_count += (all_actions.get('k'))
        else: print("Sorry, I don't understand that response.")

        if q321_answer.lower() == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k':
                q421_answer = input("Is this pack animated? \n a) Yes \n b) No")

                eroel_animated = {
                'a': 0.14283, 'b': 0.15143, 'c': 0.16104, 'd': 0.15143, 'e': 0.15143, 'f': 0.15143, 'g': 0.15143
                        }
                eroel_static = {
                'a': 0.17562, 'b': 0.22101, 'c': 0.25220, 'd': 0.22101, 'e': 0.22101, 'f': 0.22101, 'g': 0.22101
                        }

                if q421_answer.lower() == 'a':
                            a_count += (eroel_animated.get('c'))

                if q421_answer.lower() == 'b':
                            a_count += (eroel_static.get('c'))

                if q421_answer.lower() == 'a' or 'b':
                        q521_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        eroel_text = {
                        'a': 0.11684, 'b': 0.18381, 'c': 0.19214, 'd': 0.51751, 'e': 0.18381, 'f': 0.18381, 'g': 0.18381
                        }
                        eroel_notext = {
                        'a': 0.17684, 'b': 0.18282, 'c': 0.18660, 'd': 0.24173, 'e': 0.18282, 'f': 0.18282, 'g': 0.18282
                        }
                        if q521_answer.lower() == 'a':
                                a_count += (eroel_text.get('c'))

                        if q521_answer.lower() == 'b':
                                a_count += (eroel_notext.get('c'))

                        if q521_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q2_answer.lower() =='d':
        q14_answer = input("Is this a/an: \n a) Pack with Couples in Love? \n b) Something Else?")
#cut to q_answer if value

        romance_eroel = {
        'a': 0.37962, 'b': 0.37962
                    }

        if q14_answer.lower() =='a':
            a_count += (romance_eroel.get('a'))
        elif q14_answer.lower() =='b':
            a_count += (romance_eroel.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q14_answer.lower() =='a' or 'b':
            q331_answer = input("What is the second closest type of sticker pack? \n a) Pack with Couples in Love? \n b) Something Else?")

        elif q331_answer.lower() =='a':
            a_count += (romance_eroel.get('a'))
        elif q331_answer.lower() =='b':
            a_count += (romance_eroel.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q331_answer.lower() == 'a' or 'b':
                q431_answer = input("Is this pack animated? \n a) Yes \n b) No")

        eroel_animated = {
        'a': 0.14283, 'b': 0.15143, 'c': 0.16104, 'd': 0.15143, 'e': 0.15143, 'f': 0.15143, 'g': 0.15143
                        }
        eroel_static = {
        'a': 0.17562, 'b': 0.22101, 'c': 0.25220, 'd': 0.22101, 'e': 0.22101, 'f': 0.22101, 'g': 0.22101
                        }
        front_style = {
        'a': 0.27100, 'b': 0.05206, 'c': 0.15311, 'd': 0.13803, 'e': 0.11882, 'f': 0.18237
                        }
        eroel_text = {
        'a': 0.11684, 'b': 0.18381, 'c': 0.19214, 'd': 0.51751, 'e': 0.18381, 'f': 0.18381, 'g': 0.18381
        }
        eroel_notext = {
        'a': 0.17684, 'b': 0.18282, 'c': 0.18660, 'd': 0.24173, 'e': 0.18282, 'f': 0.18282, 'g': 0.18282
        }

        if q431_answer.lower() == 'a':
                        a_count += (eroel_animated.get('d'))

        if q431_answer.lower() == 'b':
                        a_count += (eroel_static.get('d'))

        if q431_answer.lower() == 'a' or 'b':
                        q531_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        eroel_text = {
                        'a': 0.11684, 'b': 0.18381, 'c': 0.19214, 'd': 0.51751, 'e': 0.18381, 'f': 0.18381, 'g': 0.18381
                        }
                        eroel_notext = {
                        'a': 0.17684, 'b': 0.18282, 'c': 0.18660, 'd': 0.24173, 'e': 0.18282, 'f': 0.18282, 'g': 0.18282
                        }
                        if q531_answer.lower() == 'a':
                                a_count += (eroel_text.get('d'))

                        if q531_answer.lower() == 'b':
                                a_count += (eroel_notext.get('d'))

                        if q531_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q2_answer.lower() =='e':
        q15_answer = input("Is this a/an: \n a) Winter Sports Pack? \n b) Bobo Sports Pack? \n c) Something Else?")

#cut to q_answer if value
        sports_eroel = {
        'a': 0.14987, 'b': 0.11843, 'c': 0.14987
            }
        if q15_answer.lower() =='a':
            a_count += (sports_eroel.get('a'))
        elif q15_answer.lower() =='b':
            a_count += (sports_eroel.get('b'))
        elif q15_answer.lower() =='c':
            a_count += (sports_eroel.get('c'))
        else: print("Sorry, I don't understand that response.")

        if q15_answer.lower() =='a' or 'b' or 'c':
            q341_answer = input("What is the second closest type of sticker pack? \n a) Winter Sports Pack? \n b) Bobo Sports Pack? \n c) Something Else?")

        if q341_answer.lower() =='a':
            a_count += (sports_eroel.get('a'))
        elif q341_answer.lower() =='b':
            a_count += (sports_eroel.get('b'))
        elif q341_answer.lower() =='c':
            a_count += (sports_eroel.get('c'))
        else: print("Sorry, I don't understand that response.")

        if q341_answer.lower() == 'a' or 'b' or 'c':
                q441_answer = input("Is this pack animated? \n a) Yes \n b) No")

                eroel_animated = {
                'a': 0.14283, 'b': 0.15143, 'c': 0.16104, 'd': 0.15143, 'e': 0.15143, 'f': 0.15143, 'g': 0.15143
                        }
                eroel_static = {
                'a': 0.17562, 'b': 0.22101, 'c': 0.25220, 'd': 0.22101, 'e': 0.22101, 'f': 0.22101, 'g': 0.22101
                        }

                if q441_answer.lower() == 'a':
                        a_count += (eroel_animated.get('e'))


                if q441_answer.lower() == 'b':
                        a_count += (eroel_static.get('e'))

                if q441_answer.lower() == 'a' or 'b':
                        q541_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        eroel_text = {
                        'a': 0.11684, 'b': 0.18381, 'c': 0.19214, 'd': 0.51751, 'e': 0.18381, 'f': 0.18381, 'g': 0.18381
                        }
                        eroel_notext = {
                        'a': 0.17684, 'b': 0.18282, 'c': 0.18660, 'd': 0.24173, 'e': 0.18282, 'f': 0.18282, 'g': 0.18282
                        }
                        if q541_answer.lower() == 'a':
                                a_count += (eroel_text.get('e'))

                        if q541_answer.lower() == 'b':
                                a_count += (eroel_notext.get('e'))

                        if q541_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q2_answer.lower() =='f':
        q16_answer = input("Is this a/an: \n a) Cute Animal? \n b) Something Else?")

#cut to q_answer if value
        high_variety = {
        'a': 0.17618, 'b': 0.18627
                    }
        if q16_answer.lower() =='a':
            a_count += (high_variety.get('a'))
        elif q16_answer.lower() =='b':
            a_count += (high_variety.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q16_answer.lower() =='a' or 'b':
            q351_answer = input("What is the second closest type of sticker pack? \n a) Cute Animal? \n b) Something Else?")

        if q351_answer.lower() =='a':
            a_count += (high_variety.get('a'))
        elif q351_answer.lower() =='b':
            a_count += (high_variety.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q351_answer.lower() == 'a' or 'b':
                q451_answer = input("Is this pack animated? \n a) Yes \n b) No")

                eroel_animated = {
                'a': 0.14283, 'b': 0.15143, 'c': 0.16104, 'd': 0.15143, 'e': 0.15143, 'f': 0.15143, 'g': 0.15143
                        }
                eroel_static = {
                'a': 0.17562, 'b': 0.22101, 'c': 0.25220, 'd': 0.22101, 'e': 0.22101, 'f': 0.22101, 'g': 0.22101
                        }

                if q451_answer.lower() == 'a':
                        a_count += (eroel_animated.get('f'))

                if q451_answer.lower() == 'b':
                        a_count += (eroel_static.get('f'))

                if q451_answer.lower() == 'a' or 'b':
                        q551_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        eroel_text = {
                            'a': 0.11684, 'b': 0.18381, 'c': 0.19214, 'd': 0.51751, 'e': 0.18381, 'f': 0.18381, 'g': 0.18381
                            }
                        eroel_notext = {
                            'a': 0.17684, 'b': 0.18282, 'c': 0.18660, 'd': 0.24173, 'e': 0.18282, 'f': 0.18282, 'g': 0.18282
                            }
                        if q551_answer.lower() == 'a':
                                a_count += (eroel_text.get('g'))

                        if q551_answer.lower() == 'b':
                                a_count += (eroel_notext.get('f'))

                        if q551_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q2_answer.lower() =='g':
        q17_answer = input("Is this a/an: \n a) Pack with Objects? \n b) Something Else?")

#cut to q_answer if value
        creative_eroel = {
        'a': 0.10537, 'b': 0.10537
                    }
        if q17_answer.lower() =='a':
            a_count += (creative_eroel.get('a'))
        elif q17_answer.lower() =='b':
            a_count += (creative_eroel.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q17_answer.lower() =='a' or 'b':
            q361_answer = input("What is the second closest type of sticker pack? \n a) Pack with Objects? \n b) Something Else?")

        if q361_answer.lower() =='a':
            a_count += (creative_eroel.get('a'))
        elif q361_answer.lower() =='b':
            a_count += (creative_eroel.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q361_answer.lower() == 'a' or 'b':
                q461_answer = input("Is this pack animated? \n a) Yes \n b) No")

                eroel_animated = {
                'a': 0.14283, 'b': 0.15143, 'c': 0.16104, 'd': 0.15143, 'e': 0.15143, 'f': 0.15143, 'g': 0.15143
                        }
                eroel_static = {
                'a': 0.17562, 'b': 0.22101, 'c': 0.25220, 'd': 0.22101, 'e': 0.22101, 'f': 0.22101, 'g': 0.22101
                        }

                if q461_answer.lower() == 'a':
                        a_count += (eroel_animated.get('g'))

                if q461_answer.lower() == 'b':
                        a_count += (eroel_static.get('g'))

                if q461_answer.lower() == 'a' or 'b':
                        q561_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        eroel_text = {
                        'a': 0.11684, 'b': 0.18381, 'c': 0.19214, 'd': 0.51751, 'e': 0.18381, 'f': 0.18381, 'g': 0.18381
                        }
                        eroel_notext = {
                        'a': 0.17684, 'b': 0.18282, 'c': 0.18660, 'd': 0.24173, 'e': 0.18282, 'f': 0.18282, 'g': 0.18282
                        }
                        if q561_answer.lower() == 'a':
                                a_count += (eroel_text.get('g'))

                        if q561_answer.lower() == 'b':
                                a_count += (eroel_notext.get('g'))

                        if q561_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

if q1_answer.lower() =='b':
    q3_answer = input("Select the type of sticker style you feel best reflects the sticker being deployed. \n a) KMK Studios' Cartoon Style Type? \n b) KMK Studios' Variety of Positions Style Type? \n c) KMK Studios' Sports Style Type? \n d) KMK Studios' Expressions Style Type? \n e) KMK Studios' Light Colour and No Borders Style Type?")
    if q3_answer.lower() =='a':
        q21_answer = input("Is this a/an: \n a) Cute Character? \n b) Cute Animal?")

        kmk_animated = {
        'a': 0.26361, 'b': 0.17988, 'c': 0.11903, 'd': 0.27208, 'e': 0.14947
                        }

        kmk_static = {
        'a': 0.20741, 'b': 0.20741, 'c': 0.06918, 'd': 0.27652, 'e': 0.20741
                        }

        kmk_text = {
        'a': 0.26006, 'b': 0.19094, 'c': 0.22185, 'd': 0.20838, 'e': 0.22185
        }
        kmk_notext = {
        'a': 0.27429, 'b': 0.14119, 'c': 0.20420, 'd': 0.40835, 'e': 0.14947
        }

        cartoon_kmk = {
        'a': 0.27289, 'b': 0.25434
                        }
#cut to q_answer if value
        if q21_answer.lower() =='a':
            a_count += (cartoon_kmk.get('a'))
        elif q21_answer.lower() == 'b':
            a_count += (cartoon_kmk.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q21_answer.lower() =='a' or 'b':
            q371_answer = input("What is the second closest type of sticker pack? \n a) Cute Character? \n b) Cute Animal?")

        if q371_answer.lower() =='a':
            a_count += (cartoon_kmk.get('a'))
        elif q371_answer.lower() == 'b':
            a_count += (cartoon_kmk.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q371_answer.lower() == 'a' or 'b':
                q471_answer = input("Is this pack animated? \n a) Yes \n b) No")

                kmk_animated = {
                'a': 0.26361, 'b': 0.17988, 'c': 0.11903, 'd': 0.27208, 'e': 0.14947
                                }

                kmk_static = {
                'a': 0.20741, 'b': 0.20741, 'c': 0.06918, 'd': 0.27652, 'e': 0.20741
                                }

                if q471_answer.lower() == 'a':
                        a_count += (kmk_animated.get('a'))

                if q471_answer.lower() == 'b':
                        a_count += (kmk_static.get('a'))

                if q471_answer.lower() == 'a' or 'b':
                        q571_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")
                        if q571_answer.lower() == 'a':
                                a_count += (kmk_text.get('a'))

                        if q571_answer.lower() == 'b':
                                a_count += (kmk_notext.get('a'))

                        if q571_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q3_answer.lower() =='b':
        q22_answer = input("Is this a/an: \n a) Cute Animal? \n b) Food Character? \n c) Weird Character? \n d) Cute Character? \n e) Indonesian Character?")

#cut to q_answer if value
        variety_positions = {
        'a': 0.20270, 'b': 0.20082, 'c': 0.19046, 'd': 0.09192, 'e': 0.21585
                    }
        if q22_answer.lower() =='a':
            a_count += (variety_positions.get('a'))
        elif q22_answer.lower() =='b':
            a_count += (variety_positions.get('b'))
        elif q22_answer.lower() =='c':
            a_count += (variety_positions.get('c'))
        elif q22_answer.lower() =='d':
            a_count += (variety_positions.get('d'))
        elif q22_answer.lower() =='e':
            a_count += (variety_positions.get('e'))
        else: print("Sorry, I don't understand that response.")

        if q22_answer.lower() =='a' or 'b' or 'c' or 'd' or 'e':
                q381_answer = input("What is the second closest type of sticker pack? \n a) Cute Animal? \n b) Food Character? \n c) Weird Character? \n d) Cute Character? \n e) Indonesian Character?")

        if q381_answer.lower() =='a':
            a_count += (variety_positions.get('a'))
        elif q381_answer.lower() =='b':
            a_count += (variety_positions.get('b'))
        elif q381_answer.lower() =='c':
            a_count += (variety_positions.get('c'))
        elif q381_answer.lower() =='d':
            a_count += (variety_positions.get('d'))
        elif q381_answer.lower() =='e':
            a_count += (variety_positions.get('e'))
        else: print("Sorry, I don't understand that response.")

        if q381_answer.lower() =='a' or 'b' or 'c' or 'd' or 'e':
                q481_answer = input("Is this pack animated? \n a) Yes \n b) No")
                kmk_animated = {
                'a': 0.26361, 'b': 0.17988, 'c': 0.11903, 'd': 0.27208, 'e': 0.14947
                                }

                kmk_static = {
                'a': 0.20741, 'b': 0.20741, 'c': 0.06918, 'd': 0.27652, 'e': 0.20741
                                }

                if q481_answer.lower() == 'a':
                        a_count += (kmk_animated.get('b'))

                if q481_answer.lower() == 'b':
                        a_count += (kmk_static.get('b'))

                if q481_answer.lower() == 'a' or 'b':
                        q581_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        kmk_text = {
                        'a': 0.26006, 'b': 0.19094, 'c': 0.22185, 'd': 0.20838, 'e': 0.22185
                        }
                        kmk_notext = {
                        'a': 0.27429, 'b': 0.14119, 'c': 0.20420, 'd': 0.40835, 'e': 0.14947
                        }
                        kmk_animated = {
                        'a': 0.26361, 'b': 0.17988, 'c': 0.11903, 'd': 0.27208, 'e': 0.14947
                                                }
                        kmk_static = {
                        'a': 0.20741, 'b': 0.20741, 'c': 0.06918, 'd': 0.27652, 'e': 0.20741
                                                }

                        if q581_answer.lower() == 'a':
                                a_count += (kmk_text.get('b'))

                        if q581_answer.lower() == 'b':
                                a_count += (kmk_notext.get('b'))

                        if q581_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q3_answer.lower() =='c':
        q23_answer = input("Is this a/an: \n a) Soccer Pack? \n Something Else?")
        if q23_answer.lower() =='a' or 'b':

#cut to q_answer if value
                    sports_kmk = {
                    'a': 0.09006, 'b': 0.09006
                    }
        if q23_answer.lower() =='a':
            a_count += (sports_kmk.get('a'))
        elif q23_answer.lower() =='b':
            a_count += (sports_kmk.get('b'))
        else: print("Sorry, I don't understand that response.")

        q391_answer = input("What is the second closest type of sticker pack? \n a) Soccer Pack? \n b) Something Else?")

        if q391_answer.lower() =='a':
            a_count += (sports_kmk.get('a'))
        elif q391_answer.lower() =='b':
            a_count += (sports_kmk.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q391_answer.lower() == 'a' or 'b':
                q491_answer = input("Is this pack animated? \n a) Yes \n b) No")

                kmk_animated = {
                'a': 0.26361, 'b': 0.17988, 'c': 0.11903, 'd': 0.27208, 'e': 0.14947
                                }
                kmk_static = {
                'a': 0.20741, 'b': 0.20741, 'c': 0.06918, 'd': 0.27652, 'e': 0.20741
                                }

                if q491_answer.lower() == 'a':

                        a_count += (kmk_animated.get('c'))


                if q491_answer.lower() == 'b':

                        a_count += (kmk_static.get('c'))

                if q491_answer.lower() == 'a' or 'b':
                        q591_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        kmk_text = {
                        'a': 0.26006, 'b': 0.19094, 'c': 0.22185, 'd': 0.20838, 'e': 0.22185
                        }
                        kmk_notext = {
                        'a': 0.27429, 'b': 0.14119, 'c': 0.20420, 'd': 0.40835, 'e': 0.14947
                        }
                        if q591_answer.lower() == 'a':
                                a_count += (kmk_text.get('c'))

                        if q591_answer.lower() == 'b':
                                a_count += (kmk_notext.get('c'))

                        if q591_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q3_answer.lower() =='d':
        q24_answer = input("Is this a/an: \n a) Pack full of different Colours? \n b) Pack with a Consistent Colour or Design?")

        expresions_kmk = {
        'a': 0.20838, 'b': 0.40835
                    }
        if q24_answer.lower() =='a':
            a_count += (expresions_kmk.get('a'))
        elif q24_answer.lower() =='b':
            a_count += (expresions_kmk.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q24_answer.lower() =='a' or 'b':
                q3101_answer = input("What is the second closest type of sticker pack? \n a) Pack full of different Colours? \n b) Pack with a Consistent Colour or Design?")

#cut to q_answer if value

                if q3101_answer.lower() =='a':
                    a_count += (expresions_kmk.get('a'))
                elif q3101_answer.lower() =='b':
                    a_count += (expresions_kmk.get('b'))
                else: print("Sorry, I don't understand that response.")

                if q3101_answer.lower() == 'a' or 'b':
                        q4101_answer = input("Is this pack animated? \n a) Yes \n b) No")

                        kmk_animated = {
                        'a': 0.26361, 'b': 0.17988, 'c': 0.11903, 'd': 0.27208, 'e': 0.14947
                                    }

                        kmk_static = {
                        'a': 0.20741, 'b': 0.20741, 'c': 0.06918, 'd': 0.27652, 'e': 0.20741
                                    }

                        if q4101_answer.lower() == 'a':
                                a_count += (kmk_animated.get('d'))

                        if q4101_answer.lower() == 'b':
                                a_count += (kmk_static.get('d'))

                        if q4101_answer.lower() == 'a' or 'b':
                                q5101_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                                kmk_text = {
                                'a': 0.26006, 'b': 0.19094, 'c': 0.22185, 'd': 0.20838, 'e': 0.22185
                                }
                                kmk_notext = {
                                'a': 0.27429, 'b': 0.14119, 'c': 0.20420, 'd': 0.40835, 'e': 0.14947
                                }

                                if q5101_answer.lower() == 'a':
                                        a_count += (kmk_text.get('d'))

                                if q5101_answer.lower() == 'b':
                                        a_count += (kmk_notext.get('d'))

                                if q5101_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q3_answer.lower() =='e':
        q25_answer = input("Is this a/an: \n a) Cute Animal? \n b) Something Else?")

#cut to q_answer if value

        light_colour_kmk = {
        'a': 0.14947, 'b': 0.14947
                    }
        if q25_answer.lower() =='a' or 'b':

            if q25_answer.lower() == 'a':
                a_count += (light_colour_kmk.get('a'))
            if q25_answer.lower() == 'b':
                a_count += (light_colour_kmk.get('b'))

            q3111_answer = input("What is the second closest type of sticker pack? \n a) Cute Animal? \n b) Something Else?")

            if q3111_answer.lower() == 'a':
                a_count += (light_colour_kmk.get('a'))
            if q3111_answer.lower() == 'b':
                a_count += (light_colour_kmk.get('b'))
            else: print("Sorry, I don't understand that response.")

            if q3111_answer.lower() == 'a' or 'b':
                    q4111_answer = input("Is this pack animated? \n a) Yes \n b) No")

                    kmk_animated = {
                    'a': 0.26361, 'b': 0.17988, 'c': 0.11903, 'd': 0.27208, 'e': 0.14947
                                    }

                    kmk_static = {
                    'a': 0.20741, 'b': 0.20741, 'c': 0.06918, 'd': 0.27652, 'e': 0.20741
                                    }
                    if q4111_answer.lower() == 'a':
                            a_count += (kmk_animated.get('e'))

                    if q4111_answer.lower() == 'b':
                            a_count += (kmk_static.get('e'))

                    if q4111_answer.lower() == 'a' or 'b':
                        q5111_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        kmk_text = {
                        'a': 0.26006, 'b': 0.19094, 'c': 0.22185, 'd': 0.20838, 'e': 0.22185
                        }
                        kmk_notext = {
                        'a': 0.27429, 'b': 0.14119, 'c': 0.20420, 'd': 0.40835, 'e': 0.14947
                        }
                        if q5111_answer.lower() == 'a':
                                a_count += (kmk_text.get('e'))

                        if q5111_answer.lower() == 'b':
                                a_count += (kmk_notext.get('e'))

                        if q5111_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

if q1_answer.lower() =='c':
    q4_answer = input("Select the type of sticker style you feel best reflects the sticker being deployed. \n a) Susilo's Native Indonesian Style? \n b) Susilo's Non-Native Indonesian Style? \n c) Susilo's Romance Style? \n d) Susilo's Rest of World Style?")
    if q4_answer.lower() =='a':
        q31_answer = input("Is this a/an: \n a) Indonesian Character? \n b) Something Else?")

        if q31_answer.lower() =='a' or 'b':
            q3121_answer = input("What is the second closest type of sticker pack? \n a) Indonesian Character? \n b) Something Else?")

#cut to q_answer if value
            native_susilo = {
            'a': 0.23955, 'b': 0.23955
                    }
        if q31_answer.lower() =='a':
            a_count += (native_susilo.get('a'))
        elif q31_answer.lower() =='b':
            a_count += (native_susilo.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q3121_answer.lower() =='a':
            a_count += (native_susilo.get('a'))
        elif q3121_answer.lower() =='b':
            a_count += (native_susilo.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q3121_answer.lower() == 'a' or 'b':
                q4121_answer = input("Is this pack animated? \n a) Yes \n b) No")

                susilo_animated = {
                'a': 0.17886, 'b': 0.15054, 'c': 0.18912, 'd': 0.14931
                }
                susilo_static = {
                'a': 0.25479, 'b': 0.22776, 'c': 0.19183, 'd': 0.22776
                }
                susilo_text = {
                'a': 0.19088, 'b': 0.19088, 'c': 0.19088, 'd': 0.14254
                }
                susilo_notext = {
                'a': 0.17596, 'b': 0.17596, 'c': 0.17596, 'd': 0.16280
                }

                if q4121_answer.lower() == 'a':
                        a_count += (susilo_animated.get('a'))

                if q4121_answer.lower() =='b':
                        a_count += (susilo_static.get('a'))

                if q4121_answer.lower() == 'a' or 'b':
                        q5121_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        susilo_text = {
                        'a': 0.19088, 'b': 0.19088, 'c': 0.19088, 'd': 0.14254
                        }
                        susilo_notext = {
                        'a': 0.17596, 'b': 0.17596, 'c': 0.17596, 'd': 0.16280
                        }

                        if q5121_answer.lower() == 'a':
                                a_count += (susilo_text.get('a'))

                        if q5121_answer.lower() == 'b':
                                a_count += (susilo_notext.get('a'))

                        if q5121_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q4_answer.lower() =='b':
        q32_answer = input("Is this a/an: \n a) Indonesian Character? \n b) Rest of World Character? \n c) Non-Human Character")

#cut to q_answer if value
        nonnative_susilo = {
        'a': 0.21084, 'b': 0.12546, 'c': 0.21776
                    }
        if q32_answer.lower() =='a':
            a_count += (nonnative_susilo.get('a'))
        elif q32_answer.lower() =='b':
            a_count += (nonnative_susilo.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q32_answer.lower() =='a' or 'b':
            q3131_answer = input("What is the second closest type of sticker pack? \n a) Indonesian Character? \n b) Rest of World Character? \n c) Non-Human Character")

        if q3131_answer.lower() =='a':
            a_count += (nonnative_susilo.get('a'))
        elif q3131_answer.lower() =='b':
            a_count += (nonnative_susilo.get('b'))

        if q3131_answer.lower() == 'a' or 'b' or 'c':
                q4131_answer = input("Is this pack animated? \n a) Yes \n b) No")

                susilo_animated = {
                'a': 0.17886, 'b': 0.15054, 'c': 0.18912, 'd': 0.14931
                }
                susilo_static = {
                'a': 0.25479, 'b': 0.22776, 'c': 0.19183, 'd': 0.22776
                }

                if q4131_answer.lower() == 'a':
                        a_count += (susilo_animated.get('b'))

                if q4131_answer.lower() =='b':
                        a_count += (susilo_static.get('b'))

                if q4131_answer.lower() == 'a' or 'b':
                    q5131_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                    susilo_text = {
                    'a': 0.19088, 'b': 0.19088, 'c': 0.19088, 'd': 0.14254
                    }
                    susilo_notext = {
                    'a': 0.17596, 'b': 0.17596, 'c': 0.17596, 'd': 0.16280
                    }

                    if q5131_answer.lower() == 'a':
                            a_count += (susilo_text.get('b'))

                    if q5131_answer.lower() == 'b':
                            a_count += (susilo_notext.get('b'))

                    if q5131_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q4_answer.lower() =='c':
        q33_answer = input("Is this a/an: \n a) High Variety Pack? \n b) Consistent Character Pack?")

#cut to q_answer if value
        romance_susilo = {
        'a': 0.27656, 'b': 0.12028
                    }
        if q33_answer.lower() =='a':
            a_count += (romance_susilo.get('a'))
        elif q33_answer.lower() =='b':
            a_count += (romance_susilo.get('b'))
        else: print("Sorry, I don't understand that response.")


        if q33_answer.lower() =='a' or 'b':
                q3141_answer = input("What is the second closest type of sticker pack? \n a) High Variety Pack? \n b) Consistent Character Pack?")
                if q3141_answer.lower() == 'a' or 'b':

                    if q3141_answer.lower() =='a':
                        a_count += (romance_susilo.get('a'))
                    elif q3141_answer.lower() =='b':
                        a_count += (romance_susilo.get('b'))
                    else: print("Sorry, I don't understand that response.")

                    q4141_answer = input("Is this pack animated? \n a) Yes \n b) No")

                    susilo_animated = {
                    'a': 0.17886, 'b': 0.15054, 'c': 0.18912, 'd': 0.14931
                    }
                    susilo_static = {
                    'a': 0.25479, 'b': 0.22776, 'c': 0.19183, 'd': 0.22776
                    }

                    if q4141_answer.lower() == 'a':
                                a_count += (susilo_animated.get('c'))

                    if q4141_answer.lower() =='b':
                                a_count += (susilo_static.get('c'))


                    if q4141_answer.lower() == 'a' or 'b':
                        q5141_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        susilo_text = {
                        'a': 0.19088, 'b': 0.19088, 'c': 0.19088, 'd': 0.14254
                        }
                        susilo_notext = {
                        'a': 0.17596, 'b': 0.17596, 'c': 0.17596, 'd': 0.16280
                        }

                        if q5141_answer.lower() == 'a':
                                a_count += (susilo_text.get('c'))

                        if q5141_answer.lower() == 'b':
                                a_count += (susilo_notext.get('c'))

                        if q5141_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q4_answer.lower() =='d':
        q34_answer = input("Is this a/an: \n a) Normal Character? \n b) Weird Character? \n c) Animal or Creature?")

#cut to q_answer if value
        row_susilo = {
        'a': 0.14240, 'b': 0.14232, 'c': 0.16248
                    }
        if q34_answer.lower() =='a':
            a_count += (row_susilo.get('a'))
        elif q34_answer.lower() =='b':
            a_count += (row_susilo.get('b'))
        elif q34_answer.lower() =='c':
            a_count += (row_susilo.get('c'))
        else: print("Sorry, I don't understand that response.")


        if q34_answer.lower() =='a' or 'b' or 'c':
            q3151_answer = input("What is the second closest type of sticker pack? \n a) Normal Character? \n b) Weird Character? \n c) Animal or Creature?")

            if q3151_answer.lower() =='a':
                a_count += (row_susilo.get('a'))
            elif q3151_answer.lower() =='b':
                a_count += (row_susilo.get('b'))
            elif q3151_answer.lower() =='c':
                a_count += (row_susilo.get('c'))
            else: print("Sorry, I don't understand that response.")

            if q3151_answer.lower() == 'a' or 'b' or 'c':
                    q4151_answer = input("Is this pack animated? \n a) Yes \n b) No")

                    susilo_animated = {
                    'a': 0.17886, 'b': 0.15054, 'c': 0.18912, 'd': 0.14931
                    }
                    susilo_static = {
                    'a': 0.25479, 'b': 0.22776, 'c': 0.19183, 'd': 0.22776
                    }

                    if q4151_answer.lower() == 'a':
                            a_count += (susilo_animated.get('d'))

                    if q4151_answer.lower() =='b':
                                a_count += (susilo_static.get('d'))

            if q4151_answer.lower() == 'a' or 'b':
                    q5151_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                    susilo_text = {
                    'a': 0.19088, 'b': 0.19088, 'c': 0.19088, 'd': 0.14254
                    }
                    susilo_notext = {
                    'a': 0.17596, 'b': 0.17596, 'c': 0.17596, 'd': 0.16280
                    }

                    if q5151_answer.lower() == 'a':
                            a_count += (susilo_text.get('d'))

                    if q5151_answer.lower() == 'b':
                            a_count += (susilo_notext.get('d'))

                    if q5151_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

if q1_answer.lower() =='d':
    q5_answer = input("Select the type of sticker style you feel best reflects the sticker being deployed. \n a) Kun Widiarso's Front Style? \n b) All Other Styles by Kun Widiarso?")
    if q5_answer.lower() =='a':
        q41_answer = input("Is this a/an: \n a) Cute Character? \n b) Close Up Character with just the Head Showing?")
#cut to q_answer if value
        cute_kunwidiarso = {
        'a': 0.18389000, 'b': 0.22222
                    }
        if q41_answer.lower() =='a':
            a_count += (cute_kunwidiarso.get('a'))
        elif q41_answer.lower() =='b':
            a_count += (cute_kunwidiarso.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q41_answer.lower() =='a' or 'b':
            q3161_answer = input("What is the second closest type of sticker pack? \n a) Cute Character? \n b) Close Up Character with just the Head Showing?")

            if q3161_answer.lower() =='a':
                a_count += (cute_kunwidiarso.get('a'))
            elif q3161_answer.lower() =='b':
                a_count += (cute_kunwidiarso.get('b'))
            else: print("Sorry, I don't understand that response.")

            if q3161_answer.lower() == 'a' or 'b':
                q4161_answer = input("Is this pack animated? \n a) Yes \n b) No")

                kun_animated = {
                'a': 0.20306, 'b': 0.20306
                        }
                kun_static = {
                'a': 0.20306, 'b': 0.20306
                        }
                kun_text = {
                'a': 0.20306, 'b': 0.20306
                }
                kun_notext = {
                'a': 0.20306, 'b': 0.20306
                }
                if q4161_answer.lower() == 'a':
                        a_count += (kun_animated.get('a'))

                if q4161_answer.lower() =='b':
                        a_count += (kun_static.get('a'))

                if q4161_answer.lower() == 'a' or 'b':
                        q5161_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                        kun_text = {
                        'a': 0.20306, 'b': 0.20306
                        }
                        kun_notext = {
                        'a': 0.20306, 'b': 0.20306
                        }

                        if q5161_answer.lower() == 'a':
                                a_count += (kun_text.get('a'))

                        if q5161_answer.lower() == 'b':
                                a_count += (kun_notext.get('a'))

                        if q5161_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q5_answer.lower() =='b':
        q42_answer = input("Is this a/an: \n a) Cute Character?")

        cute_kunwidiarsoothers = {
        'a': 0.20306
                    }
        if q42_answer.lower() == 'a':
            a_count += (cute_kunwidiarsoothers.get('a'))

            if q42_answer.lower() =='a':
                q3171_answer = input("What is the second closest type of sticker pack? \n a) Since there is none, press a to continue.")

                if q3171_answer.lower() =='a':
                    a_count += (cute_kunwidiarsoothers.get('a'))

                    if q3171_answer.lower() == 'a':
                        q4171_answer = input("Is this pack animated? \n a) Yes \n b) No")

                        kun_animated = {
                        'a': 0.20306, 'b': 0.20306
                        }

                        kun_static = {
                        'a': 0.20306, 'b': 0.20306
                        }

                        if q4171_answer.lower() == 'a':
                                a_count += (kun_animated.get('b'))

                        if q4171_answer.lower() =='b':
                                a_count += (kun_static.get('b'))

                        if q4161_answer.lower() == 'a' or 'b':
                            q5171_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                            kun_text = {
                            'a': 0.20306, 'b': 0.20306
                            }
                            kun_notext = {
                            'a': 0.20306, 'b': 0.20306
                            }

                            if q5171_answer.lower() == 'a':
                                    a_count += (kun_text.get('b'))

                            if q5171_answer.lower() == 'b':
                                    a_count += (kun_notext.get('b'))

                            if q5171_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

if q1_answer.lower() =='e':
    q6_answer = input("Select the type of sticker style you feel best reflects the sticker being deployed. \n a) BBM Family Activities Style? \n b) BBM Individual Characters Style? \n c) BBM Romance Style? \n d) BBM 3D Style?")
    if q6_answer.lower() =='a':
        q51_answer = input("Is this a/an: \n a) Pack Illustrating Fun Activities Excluding Holiday Activities? \n b) Only Deployable in Indonesia? \n c) Pack for a Public ROW Holiday? \n d) Pack for an Indonesian Holiday?")

#cut to q_answer if value
        familyactivities_bbm = {
        'a': 0.20606, 'b': 0.23000, 'c': 0.18948, 'd': 0.30645
                    }
        if q51_answer.lower() =='a':
            a_count += (familyactivities_bbm.get('a'))
        elif q51_answer.lower() =='b':
            a_count += (familyactivities_bbm.get('b'))
        elif q51_answer.lower() =='c':
            a_count += (familyactivities_bbm.get('c'))
        elif q51_answer.lower() =='d':
            a_count += (familyactivities_bbm.get('d'))
        else: print("Sorry, I don't understand that response.")

        if q51_answer.lower() =='a' or 'b' or 'c' or 'd':
            q3181_answer = input("What is the second closest type of sticker pack? \n a) Pack Illustrating Fun Activities Excluding Holiday Activities? \n b) Only Deployable in Indonesia? \n c) Pack for a Public ROW Holiday? \n d) Pack for an Indonesian Holiday?")

            if q3181_answer.lower() =='a':
                a_count += (familyactivities_bbm.get('a'))
            elif q3181_answer.lower() =='b':
                a_count += (familyactivities_bbm.get('b'))
            elif q3181_answer.lower() =='c':
                a_count += (familyactivities_bbm.get('c'))
            elif q3181_answer.lower() =='d':
                a_count += (familyactivities_bbm.get('d'))
            else: print("Sorry, I don't understand that response.")


            if q3181_answer.lower() == 'a' or 'b' or 'c' or 'd':
                q4181_answer = input("Is this pack animated? \n a) Yes \n b) No")

                bbm_animated = {
                'a': 0.18913, 'b': 0.18913, 'c': 0.18913, 'd': 0.18913
                        }
                bbm_static = {
                'a': 0.23295, 'b': 0.25220, 'c': 0.24257, 'd': 0.25220
                        }
                bbm_text = {
                'a': 0.21074, 'b': 0.20144, 'c': 0.20766, 'd': 0.20376
                        }
                bbm_notext = {
                'a': 0.21565, 'b': 0.22891, 'c': 0.20540, 'd': 0.20540
                        }
                if q4181_answer.lower() =='a':
                        a_count += (bbm_animated.get('a'))

                if q4181_answer.lower() =='b':
                        a_count += (bbm_static.get('a'))

                if q4181_answer.lower() == 'a' or 'b':
                    q5181_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                    bbm_text = {
                    'a': 0.21074, 'b': 0.20144, 'c': 0.20766, 'd': 0.20376
                        }
                    bbm_notext = {
                    'a': 0.21565
                        }
                    if q5181_answer.lower() == 'a':
                            a_count += (bbm_text.get('a'))

                    if q5181_answer.lower() == 'b':
                            a_count += (bbm_notext.get('a'))


                    if q5181_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q6_answer.lower() =='b':
        q52_answer = input("Is this a/an: \n a) Pack with Cotton? \n b) Pack with Joy? \n c) Pack with Alvin? \n d) Pack with Candy? \n e) Pack with Bud?")

        if q52_answer.lower() =='a' or 'b' or 'c' or 'd' or 'e':
            q3191_answer = input("What is the second closest type of sticker pack? \n a) Pack w/ Cotton? \n b) Pack w/ Joy? \n c) Pack w/ Alvin? \n d) Pack w/ Candy? \n e) Pack w/ Bud?")
#cut to q_answer if value
            characters_bbm = {
            'a': 0.26028, 'b': 0.15825, 'c': 0.24768, 'd': 0.12548, 'e': 0.04997
                    }
            if q52_answer.lower() =='a':
                a_count += (characters_bbm.get('a'))
            elif q52_answer.lower() =='b':
                a_count += (characters_bbm.get('b'))
            elif q52_answer.lower() =='c':
                a_count += (characters_bbm.get('c'))
            elif q52_answer.lower() =='d':
                a_count += (characters_bbm.get('d'))
            elif q52_answer.lower() =='e':
                a_count += (characters_bbm.get('e'))
            else: print("Sorry, I don't understand that response.")

            if q3191_answer.lower() =='a':
                a_count += (characters_bbm.get('a'))
            elif q3191_answer.lower() =='b':
                a_count += (characters_bbm.get('b'))
            elif q3191_answer.lower() =='c':
                a_count += (characters_bbm.get('c'))
            elif q3191_answer.lower() =='d':
                a_count += (characters_bbm.get('d'))
            elif q3191_answer.lower() =='e':
                a_count += (characters_bbm.get('e'))
            else: print("Sorry, I don't understand that response.")

            if q3191_answer.lower() == 'a' or 'b' or 'c' or 'd' or 'e':
                q4191_answer = input("Is this pack animated? \n a) Yes \n b) No")

                bbm_animated = {
                'a': 0.18913, 'b': 0.18913, 'c': 0.18913, 'd': 0.18913
                        }

                bbm_static = {
                'a': 0.23295, 'b': 0.25220, 'c': 0.24257, 'd': 0.25220
                        }

                if q4191_answer.lower() == 'a':
                        a_count += (bbm_animated.get('b'))


                if q4191_answer.lower() =='b':
                        a_count += (bbm_static.get('b'))

                if q4191_answer.lower() == 'a' or 'b':
                    q5191_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                    bbm_text = {
                    'a': 0.21074, 'b': 0.20144, 'c': 0.20766, 'd': 0.20376
                        }
                    bbm_notext = {
                    'a': 0.21565
                    }
                    if q5191_answer.lower() == 'a':
                            a_count += (bbm_text.get('b'))

                    if q5191_answer.lower() == 'b':
                            a_count += (bbm_notext.get('a'))

                    if q5191_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q6_answer.lower() =='c':
        q53_answer = input("Is this a/an: \n a) Pack about Love Stories or Romance? \n b) Something Else?")

#cut to q_answer if value
        romance_bbm = {
        'a': 0.21176, 'b': 0.20556
                    }
        if q53_answer.lower() =='a':
            a_count += (romance_bbm.get('a'))
        elif q53_answer.lower() =='b':
                a_count += (romance_bbm.get('b'))

                if q53_answer.lower() =='a' or 'b':
                    q3201_answer = input("What is the second closest type of sticker pack? \n a) Pack about Love Stories or Romance? \n b) Something Else?")

                    if q3201_answer.lower() =='a':
                        a_count += (romance_bbm.get('a'))
                    elif q3201_answer.lower() =='b':
                        a_count += (romance_bbm.get('b'))
                    else: print("Sorry, I don't understand that response.")

                    if q3201_answer.lower() == 'a' or 'b':
                        q4201_answer = input("Is this pack animated? \n a) Yes \n b) No")

                        bbm_animated = {
                        'a': 0.18913, 'b': 0.18913, 'c': 0.18913, 'd': 0.18913
                        }

                        bbm_static = {
                        'a': 0.23295, 'b': 0.25220, 'c': 0.24257, 'd': 0.25220
                        }

                        if q4201_answer.lower() == 'a':
                                    a_count += (bbm_animated.get('c'))

                        if q4201_answer.lower() =='b':
                                    a_count += (bbm_static.get('c'))


                        if q4201_answer.lower() == 'a' or 'b':
                            q5201_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                            bbm_text = {
                            'a': 0.21074, 'b': 0.20144, 'c': 0.20766, 'd': 0.20376
                            }
                            bbm_notext = {
                            'a': 0.21565
                            }
                            if q5201_answer.lower() == 'a':
                                    a_count += (bbm_text.get('c'))

                            if q5201_answer.lower() == 'b':
                                    a_count += (bbm_notext.get('a'))


                            if q5201_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")

    if q6_answer.lower() =='d':
        q54_answer = input("Is this a/an: \n a) Pack icnluding Fun Activities? \n b) Something Else?")

#cut to q_answer if value
        threed_bbm = {
        'a': 0.17385, 'b': 0.17385
                    }
        if q54_answer.lower() =='a':
            a_count += (threed_bbm.get('a'))
        elif q54_answer.lower() =='b':
            a_count += (threed_bbm.get('b'))
        else: print("Sorry, I don't understand that response.")

        if q54_answer.lower() =='a' or 'b':
                q3211_answer = input("What is the second closest type of sticker pack? \n a) Pack icnluding Fun Activities? \n b) Something Else?")

                if q3211_answer.lower() =='a':
                    a_count += (threed_bbm.get('a'))
                elif q3211_answer.lower() =='b':
                    a_count += (threed_bbm.get('b'))
                else: print("Sorry, I don't understand that response.")

        if q3211_answer.lower() == 'a' or 'b':
                q4211_answer = input("Is this pack animated? \n a) Yes \n b) No")

                bbm_animated = {
                'a': 0.18913, 'b': 0.18913, 'c': 0.18913, 'd': 0.18913
                        }

                bbm_static = {
                'a': 0.23295, 'b': 0.25220, 'c': 0.24257, 'd': 0.25220
                        }

                if q4211_answer.lower() == 'a':
                        a_count += (bbm_animated.get('d'))

                if q4211_answer.lower() =='b':
                        a_count += (bbm_static.get('d'))

                if q4211_answer.lower() == 'a' or 'b':
                    q5221_answer = input("Is there text in at least half of the stickers? \n a) Yes \n b) No")

                    bbm_text = {
                    'a': 0.21074, 'b': 0.20144, 'c': 0.20766, 'd': 0.20376
                        }
                    bbm_notext = {
                    'a': 0.21565
                        }
                    if q5221_answer.lower() == 'a':
                            a_count += (bbm_text.get('d'))
                    if q5221_answer.lower() == 'b':
                            a_count += (bbm_notext.get('a'))

                    if q5221_answer.lower() == 'a' or 'b':
                                        if a_count >= 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be popular.")
                                        if 0.82224 <= a_count < 0.91883:
                                            print("According to existing Sticker Installation data, this pack has a likely chance to be popular.")
                                        if 0.66331 < a_count < 0.82224:
                                            print("According to existing Sticker Installation data, this pack will perform rather averagely.")
                                        if 0.59139 < a_count <= 0.66331:
                                            print("According to existing Sticker Installation data, this pack will may not perform as well as we hope.")
                                        if a_count <= 0.59139:
                                            print("According to existing Sticker Installation data, this pack has a very likely chance to be unpopular.")
