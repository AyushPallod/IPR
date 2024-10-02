from tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk, ImageFilter

window = Tk()
window.title("Prop Quiz")
window.minsize(1600, 900)

score = 0  # Initialize the score
stories = {
    "Story 1": {  # copyright 1
        "text": """
        Emma is a talented photographer who loves capturing the beauty of nature. One day, she took a breathtaking photo of a sunrise over a misty forest.
        She shared it on social media, where it quickly went viral.
        A few weeks later, she discovered that a popular travel blog had used her photo in an article without her permission.

        The blog gave no credit to Emma, and she wasn't paid for her work. Feeling upset, Emma decided to take action.
        She learned that her photo was protected by copyright from the moment she created it.
        Emma contacted the blog, explaining her rights, and they eventually agreed to pay her for the photo and give her proper credit.
        """,
        "image": "story1.jpg"
    },
    "Story 2": {  # copyright 2
        "text": """
        Once upon a time in a small town, there lived a young artist named Maya.
        Maya loved creating beautiful paintings and often shared her artwork with her friends and family.
        One day, she painted a stunning landscape that everyone admired.
        Her friend, Alex, suggested that she should share it online to reach a larger audience.

        Maya decided to take Alex's advice and posted her painting on social media.
        To her surprise, the painting went viral, and people from all over the world started sharing it.
        However, Maya soon noticed that some people were using her painting for commercial purposes without her permission.
        This made her worried and sad.
        """,
        "image": "story2.jpg"  # Update the path to your image
    },
    "Story 3": {  # copyright 3
        "text": """
        Tom, an aspiring author, wrote a short story that he was proud of. He shared it on an online platform for writers, hoping to get feedback.
        To his surprise, a few months later, he found that someone had published a book using his story's exact plot and characters without his permission.

        Tom felt betrayed but learned that as the original author, he automatically held the copyright to his story.
        He reached out to the platform and the publisher, and after a legal process, Tom was recognized as the rightful author, and the book was taken down.
        """,
        "image": "story3.jpg"
    },
    "Story 4": {  # patent 1
        "text": """
        A scientist named Dr. Lee invented a new type of eco-friendly packaging material.
        The invention was revolutionary and attracted the attention of several companies.
        Dr. Lee was thrilled, but soon he discovered that some companies started producing similar materials without giving him any credit.

        Dr. Lee realized the importance of protecting his intellectual property and decided to look into patenting his invention.
        """,
        "image": "story4.jpg"  # Update the path to your image
    },
    "Story 5": {  # patent 2
        "text": """
        Raj, an innovative engineer, spent years developing a new type of portable charger that could fully charge a smartphone in just 10 minutes.
        Excited about his invention, he started selling it online.

        However, he soon discovered that another company had started selling a similar product that looked almost identical to his charger.
        Raj was worried that all his hard work would go to waste. Fortunately, he had filed a patent for his invention before releasing it to the public.
        With his patent in hand, Raj was able to stop the other company from selling the copycat product and secure his market share.
        """,
        "image": "story5.jpg"
    },
    "Story 6": {  # patent 3
        "text": """
        Lena, a talented musician, invented a unique instrument called the "Synthtar," which combined the features of a guitar and a synthesizer.
        The Synthtar created new, innovative sounds that amazed her audiences.
        Worried that others might copy her creation, Lena filed a patent to protect her invention.

        With the patent in place, she secured her rights to the Synthtar, preventing others from replicating it.
        Her invention quickly gained popularity, and Lena’s Synthtar became a revolutionary instrument in the music industry.
        """,
        "image": "story6.jpg"
    },
    "Story 7": {  # trademark 1
        "text": """
        Maya opened a small restaurant called "The Spicy Spoon," known for its delicious and fiery dishes.
        She designed a unique logo featuring a spoon with flames, which she used on her menu, signage, and even her social media.
        As her restaurant became popular, a new eatery opened nearby with a similar name and logo, causing confusion among customers.

        Maya realized she needed to protect her brand. She decided to register her logo as a trademark.
        Once her trademark was approved, Maya was able to stop the other restaurant from using a similar name and logo, ensuring her brand remained distinctive.
        """,
        "image": "story7.jpg"
    },
    "Story 8": {  # trademark 2
        "text": """ 
        Alex is a fashion designer known for his unique line of t-shirts featuring a distinctive logo.
        As his brand grew, he noticed that counterfeit products with similar logos started appearing in the market, confusing his customers.

        To protect his brand, Alex decided to register his logo as a trademark.
        With the trademark in place, Alex was able to take legal action against the counterfeiters and prevent them from selling the fake products.
        """,
        "image": "story8.jpg"
    },
    "Story 9": {  # trademark 3
        "text": """
        Nina, a visionary architect, became renowned for her innovative building designs that featured a distinctive spiral-shaped roof.
        Her unique architectural style made her buildings stand out, attracting prestigious clients worldwide.

        As her designs gained fame, other architects started copying the spiral roof, leading to confusion about which buildings were truly hers.    
        To protect her signature style, Nina decided to trademark the spiral roof design.
        With the trademark in place, she ensured that only her firm could use the distinctive design, preserving her reputation and keeping her work exclusive.
        """,
        "image": "story9.jpg"
    },
    "Story 10": {  # trade secret 1
        "text": """
        In a village, a farmer named Raj grew a unique type of organic vegetable that was in high demand.
        Seeing its popularity, other farmers started selling similar vegetables claiming them to be the same as Raj's.
        Raj was worried about losing his market and the authenticity of his product.

        Raj's friend advised him to look into obtaining a geographical indication for his unique vegetable to protect its uniqueness.
        """,
        "image": "story10.jpg"  # Update the path to your image
    },
    "Story 11": {  # trade secret 2
        "text": """
        Sarah runs a small, family-owned restaurant famous for its "Secret Sauce," a recipe that has been passed down through generations.
        The unique flavor of the sauce is what keeps customers coming back.
        Sarah has always been careful to keep the recipe a secret, only sharing it with her most trusted family members.

        One day, she discovers that a former employee is trying to sell a similar sauce to competitors.
        Fortunately, Sarah had ensured that all her employees signed confidentiality agreements, which legally protected her trade secret.
        She was able to stop the ex-employee from revealing the recipe and protect her restaurant's reputation.
        """,
        "image": "story11.jpg"
    },
    "Story 12": {  # trade secret 3
        "text": """
        Linda is the head of marketing at a tech startup that quickly rose to success thanks to a highly effective and innovative marketing strategy.
        This strategy was a trade secret, known only to a small team of executives.
        To keep it secure, the team communicated only through encrypted channels and stored all related documents in a secure, access-controlled environment.

        When a competitor tried to launch a similar campaign, they couldn’t match the impact because they didn’t have access to Linda's secret strategy.
        The startup continued to lead the market, with its marketing tactics remaining a well-guarded secret.
        """,
        "image": "story12.jpg"
    },
}


def select_story():
    story_selection_window = Toplevel(window)
    story_selection_window.title("Select a story you want to learn")
    story_selection_window.minsize(1600, 900)
    story_selection_window.state('zoomed')

    # Create canvas
    canvas = Canvas(story_selection_window, width=1600, height=900)
    canvas.pack(fill=BOTH, expand=True)

    # Load and process the background image
    image = Image.open("story_sel.jpeg")  # Replace with your image path
    image = image.resize((1600, 900), Image.LANCZOS)
    image = image.filter(ImageFilter.GaussianBlur(5))  # Apply blur

    # Apply opacity
    image = image.convert("RGBA")
    alpha = 100  # Set opacity (0 for transparent, 255 for opaque)
    image.putalpha(alpha)

    # Convert the processed image to ImageTk format
    background_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=background_image)
    canvas.image = background_image

    # Group the stories into sets of four
    story_groups = [list(stories.keys())[i:i + 3] for i in range(0, len(stories), 3)]
    title_names = ['Copyright', 'Patent', 'Trademark', 'Trade secret']
    button_width = 20  # Adjusted width of the button
    button_height = 2  # Height of the button
    button_style = {
        "bg": "#0080FF",  # Background color
        "activebackground": "#f7db7b",  # Active background color
        "bd": 0,  # No border
        "highlightthickness": 0,  # No highlight
        "fg": "#333333",  # Font color
        "font": ("Arial", 12, "bold"),  # Font style
        "anchor": CENTER,  # Center the text in the button
    }

    # Create buttons for each group
    for idx, group in enumerate(story_groups):
        # Calculate y position dynamically
        y_position = (idx - len(story_groups) / 2) * 50 + 65
        group_button = Button(story_selection_window, text=title_names[idx],
                              command=lambda grp=group: start_quiz(random.choice(grp), story_selection_window),
                              width=button_width, height=button_height, **button_style)
        group_button.place(relx=0.5, rely=0.5, y=y_position, anchor='center')
    close_button = Button(story_selection_window, text="Close",command=story_selection_window.destroy, width=button_width, height=button_height, **button_style)
    close_button.place(relx=0.5, rely=0.5, y=120, anchor='center')

def start_quiz(story_title, story_selection_window):
    global selected_story, selected_story_questions, selected_image
    selected_story = stories[story_title]["text"]
    selected_image = stories[story_title]["image"]
    selected_story_questions = get_questions_for_story(story_title)
    story_selection_window.destroy()
    quiz()


def get_questions_for_story(story_title):
    questions = {
        "Story 1": {  # copyright 1
            "What did Emma take a photo of?": {
                "Answer": "A sunrise over a misty forest",
                "Options": ["A sunset over the ocean", "A sunrise over a misty forest", "A city skyline at night",
                            "A snowy mountain peak"]
            },
            "Where did Emma share her photo?": {
                "Answer": "On social media",
                "Options": ["In a magazine", "On a website", "On social media", "In a photo gallery"]
            },
            "What right did Emma use to protect her photo?": {
                "Answer": "Copyright",
                "Options": ["Patent", "Trademark", "Copyright", "Trade secret"]
            },
            "How long does copyright protect Emma's photo?": {
                "Answer": "For her lifetime plus 70 years",
                "Options": ["10 years from creation", "50 years after it is published",
                            "For her lifetime plus 70 years", "As long as it remains online"]
            },
            "Who can give permission to use Emma’s photo?": {
                "Answer": "Only Emma",
                "Options": ["The social media platform", "Anyone who sees the photo", "Only Emma", "The travel blog"]
            }
        },
        "Story 2": {  # copyright 2
            "What should Maya do to protect her painting legally?": {
                "Answer": "Register it under copyright",
                "Options": ["Keep it offline", "Sell the painting", "Ignore the issue", "Register it under copyright"]
            },
            "What IP right will Maya be using here?": {
                "Answer": "Copyright",
                "Options": ["Patent", "Copyright", "Trademark", "Inventions"]
            },
            "What can registering a painting under copyright do for Maya?": {
                "Answer": "Protect it from being used without permission",
                "Options": ["Make it more valuable", "Increase its visibility online",
                            "Protect it from being used without permission", "Allow anyone to use it freely"]
            },
            "What are Intellectual Property (IP) rights?": {
                "Answer": "Rights protecting creative works like paintings",
                "Options": ["Rights protecting physical property", "Rights protecting creative works like paintings",
                            "Rights to share any online content", "Rights to free use of public domain works"]
            },
            "Why is it important to respect others' IP rights?": {
                "Answer": "It encourages more creativity",
                "Options": ["It encourages more creativity", "It allows free use of all content",
                            "It decreases the value of works", "It has no impact"]
            }
        },
        "Story 3": {  # copyright 3
            "What did Tom discover someone had done with his story?": {
                "Answer": "Used it without permission",
                "Options": ["Translated it", "Used it without permission", "Edited it", "Deleted it"]
            },
            "What legal right did Tom automatically have over his story": {
                "Answer": "Copyright",
                "Options": ["Trademark", "Patent", "Copyright", "License"]
            },
            "What action did Tom take after discovering the unauthorized use of his story?": {
                "Answer": "He reached out to the platform and publisher",
                "Options": ["He rewrote the story", "He ignored it", "He reached out to the platform and publisher",
                            "He sold the rights"]
            },
            "What was the result of Tom's legal process?": {
                "Answer": "The book using his story was taken down",
                "Options": ["He lost his rights to the story", "The book using his story was taken down",
                            "He was fined", "The story was published again"]
            },
            "Why was Tom recognized as the rightful author?": {
                "Answer": "Because he held the copyright as the original author",
                "Options": ["Because he was famous", "Because he had a trademark",
                            "Because he held the copyright as the original author", "Because he paid for it"]
            }
        },
        "Story 4": {  # patent 1
            "What should Dr. Lee do to protect his invention?": {
                "Answer": "File a patent",
                "Options": ["File a trademark", "File a copyright", "File a patent", "Do nothing"]
            },
            "How does a patent help inventors?": {
                "Answer": "It gives them exclusive rights to their invention",
                "Options": ["It gives them exclusive rights to their invention",
                            "It allows anyone to use their invention",
                            "It decreases the value of their invention", "It has no impact on their invention"]
            }
        },
        "story 5": {  # patent 2
            "What did Raj invent?": {
                "Answer": "A portable charger",
                "Options": ["A new smartphone", "A portable charger", "A wireless speaker", "A smart thermostat"]
            },
            "What problem did Raj face after he started selling his invention online?": {
                "Answer": "Another company started selling a similar product",
                "Options": ["Another company started selling a similar product", "Customers didn’t like his product",
                            "His charger didn’t work properly", "He couldn’t keep up with demand"]
            },
            "How did Raj protect his invention from being copied?": {
                "Answer": "He patented his invention",
                "Options": ["He trademarked his invention", "He kept it a trade secret", "He patented his invention",
                            "He copyrighted his invention"]
            },
            "What did Raj’s patent allow him to do?": {
                "Answer": "Stop the other company from selling the copycat product",
                "Options": ["Improve his invention", "Sell his invention to another company",
                            "Make his invention open-source", "Stop the other company from selling the copycat product"]
            },
            "Why was filing a patent important for Raj?": {
                "Answer": "It prevented others from copying his invention and protected his market share",
                "Options": ["It helped him sell more products",
                            "It prevented others from copying his invention and protected his market share",
                            "It made his invention more expensive",
                            "It allowed him to change the design of his charger"]
            }
        },
        "Story 6": {  # patent 3
            "What two instruments did Lena combine to create the Synthtar?": {
                "Answer": "Guitar and Synthesizer",
                "Options": ["Piano and Drum", "Violin and Keyboard", "Guitar and Synthesizer", "Flute and Harp"]
            },
            "What was the name of the unique instrument Lena invented?": {
                "Answer": "Synthtar",
                "Options": ["GuitSynth", "SynthGuitar", "Guitaro", "Synthtar"]
            },
            "Why did Lena decide to file a patent for her invention?": {
                "Answer": "To protect her invention from being copied",
                "Options": ["To sell her instrument", "To protect her invention from being copied",
                            "To give her invention away for free", "To start a new band"]
            },
            "What impact did Lena’s patent have on her invention?": {
                "Answer": "It secured her rights to the Synthtar and prevented replication",
                "Options": ["It allowed others to use her invention freely",
                            "It secured her rights to the Synthtar and prevented replication",
                            "It made her invention less popular", "It made her quit music"]
            },
            "For how long does a patent typically protect an invention?": {
                "Answer": "20 years",
                "Options": ["5 years", "10 years", "20 years", "50 years"]
            }
        },
        "Story 7": {  # trademark 1
            "What was the name of Maya’s restaurant?": {
                "Answer": "The Spicy Spoon",
                "Options": ["The Hot Spoon", "The Spicy Spoon", "The Fiery Fork", "The Flaming Fork"]
            },
            "What was unique about Maya’s restaurant logo?": {
                "Answer": "A spoon with flames",
                "Options": ["A spoon with flames", "A fork with fire", "A bowl with steam", "A knife with sparks"]
            },
            "Why did Maya decide to register her logo as a trademark?": {
                "Answer": "To protect her brand from being copied",
                "Options": ["To make her logo more colorful", "To protect her brand from being copied",
                            "To redesign her restaurant’s logo", "To sell her restaurant"]
            },
            "What problem did Maya face when a new eatery opened nearby?": {
                "Answer": "The new eatery used a similar name and logo",
                "Options": ["The new eatery had better food", "The new eatery used a similar name and logo",
                            "The new eatery was more popular", "The new eatery offered similar discounts"]
            },
            "What was the result after Maya’s trademark was approved?": {
                "Answer": "She was able to stop the other restaurant from using a similar name and logo",
                "Options": ["She had to redesign her logo", "She sold her restaurant",
                            "She was able to stop the other restaurant from using a similar name and logo",
                            "She opened a new branch"]
            }
        },
        "Story 8": {  # trademark 2
            "What type of products does Alex design?": {
                "Answer": "T-shirts",
                "Options": ["Shoes", "Hats", "T-shirts", "Bags"]
            },
            "What problem did Alex face as his brand grew?": {
                "Answer": "Counterfeit products with similar logos appeared in the market",
                "Options": ["Customers stopped buying his products", "Other designers copied his designs",
                            "Counterfeit products with similar logos appeared in the market",
                            "His logo was not popular"]
            },
            "Why did Alex decide to register his logo as a trademark?": {
                "Answer": "To protect his brand from counterfeit products",
                "Options": ["To change his logo", "To protect his brand from counterfeit products", "To sell his brand",
                            "To create new designs"]
            },
            "What legal action was Alex able to take after registering his trademark?": {
                "Answer": "He could stop counterfeiters from selling fake products",
                "Options": ["He could change his logo", "He could prevent others from copying his designs",
                            "He could stop counterfeiters from selling fake products", "He could sue his customers"]
            },
            "What did the counterfeit products cause among Alex's customers?": {
                "Answer": "Confusion",
                "Options": ["Excitement", "Confusion", "Satisfaction", "Increased sales"]
            },
        },
        "Story 9": {  # trademark 3
            "What does a trademark protect in Nina’s case?": {
                "Answer": "The spiral-shaped roof design",
                "Options": ["The color of the buildings", "The location of her buildings",
                            "The materials used in the construction", "The spiral-shaped roof design"]
            },
            "What could happen if Nina did not trademark her spiral roof design?": {
                "Answer": "Her design could be freely copied by others",
                "Options": ["Her design could be freely copied by others", "Her buildings would be more expensive",
                            "Her clients would stop hiring her", "Her buildings would become less attractive"]
            },
            "Which of the following is a benefit of trademarking a design like Nina's?": {
                "Answer": "It provides legal protection against unauthorized use",
                "Options": ["It makes the design more complex", "It allows the design to be sold to other firms",
                            "It provides legal protection against unauthorized use",
                            "It reduces the cost of construction"]
            },
            "What is a key characteristic of a trademark?": {
                "Answer": "It can be a word, symbol, or design that identifies and distinguishes goods or services",
                "Options": ["It is automatically granted without registration",
                            "It can be a word, symbol, or design that identifies and distinguishes goods or services",
                            "It protects the physical appearance of a product", "It is only used for digital products"]
            },
            "What distinguishes a trademark from other forms of intellectual property like patents or copyrights?": {
                "Answer": "Trademarks protect brand names and logos, while patents protect inventions",
                "Options": ["Trademarks are only valid for physical objects",
                            "Trademarks protect brand names and logos, while patents protect inventions",
                            "Trademarks last forever without renewal", "Trademarks can only be used in one country"]
            }
        },
        "Story 10": {  # trade secret 1
            "What can Raj do to protect the uniqueness of his vegetable?": {
                "Answer": "Obtain a geographical indication",
                "Options": ["File a patent", "File a trademark", "Obtain a geographical indication", "Do nothing"]
            },
            "What is the benefit of a geographical indication?": {
                "Answer": "It helps protect the authenticity of products from a specific region",
                "Options": ["It helps protect the authenticity of products from a specific region",
                            "It allows free use of the product",
                            "It makes the product more expensive", "It has no impact on the product"]
            }
        },
        "Story 11": {  # trade secret 11
            "What makes Sarah's restaurant famous?": {
                "Answer": "Its Secret Sauce",
                "Options": ["Its desserts", "Its Secret Sauce", "Its decor", "Its location"]
            },
            "Who did Sarah share the Secret Sauce recipe with?": {
                "Answer": "Only her most trusted family members",
                "Options": ["All her customers", "Everyone on her staff", "Only her most trusted family members",
                            "The chef of a competing restaurant"]
            },
            "What did Sarah require her employees to sign to protect the Secret Sauce?": {
                "Answer": "A confidentiality agreement",
                "Options": ["A contract of employment", "A non-compete agreement", "A confidentiality agreement",
                            "A marketing agreement"]
            },
            "What did the former employee try to do with a similar sauce?": {
                "Answer": "Sell it to competitors",
                "Options": ["Serve it in another restaurant", "Sell it to Sarah’s customers", "Sell it to competitors",
                            "Use it in their own cooking"]
            },
            "How was Sarah able to protect her Secret Sauce recipe from being revealed?": {
                "Answer": "By using the confidentiality agreements",
                "Options": ["By changing the recipe", "By using the confidentiality agreements",
                            "By opening a new restaurant", "By publicly sharing the recipe"]
            }
        },
        "Story 12": {  # trade secret 3
            "What was the key to the tech startup’s success?": {
                "Answer": "Its highly effective marketing strategy",
                "Options": ["Its innovative product", "Its large customer base", "Its affordable pricing",
                            "Its highly effective marketing strategy"]
            },
            "Who knew about the secret marketing strategy?": {
                "Answer": "A small team of executives",
                "Options": ["The entire company", "A small team of executives", "The customers", "The competitors"]
            },
            "How did the team ensure the marketing strategy remained a secret?": {
                "Answer": "By communicating through encrypted channels and using secure, access-controlled environments",
                "Options": ["By sharing it publicly", "By storing it in an open file",
                            "By communicating through encrypted channels and using secure, access-controlled environments",
                            "By printing it out and filing it"]
            },
            "What happened when a competitor tried to launch a similar campaign?": {
                "Answer": "They couldn’t match the impact because they didn’t have access to the secret strategy",
                "Options": ["They succeeded in matching the startup's success",
                            "They couldn’t match the impact because they didn’t have access to the secret strategy",
                            "They outperformed the startup", "They were able to steal the strategy"]
            },
            "What was the result of keeping the marketing strategy a well-guarded secret?": {
                "Answer": "The startup continued to lead the market",
                "Options": ["The startup continued to lead the market", "The startup lost its market position",
                            "The competitors surpassed the startup", "The strategy was eventually leaked"]
            }
        }
    }
    return questions[story_title]


def quiz():
    global score, username, question_index
    score = 0
    question_index = 0
    story_window = Toplevel(window)
    story_window.title("Story")
    story_window.minsize(1600, 900)
    story_window.state('zoomed')
    # Set up the canvas for the background image
    canvas = Canvas(story_window, width=1600, height=900)
    canvas.pack(fill=BOTH, expand=True)
    image = Image.open(selected_image)
    image = image.resize((1600, 900), Image.LANCZOS)  # Resize as needed
    image = image.filter(ImageFilter.GaussianBlur(5))  # Adjust the radius as needed

    # Apply opacity
    image = image.convert("RGBA")
    alpha = 100  # Set opacity (0 for transparent, 255 for opaque)
    image.putalpha(alpha)

    # Convert the processed image to ImageTk format
    background_image = ImageTk.PhotoImage(image)

    # Add the image to the canvas
    canvas.create_image(0, 0, anchor=NW, image=background_image)
    canvas.image = background_image

    # Display the story text with bold font and transparent background
    story_text = canvas.create_text(400, 300, text=selected_story, font=("Serif", 14, "bold", "italic"), fill="black",
                                    width=700)

    quest_button = Button(story_window, text="Questions", command=lambda: [display_question(story_window)])
    quest_button.place(relx=0.5, rely=0.5, y=250, anchor='center', width=70, height=30)


def display_question(story_window):
    global question_index, score, selected_story_questions

    if question_index < len(selected_story_questions):
        question, data = list(selected_story_questions.items())[question_index]
        correct_answer = data["Answer"]
        options = data["Options"]

        quiz_window = Toplevel(window)
        quiz_window.title("Property Quiz")
        quiz_window.minsize(600, 500)

        # Score display in the top left corner
        score_label = Label(quiz_window, text=f"Score: {score}", font=("Arial", 12))
        score_label.grid(row=0, column=0, sticky=W, padx=20, pady=10)

        # Center the question in the middle
        question_label = Label(quiz_window, text="Question: " + question, font=("Arial", 14, "bold"))
        question_label.grid(row=1, column=0, columnspan=3, pady=50, padx=20)

        answer_var = StringVar()

        # Display the options below the question
        for idx, option in enumerate(options):
            option_radio = Radiobutton(quiz_window, text=option, variable=answer_var, value=option)
            option_radio.grid(row=2 + idx, column=0, columnspan=3, sticky="w", padx=20, pady=5)

        # Submit button at the bottom
        submit_button = Button(quiz_window, text="Submit",
                               command=lambda: check_answer(quiz_window, correct_answer, answer_var, story_window))
        submit_button.grid(row=3 + len(options), column=2, pady=20, padx=10, sticky=E)

    else:
        end_quiz()


def check_answer(quiz_window, correct_answer, answer_var, story_window):
    global score, question_index
    user_answer = answer_var.get()
    if user_answer == correct_answer:
        feedback = "Correct!"
        score += 1
    else:
        feedback = f"Incorrect! The correct answer is: {correct_answer}"
        score -= 0.25

    feedback_label = Label(quiz_window, text=feedback, font=("Arial", 12))
    feedback_label.grid(row=6, column=0, columnspan=2, pady=10)
    next_button = Button(quiz_window, text="Next Question", command=lambda: [quiz_window.destroy(), next_question()])
    next_button.grid(row=7, column=1, pady=10, padx=10, sticky=W)
    end_button = Button(quiz_window, text="End Quiz",
                        command=lambda: [quiz_window.destroy(), end_quiz(), story_window.destroy()])
    end_button.grid(row=7, column=0, pady=10, padx=10, sticky=E)


def next_question():
    global question_index
    question_index += 1
    display_question(story_window=None)  # Continue to the next question


def end_quiz():
    global score
    end_window = Toplevel(window)
    end_window.title("Quiz Ended")
    end_window.maxsize(1600, 900)
    score_label = Label(end_window, text=f"Final Score: {score}", font=("Arial", 12))
    score_label.pack(pady=10)
    close_button = Button(end_window, text="Close", command=lambda: [end_window.destroy()])
    close_button.pack(pady=10)


def law():
    law_window = Toplevel(window)
    law_window.title("List of laws")
    law_window.minsize(1600, 900)
    law_window.state('zoomed')

    # Create canvas
    canvas = Canvas(law_window, width=1600, height=900)
    canvas.pack(fill=BOTH, expand=True)

    # Load and process the background image
    image = Image.open("law.jpeg")
    image = image.resize((1600, 900), Image.LANCZOS)
    image = image.filter(ImageFilter.GaussianBlur(5))  # Apply blur

    # Apply opacity
    image = image.convert("RGBA")
    alpha = 100  # Set opacity
    image.putalpha(alpha)

    # Convert the processed image to ImageTk format
    background_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=background_image)
    canvas.image = background_image

    # Property laws data
    property_laws = {
        "The Patents Act, 1970": "This act provides the legal framework for the protection of inventions. It outlines the process for applying for patents, the rights of patent holders, and the penalties for patent infringement.",
        "The Trade Marks Act, 1999": "This act governs the registration, protection, and enforcement of trademarks in India. A trademark can be a word, logo, symbol, or design that distinguishes goods or services.",
        "The Copyright Act, 1957": "This act protects original literary, dramatic, musical, and artistic works, as well as cinematograph films and sound recordings.",
        "The Designs Act, 2000": "This act provides protection for new and original designs, which refer to the shape, configuration, pattern, or ornamentation applied to an article by any industrial process.",
        "The Geographical Indications of Goods (Registration and Protection) Act, 1999": "This act provides protection for geographical indications (GIs), which are signs used on goods that have a specific geographical origin and possess qualities or a reputation due to that origin.",
        "The Protection of Plant Varieties and Farmers’ Rights Act, 2001": "This act aims to protect the rights of plant breeders and farmers by recognizing and protecting new plant varieties.",
        "The Semiconductor Integrated Circuits Layout-Design Act, 2000": "This act provides protection for the layout designs of semiconductor integrated circuits.",
        "The Biological Diversity Act, 2002": "This act aims to preserve biological diversity in India and provides mechanisms for equitable sharing of benefits arising from the use of biological resources.",
        "Property Management Laws": "Governs the management and maintenance of properties."
    }

    # Add labels with laws
    num_laws = len(property_laws)

    for idx, (law, description) in enumerate(property_laws.items()):
        law_text = f"{law}: {description}"
        # Create the label
        law_label = Label(law_window, text=law_text, font=("Arial", 12, "bold"), fg='#333333',
                          wraplength=1000, justify=CENTER, bg='azure2')  # Transparent background
        law_label.place(x=300, y=100 + idx * 70, anchor=W)

    # Add close button
    close_button = Button(law_window, text="Close", command=law_window.destroy)
    close_button.place(x=800, y=750, anchor=CENTER)


def website():
    web_window = Toplevel(window)
    web_window.title("List of websites")
    web_window.minsize(1600, 900)
    web_window.state('zoomed')

    # Create canvas
    canvas = Canvas(web_window, width=1600, height=900)
    canvas.pack(fill=BOTH, expand=True)

    # Load and process the background image
    image = Image.open("website.jpeg")
    image = image.resize((1600, 900), Image.LANCZOS)
    image = image.filter(ImageFilter.GaussianBlur(5))  # Apply blur

    # Apply opacity
    image = image.convert("RGBA")
    alpha = 100  # Set opacity
    image.putalpha(alpha)

    # Convert the processed image to ImageTk format
    background_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=background_image)
    canvas.image = background_image

    government_websites = {
        "Intellectual Property India": "https://www.ipindia.gov.in/",
        "World Intellectual Property Organization (WIPO)": "https://www.wipo.int/portal/en/index.html",
        "Indian Patent Office": "https://www.ipindia.gov.in/",
        "Controller General of Patents, Designs & Trade Marks (CGPDTM)": "https://www.ipindia.gov.in/",
        "Copyright Office, India": "https://copyright.gov.in/",
        "National Innovation Foundation-India (NIF)": "https://www.nif.org.in/",
        "Indian Council of Agricultural Research (ICAR)": "https://www.icar.org.in/",
        "Ministry of Commerce and Industry, Government of India": "https://commerce.gov.in/",
        "National Biodiversity Authority (NBA)": "http://nbaindia.org/",
        "Legal Information Institute of India": "http://www.liiofindia.org/"
    }

    num_laws = len(government_websites)

    for idx, (law, description) in enumerate(government_websites.items()):
        law_text = f"{law}: {description}"
        # Create the label
        law_label = Label(web_window, text=law_text, font=("Arial", 12, "bold"), fg='#333333',
                          wraplength=1000, justify=CENTER, bg='azure2')  # Transparent background
        law_label.place(x=300, y=100 + idx * 70, anchor=W)

    # Add close button
    close_button = Button(web_window, text="Close", command=web_window.destroy)
    close_button.place(x=800, y=750, anchor=CENTER)


def open_url(url):
    import webbrowser
    webbrowser.open(url)


canvas = Canvas(window, width=1600, height=900)
canvas.pack(fill=BOTH, expand=True)
image = Image.open("welcome.jpg")
image = image.resize((1600, 900), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=NW, image=background_image)
canvas.image = background_image  # Keep a reference to avoid garbage collection

# Create buttons with transparent background
button_width = 10  # Width of the button
button_height = 2  # Height of the button

button_style = {
    "bg": "#f7db7b",  # Match this with the image's main color or transparent color
    "activebackground": "#f7db7b",
    "bd": 0,  # Remove border
    "highlightthickness": 0,  # Remove focus highlight
    "fg": "#333333",  # Font color
    "font": ("Arial", 12, "bold")  # Font style
}

quiz_button = Button(window, text="Quiz", command=select_story, width=button_width, height=button_height,
                     **button_style)
laws_button = Button(window, text="Laws", command=law, width=button_width, height=button_height, **button_style)
website_button = Button(window, text="Websites", command=website, width=button_width, height=button_height,
                        **button_style)
end_button = Button(window, text="Close", command=lambda: [window.destroy()], width=button_width, height=button_height,
                    **button_style)

# Calculate the y-coordinate to vertically center the buttons
button_y = 200  # Center position along the y-axis

# Place buttons in the center of the window
quiz_button.place(relx=0.5, rely=0.5, y=button_y - 60, anchor='center')
laws_button.place(relx=0.5, rely=0.5, y=button_y - 20, anchor='center')
website_button.place(relx=0.5, rely=0.5, y=button_y + 20, anchor='center')
end_button.place(relx=0.5, rely=0.5, y=button_y + 60, anchor='center')
window.state('zoomed')
# Start the main event loop
window.mainloop()
