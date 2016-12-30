#!/usr/bin/env python2

import os
import logging as LG
import random
import commands

# create logger
logger = LG.getLogger(os.path.basename(__file__))
logger.setLevel(LG.DEBUG)

# create console handler and set level to debug
ch = LG.StreamHandler()
ch.setLevel(LG.DEBUG)

# create formatter
formatter = LG.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
## logger.debug('debug message')
## logger.info('info message')
## logger.warn('warn message')
## logger.error('error message')
## logger.critical('critical message')

def get_quotes():
    result = [ ]
    result.append("There is always light behind the clouds. -- Louisa May Alcott")
    result.append("Change before you have to. -- Jack Welch")
    result.append("If you can dream it, you can do it. -- Walt Disney")
    result.append("Love the life you live. Live the life you love. -- Bob Marley")
    result.append("My life didn't please me, so I created my life. -- Coco Chanel")
    result.append("It always seems impossible until it's done -- Nelson Mandela")
    result.append("Peace begins with a smile. -- Mother Teresa")
    result.append("Love dies only when growth stops. -- Pearl S. Buck")
    result.append("There is more to life than increasing its speed. -- Mahatma Gandhi")
    result.append("Everything is practice. -- Pele")
    result.append("Men willingly believe what they wish. -- Julius Caesar")
    result.append("If you want to be happy, be. -- Leo Tolstoy")
    result.append("Without haste, but without rest. -- Johann Wolfgang von Goethe")
    result.append("You'll never find a rainbow if you're looking down. -- Charlie Chaplin")
    result.append("Indecision is often worse than wrong action. -- Henry Ford")
    result.append("He who has never hoped can never despair. -- George Bernard Shaw")
    result.append("Love is more afraid of change than destruction. -- Friedrich Nietzsche")
    result.append("It's all about the journey, not the outcome. -- Carl Lewis")
    result.append("I will prepare and some day my chance will come. -- Abraham Lincoln")
    result.append("Do one thing everyday that scares you. -- Eleanor Roosevelt")
    result.append("Some people feel the rain. Others just get wet. -- Bob Marley")
    result.append("I like to be a free spirit. Some don't like that, but that's the way I am -- Diana, Princess of Wales")
    result.append("The man who has no imagination has no wings. -- Muhammad Ali")
    result.append("I don't dream at night, I dream all day; I dream for a living. -- Steven Spielberg")
    result.append("To say Good bye is to die a little. -- Raymond Chandler")
    result.append("Don't walk behind me; I may not lead. Don't walk in front me; I may not follow. Just walk beside me and be my friend -- Albert Camus")
    result.append("I can accept failure, everyone fails at something. But I can't accept not trying. -- Michael Jordan")
    result.append("Defeat? I do not recognize the meaning of the word. -- Margaret Thatcher")
    result.append("I do not seek, I find. -- Pablo Picasso")
    result.append("If I wasn't hard, I wouldn't be alive. If I couldn't ever be gentle, I wouldn't deserve to be alive. -- Raymond Chandler")
    result.append("A woman does not became interesting until she is over 40. -- Coco Chanel")
    result.append("We don't stop playing because we grow old; we grow old because we stop playing. -- George Bernard Shaw")
    result.append("Before you point your fingers, make sure your hands are clean. -- Bob Marley")
    result.append("Never, never, never, never give up. -- Winston Churchill")
    result.append("If you don't practice you don't deserve to win. -- Andre Agassi")
    result.append("You don't need any brains to listen to music. -- Luciano Pavarotti")
    result.append("Only the gentle are ever really strong. -- James Dean")
    result.append("I always looked ahead. -- Chris Evert")
    result.append("Living is not breathing but doing. -- Jean-Jacques Rousseau")
    result.append("You can't get away from yourself by moving from one place to another. -- Ernest Hemingway")
    result.append("It is not length of life, but depth of life. -- Ralph Waldo Emerson")
    result.append("This world is but a canvas to our imaginations. -- Henry David Thoreau")
    result.append("In the near future, I hope that we will be able to further the work that was started here. -- John Coltrane")
    result.append("Once I made a decision, I never thought about it again. -- Michael Jordan")
    result.append("Our life is our art. -- John Lennon")
    result.append("Art washes away from the soul the dust of everyday life. -- Pablo Picasso")
    result.append("All we're supposed to do, I feel, is try to make people happy. This is music that belongs to all of us, not just black or white - and I'm proud of it. -- Art Blakey")
    result.append("The real voyage of discovery consists not in seeking new landscapes, but in having new eyes. -- Marcel Proust")
    result.append("I keep my ideals, because in spite of everything I still believe that people are really good at heart. -- Anne Frank")
    result.append("I submit to you that if a man hasn't discovered something that he will die for, he isn't fit to live. -- Martin Luther King, Jr.")
    result.append("I have nothing to offer but blood, toil, tears, and sweat. -- Winston Churchill")
    result.append("I have done battle every single day of my life. -- Margaret Thatcher")
    result.append("Find purpose, the means will follow. -- Mahatma Gandhi")
    result.append("Do you want to spend the rest of your life selling sugared water, or do you want a chance to change the world? -- Steve Jobs")
    result.append("Whoever said, ''It's not whether you win or lose that counts,'' probably lost. -- Martina Navratilova")
    result.append("The best way to predict the future is to create it. -- Peter Drucker")
    result.append("Happiness does not lie in happiness, but in the achievement of it. -- Fyodor Dostoyevsky")
    result.append("Freedom is not worth having if it does not include the freedom to make mistakes. -- Mahatma Gandhi")
    result.append("A game is not won until it's lost. -- David Pleat")
    result.append("Dream as if you'll live forever, live as if you'll die today. -- James Dean")
    result.append("All we are saying is give peace a chance! -- John Lennon")
    result.append("A life is not important except in the impact it has on other lives. -- Jackie Robinson")
    result.append("Our greatest glory is not in never falling, but in rising up every time we fail. -- Ralph Waldo Emerson")
    result.append("It's been a long way, but we're here. -- Alan Shepard")
    result.append("Circumstances - what are circumstances? I make circumstances. -- Napoleon")
    result.append("Stay hungry. Stay foolish. -- Steve Jobs")
    result.append("Learn from the mistakes of others. You can't live long enough to make them all yourself. -- Eleanor Roosevelt")
    result.append("The pessimist complains about the wind; the optimist expects it to change; the realist adjusts the sails. -- William Arthur Ward")
    result.append("Life can only be understood backwards; but it must be lived forwards. -- Soren Kierkegaard")
    result.append("God doesn't require us to succeed; he only requires that you try. -- Mother Teresa")
    result.append("Many of life's failures are people who did not realize how close they were to success when they gave up. -- Thomas A. Edison")
    result.append("Anyone who has never made a mistake has never tried anything new. -- Albert Einstein")
    result.append("Life isn't about finding yourself. Life is about creating yourself. -- George Bernard Shaw")
    result.append("It is not what we get. But who we become, what we contribute that gives meaning to our lives. -- Anthony Robbins")
    result.append("The purpose of life is a life of purpose. -- Robert Byrne")
    result.append("To live is to climb the Andes: the more one climbs, the steeper become the precipices. -- Eucenio Maria De Hostos")
    result.append("You can't get away from yourself by moving from one place to another. -- Ernest Hemingway")
    result.append("The greatest mistake you can make in life is be continually fearing you will make one. -- Elbert Hubbard")
    result.append("The most important thing is to enjoy your life - to be happy - It's all that matters. -- Audrey Hepbarn")
    result.append("An investment in knowledge always pays the best interest. -- Benjamin Franklin")
    result.append("What do you want meaning for ? Life is desire, not meaning. -- Charlie Chaplin")
    result.append("The snake which cannot cast its skin has to die. As well the minds which are prevented from changing their opinions; they cease to be mind. -- Friedrich Nietzche")
    result.append("For one swallow does not make a summer, nor does one day; and so too one day, or a short time, does not make a man blessed and happy. -- Aristotle")
    result.append("Man lives freely only by his readiness to die. -- Mahatma Gandhi")
    result.append("One's philosophy is not best expressed in words; it is expressed in the choices one makes ... and the choice we make are ultimately our responsibility. -- Eleanor Roosevelt")
    result.append("Life is what happens to you while you're busy making other plans. -- John Lennon")
    result.append("If one advances confidently in the direction of his dreams, and endeavors to live the life which he has imagined, he will meet with a success unexpected in common hours. -- Henry David Thoreau")
    result.append("Real life is, to most men. a long second-best, a perpetual compromise between the ideal and the possible. -- Bertrand Russell")
    result.append("Life is not fair, get used to it. -- Bill Gates")
    result.append("Life is not complex. We are complex. Life is simple, and the simple thing is the right thing. -- Oscar Wilde")
    result.append("The greatest glory in living lies not in never falling, but in rising ever time we fall. -- Nelson Mandela")
    result.append("He is the happiest, be he king or peasant, who finds peace in his home. -- Johann Wolfgang von Goethe")
    result.append("In three words I can sum up everything I've learned about life: it goes on. -- Robert Frost")
    result.append("To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. -- Ralph Waldo Emerson")
    result.append("Life is like riding a bicycle. To keep your balance you must keep moving. -- Albert Einstein")
    result.append("Where there's hope, there's life. It fills us with fresh courage and makes us strong again. -- Anne Frank")
    result.append("To play billiards moderately well is the sign of a gentleman; to play it too well is the sign of a misspent life. -- Mark Twain")
    result.append("Life was meant to be lived, and curiosity must be kept alive. One must never, for whatever reason, turn his back on life. -- Eleanor Roosevelt")
    result.append("Take a chance! All life is a chance. The man who goes the farthest is generally the one who is willing to do and dare. -- Dale Carnegie")
    result.append("I count him braver who overcomes his desires than him who conquers his enemies; for the hardest victory is over self. -- Aristotle")
    result.append("There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle. -- Albert Einstein")
    result.append("Success is most often achieved by those who don't know that failure is inevitable. -- Coco Chanel")
    result.append("Life is an exciting business and most exciting when it is lived for others. -- helen keller")
    result.append("One thing life has taught me: If you are interested, you never have to look for new interests. They come to you. When you are genuinely interested in one thing, it will always lead to something else. -- Elenor Roosevelt")
    result.append("A successful man cannot realize how hard an unsuccessful man finds life. -- E. W. Howe")
    result.append("Most people are other people. Their thoughts are someone else's opinions, their lives a mimicry, their passions a quotation. -- Oscar Wilde")
    result.append("Life shouldn't be printed on dollar bills. -- Clifford Odets")
    result.append("I can think of nothing less pleasurable than a life devoted to pleasure. -- John D. Rockfeller, Jr.")
    result.append("Only put off until tomorrow what you are willing to die having left undone. -- Pablo Picasso")
    result.append("Try not to become a man of success but rather to become a man of value. -- Albert Einstein")
    result.append("The greatest happiness of life is the conviction that we are loved - loved for ourselves, or rather, loved in spite of ourselves. -- Victor Hugo")
    result.append("What can you do to promote world peace? Go home and love your family. -- Mother Teresa")
    result.append("The greatest use of life is spend it for something that will outlast it. -- William James")
    return result

'''
!! What a Wonderful World. !!
'''
if __name__ == "__main__":

    qs = get_quotes()
    qs.sort()
    msg = random.choice(qs)
    cmd = 'git commit -m "' + msg + '"; git push origin master;'
    print cmd



