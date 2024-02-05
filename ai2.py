import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pygame
import time
import random
import subprocess as sp
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("GOOD MORNING!")
    
    elif hour >=12 and hour <18:
        speak("GOOD AFTERNOON!")
    
    else:
        speak("GOOD EVENING!")
    
    speak("NICE TO MEET YOU. HOW MAY I HELP YOU")


def takeCommand():
    #takes mic input to string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening . . .")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-us')
        print(f"USER SAID : {query}\n")
        
    except Exception as ex:
        print("SAY AGAIN")
        speak("SAY AGAIN PLEASE")
        return "NONE"    
    return query    


if __name__ == "__main__":
    speak("")
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching in wikipedia')
            query = query.replace('wikipedia', "")
            if "" in query:
                speak('what would you like to search')
                print("WHAT WOULD YOU LIKE TO SEARCH", query)
                query = takeCommand()
                
                try:
                    result = wikipedia.summary({query}, sentences = 5)
                    speak("According to wikipedia")
                    speak(result)
                    print(result)
                
                except:
                    speak("Sorry page not found. Try something else")
                
        if "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            print("YOUTUBE IS OPEN")

        if 'change voice' in query:
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)
        speak("Hello Sir, I have switched my voice. How is it?")
            
        if "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
            print("GOOGLE IS OPEN")
        if " open gmail" in query:
            speak("opening gmail")
            webbrowser.open("gmail.com")
            print("GMAIL IS OPEN")
            
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the current time is {strTime}") 
            print(strTime)
                                        
        if "college website" in query:
            speak("opening Darrang college website")
            webbrowser.open("darrangcollege.ac.in")
            print("website is open")
        
        if 'play in youtube' in query:
            speak('searching in youtube')
            query = query.replace('play in youtube', "")
            if "" in query:
                speak('what would you like to search')
                print("WHAT WOULD YOU LIKE TO SEARCH", query)
                query = takeCommand()
                
                try:
                    yt = kit.playonyt(query)
                    speak("Searching")
                    print(yt)
                    print(query)
                
                except:
                    speak("Sorry page not found. Try something else")
    
        if 'search in google' in query:
            speak('searching in google')
            query = query.replace('search in google', "")
            if "" in query:
                speak('what would you like to search')
                print("WHAT WOULD YOU LIKE TO SEARCH", query)
                query = takeCommand()
                
                try:
                    gle = kit.search(query)
                    speak("Searching")
                    print(gle)
                    speak(query)
                
                except:
                    speak("Sorry page not found. Try something else")

        if "snake game" in query:
            speak("starting snake game")
            print("Starting game")
            snake_speed = 15

            Window_x = 720
            window_y = 480

            black = pygame.Color(0, 0, 0)
            white = pygame.Color(255, 255, 255)
            red = pygame.Color(255, 0, 0)
            green = pygame.Color(0, 255, 0)
            blue = pygame.Color(0, 0, 255)


            pygame.init()

            pygame.display.set_caption("snakes")
            game_window = pygame.display.set_mode((Window_x, window_y))

            fps = pygame.time.Clock()


            snake_position = [100, 50]

            snake_body = [[100, 50],
                        [90, 50],
                        [80,50],
                        [70, 50]
                        ]

            fruit_position = [random.randrange(1, (Window_x//10)) * 10,
                            random.randrange(1, (window_y//10)) * 10]
            fruit_spawn = True

            direction = 'RIGHT'
            change_to = direction


            score = 0

            def show_score(choice, color, font, size):
                
                score_font = pygame.font.SysFont(font, size)
                
                score_surface = score_font.render('score : '+ str(score), True, color)
                
                score_rect = score_surface.get_rect()
                
                game_window.blit(score_surface, score_rect)
                
                
            def game_over():
                my_font = pygame.font.SysFont('times new roman', 50)
                
                game_over_surface = my_font.render('Your score is : '+ str(score), True, red)
                
                game_over_rect = game_over_surface.get_rect()
                
                game_over_rect.midtop = (Window_x/2, window_y/4)
                
                game_window.blit(game_over_surface, game_over_rect)
                pygame.display.flip()
                
                time.sleep(2)
                
                pygame.quit()
                
                quit()
                
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            change_to = 'UP'
                        if event.key == pygame.K_DOWN:
                            change_to = 'DOWN'
                        if event.key == pygame.K_LEFT:
                            change_to = 'LEFT'
                        if event.key == pygame.K_RIGHT:
                            change_to = 'RIGHT'
                
                if change_to == 'UP' and direction != 'DOWN':
                    direction = 'UP'
                if change_to == 'DOWN' and direction != 'UP':
                    direction = 'DOWN'
                if change_to == 'LEFT' and direction != 'RIGHT':
                    direction = 'LEFT'
                if change_to == 'RIGHT' and direction != 'LEFT':
                    direction = 'RIGHT'
                
                
                if direction == 'UP':
                    snake_position[1] -= 10
                if direction == 'DOWN':
                    snake_position[1] += 10
                if direction == 'LEFT':
                    snake_position[0] -= 10
                if direction == 'RIGHT':
                    snake_position[0] += 10
                
                
                
                
                snake_body.insert(0, list(snake_position))
                if snake_position[0] == fruit_position[0] and snake_position[1]  == fruit_position[1]:
                    score += 10
                    fruit_spawn = False
                else:
                    snake_body.pop()
                
                if not fruit_spawn:
                    fruit_position = [random.randrange(1, (Window_x//10)) * 10,
                                    random.randrange(1, (window_y//10)) * 10]
                
                fruit_spawn = True
                game_window.fill(black)
                
                for pos in snake_body:
                    pygame.draw.rect(game_window, green, pygame.Rect(
                        pos[0], pos[1], 10, 10
                    ))
                
                pygame.draw.rect(game_window, white, pygame.Rect(
                    fruit_position[0], fruit_position[1], 10, 10
                ))
                
                
                if snake_position[0] < 0 or snake_position[0] > Window_x-10:
                    game_over()
                if snake_position[1] < 0 or snake_position[1] > window_y-10:
                    game_over()
                
                for block in snake_body[1:]:
                    if snake_position[0] == block[0] and snake_position[1] == block[1]:
                        game_over()
                        
                show_score(1, white, 'timesnew roman', 20)
                
                pygame.display.update()
                
                fps.tick(snake_speed)
        
        if "exit" in query:
            speak("exiting program. Have a nice day")
            break


    '''
        if " send email" in query:
            
            content=query
            mail=smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            sender='mvl@gmail.com'
            recipient='tester@gmail.com'
            mail.login('mvl@gmail.com','******')
            header='To:'+receipient+'\n'+'From:' 
            +sender+'\n'+'subject:testmail\n'
            content=header+content
            mail.sendmail(sender, recipient, content)
            mail.close()

        if "arithmetic equation" in query:
        speak(f"what would you like to do ")
        print(f"WHAT WOULD YOU LIKE TO DO : ")
        query = takeCommand()
        
        
        if "addition" in query:
            query = query.replace('addition', "")
            speak("enter the first number " )
        
            a = input("enter the 1st number")
            a=int(a)
            result1=0
            for digit in a :
                result1 *= 10
                for d in '0123456789':
                    result1+=digit>d
                
            
            
            query = query.replace(a, "")
            speak("enter the second number ")
            
            b = input("enter the second number")
            b=int(b)
            result2=0
            for digit in a :
                result2 *= 10
                for d in '0123456789':
                    result2+=digit>d
                
            
            sum = (int(a)+int(b))
                    
            speak(f"sum = {sum}")
        
        
        if "value conversion" in query:
            speak("enter the the character you want to convert the value to")
            print("Enter The Value you want to convert : ")
            query = query.replace('ascii value',"")
            #v = takeCommand()
            v=int(input("no."))
            ascii_char = ord(v)
            speak(f"ascii value is : {ascii_char}")
            print(f"ascii value is : {ascii_char}")       
    '''